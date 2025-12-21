from collections import defaultdict
from transformers import pipeline, AutoTokenizer
from typing import Dict

class EmotionAnalyzer:
    def __init__(self, model_name: str = "j-hartmann/emotion-english-distilroberta-base"):
        """Initializes the model on the CPU."""
        # device=-1 explicitly forces the use of CPU
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
        tokens = self.tokenizer.encode(text)
        chunks = [tokens[i:i + self.max_tokens] for i in range(0, len(tokens), self.max_tokens)]
        return [self.tokenizer.decode(chunk) for chunk in chunks]

    def get_raw_scores(self, text: str) -> Dict[str, float]:
        """Calculates averaged emotion scores for the given text on CPU."""
        if len(self.tokenizer.encode(text)) <= self.max_tokens:
            result = self.classifier(text)[0]
            return {item['label']: item['score'] for item in result}

        chunks = self._chunk_text(text)
        cumulative_scores = defaultdict(float)
        total_chars = 0

        for chunk in chunks:
            result = self.classifier(chunk)[0]
            chunk_len = len(chunk)
            total_chars += chunk_len
            for item in result:
                cumulative_scores[item['label']] += item['score'] * chunk_len

        return {label: score / total_chars for label, score in cumulative_scores.items()}

    def predict_levels(self, text: str) -> Dict[str, int]:
        """Maps emotions to Fear, Stress, Morale, and Trust levels (1-3)."""
        emotions = self.get_raw_scores(text)
        
        fear = emotions.get("fear", 0)
        anger = emotions.get("anger", 0)
        neutral = emotions.get("neutral", 0)
        disgust = emotions.get("disgust", 0)
        sadness = emotions.get("sadness", 0)
        joy = emotions.get("joy", 0)

        # Logic for Fear, Stress, Morale, Trust Levels
        fsmt_dict = {}
        
        # Fear Level
        if fear > (anger + neutral + disgust + sadness + joy) or fear > 0.8:
            fsmt_dict["Fear Level"] = 3
        elif fear > 0.5 or fear > (joy + neutral):
            fsmt_dict["Fear Level"] = 2
        else:
            fsmt_dict["Fear Level"] = 1

        # Stress Level
        if (sadness + anger) > (joy + neutral) or fsmt_dict["Fear Level"] == 3:
            fsmt_dict["Stress Level"] = 3
        elif (sadness + anger) > 0.5 or fsmt_dict["Fear Level"] == 2:
            fsmt_dict["Stress Level"] = 2
        else:
            fsmt_dict["Stress Level"] = 1

        # Morale Level
        if (sadness + disgust + fear) < (neutral + joy):
            fsmt_dict["Morale Level"] = 3
        elif (joy + neutral) > 0.5:
            fsmt_dict["Morale Level"] = 2
        else:
            fsmt_dict["Morale Level"] = 1

        # Trust Level
        if (sadness + disgust + fear) < joy:
            fsmt_dict["Trust Level"] = 3
        elif (joy + neutral) > (sadness + disgust + fear):
            fsmt_dict["Trust Level"] = 2
        else:
            fsmt_dict["Trust Level"] = 1

        return fsmt_dict

if __name__ == "__main__":
    analyzer = EmotionAnalyzer()
    print("Analyzer ready. Enter text to analyze (or 'exit' to quit):")
    while True:
        user_input = input("> ")
        if user_input.lower() == 'exit':
            break
        print(analyzer.predict_levels(user_input))