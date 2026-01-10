import pandas as pd
import os
from collections import defaultdict
from transformers import pipeline, AutoTokenizer
from typing import Dict

class EmotionAnalyzer:
    def __init__(self, model_name: str = "j-hartmann/emotion-english-distilroberta-base"):
        """Initializes the model on the CPU."""
        self.device = -1 
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.classifier = pipeline(
            "text-classification",
            model=model_name,
            top_k=None,
            device=self.device
        )
        self.max_tokens = 400

    def _chunk_text(self, text: str):
        """Splits long text into smaller chunks."""
        tokens = self.tokenizer.encode(str(text))
        chunks = [tokens[i:i + self.max_tokens] for i in range(0, len(tokens), self.max_tokens)]
        return [self.tokenizer.decode(chunk) for chunk in chunks]

    def get_raw_scores(self, text: str) -> Dict[str, float]:
        """Calculates averaged emotion scores for the given text on CPU."""
        text_str = str(text)
        if len(self.tokenizer.encode(text_str)) <= self.max_tokens:
            result = self.classifier(text_str)[0]
            return {item['label']: item['score'] for item in result}

        chunks = self._chunk_text(text_str)
        cumulative_scores = defaultdict(float)
        total_chars = 0

        for chunk in chunks:
            result = self.classifier(chunk)[0]
            chunk_len = len(chunk)
            total_chars += chunk_len
            for item in result:
                cumulative_scores[item['label']] += item['score'] * chunk_len

        return {label: score / total_chars for label, score in cumulative_scores.items()}

    def predict_levels(self, text: str):
        """Maps emotions to Fear, Stress, Morale, and Trust levels (1-3)."""
        emotions = self.get_raw_scores(text)
        
        fear = emotions.get("fear", 0)
        anger = emotions.get("anger", 0)
        neutral = emotions.get("neutral", 0)
        disgust = emotions.get("disgust", 0)
        sadness = emotions.get("sadness", 0)
        joy = emotions.get("joy", 0)

        results = {}

        # Fear Level
        if fear > (anger + neutral + disgust + sadness + joy) or fear > 0.8:
            results["Fear Level"] = 3
        elif fear > 0.5 or fear > (joy + neutral):
            results["Fear Level"] = 2
        else:
            results["Fear Level"] = 1

        # Stress Level
        if (sadness + anger) > (joy + neutral) or results["Fear Level"] == 3:
            results["Stress Level"] = 3
        elif (sadness + anger) > 0.5 or results["Fear Level"] == 2:
            results["Stress Level"] = 2
        else:
            results["Stress Level"] = 1

        # Morale Level
        if (sadness + disgust + fear) < (neutral + joy):
            results["Morale Level"] = 3
        elif (joy + neutral) > 0.5:
            results["Morale Level"] = 2
        else:
            results["Morale Level"] = 1

        # Trust Level
        if (sadness + disgust + fear) < joy:
            results["Trust Level"] = 3
        elif (joy + neutral) > (sadness + disgust + fear):
            results["Trust Level"] = 2
        else:
            results["Trust Level"] = 1

        # Return as a Series so pandas can easily expand it into columns
        return pd.Series(results)

def main():
    analyzer = EmotionAnalyzer()
    
    # 1. Input CSV file path
    file_path = input("Enter the path to your CSV file: ").strip()
    
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    try:
        # 2. Load data
        df = pd.read_csv(file_path)
        print(f"Loaded {len(df)} rows.")
        print(f"Columns: {list(df.columns)}")
        
        target_column = input("Enter the column name containing the text to analyze: ").strip()
        if target_column not in df.columns:
            print("Error: Column not found.")
            return

        # 3. Process each row
        print("Analyzing text and updating columns... (this may take a moment)")
        
        # Apply the predict_levels function to the text column
        # This returns 4 values which are mapped to 4 new columns
        analysis_df = df[target_column].apply(analyzer.predict_levels)
        
        # Join the new columns back to the original dataframe
        df = pd.concat([df, analysis_df], axis=1)

        # 4. Save the updated CSV
        output_file = file_path.replace(".csv", "_analyzed.csv")
        df.to_csv(output_file, index=False)
        
        print("-" * 30)
        print(f"Success! Analyzed file saved as: {output_file}")
        print(df[['Fear Level', 'Stress Level', 'Morale Level', 'Trust Level']].head())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()