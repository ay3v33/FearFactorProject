import argparse
import pandas as pd
import torch
from transformers import pipeline
from datasets import Dataset
from transformers.pipelines.pt_utils import KeyDataset

if torch.cuda.is_available():
    print(f"GPU Name: {torch.cuda.get_device_name(0)}")

def run_analysis(input_path, output_path):
    # 1. Load Data
    print(f"Loading data from: {input_path}")
    df = pd.read_csv(input_path)
    dataset = Dataset.from_pandas(df[['text']])

    # 2. Initialize Pipeline
    # Automatically uses GPU if available, otherwise CPU
    device = 0 if torch.cuda.is_available() else -1
    pipe = pipeline(
        "zero-shot-classification", 
        model="./code/bartLargeMnli", 
        device=device,
    )

    # 3. Define Simulation Dimensions
    dimensions = {
        "fear": {
            "labels": ["safe and secure", "moderate tension", "extreme panic and terror"],
            "template": "From a US-allied perspective, the civilian fear level is {}."
        },
        "stress": {
            "labels": ["calm and relaxed", "busy and alert", "overwhelmed and traumatized"],
            "template": "From a US-allied perspective, the speaker's stress level is {}."
        },
        "morale": {
            "labels": ["defeated and hopeless", "indifferent" , "hopeful and motivated"],
            "template": "From a US-allied perspective, the morale of the speaker is {}."
        },
        "trust": {
            "labels": ["betrayed and suspicious of leadership", "skeptical", "loyal and confident in leadership"],
            "template": "From a US-allied perspective, the trust in US/NATO is {}."
        }
    }

    # 4. Process Dimensions
    for dim_name, config in dimensions.items():
        print(f"Processing {dim_name.upper()}...")
        scores_for_dim = []
        labels = config["labels"]
        
        for out in pipe(KeyDataset(dataset, "text"), 
                        candidate_labels=labels, 
                        hypothesis_template=config["template"],
                        batch_size=32, 
                        truncation=True):
            
            s = dict(zip(out['labels'], out['scores']))
            # Result is (Bad_Prob - Good_Prob) to get -1 to 1 scale
            score = s[labels[2]] - s[labels[0]]
            scores_for_dim.append(round(score, 3))
        
        df[f'val_{dim_name}'] = scores_for_dim

    # 5. Save Output
    df.to_csv(output_path, index=False)
    print(f"Analysis complete. Results saved to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze war simulation text for psychological dimensions.")
    parser.add_argument("input", help="Path to the input CSV file")
    parser.add_argument("--output", default="simulation_results.csv", help="Path for the output CSV file")
    
    args = parser.parse_args()
    run_analysis(args.input, args.output)
    