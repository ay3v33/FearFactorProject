# requirements: transformers, datasets, evaluate, torch
from datasets import load_dataset, Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
import numpy as np
import torch
import evaluate

model_name = "distilroberta-base"  # or "roberta-base", or your starting checkpoint

# --- Example toy dataset (replace with your labeled data) ---
data = [
  {"text":"An invasion is imminent!", "labels":[0.9, 0.6, -0.8, -0.7]},
  {"text":"We have enough food today.", "labels":[-0.2, -0.1, 0.7, 0.3]},
  # ... more examples ...
]
ds = Dataset.from_list(data)
# split
ds = ds.train_test_split(test_size=0.1, seed=42)

# --- Tokenizer & model (regression head with 4 outputs) ---
tokenizer = AutoTokenizer.from_pretrained(model_name)
def preprocess(batch):
    toks = tokenizer(batch["text"], truncation=True, padding="max_length", max_length=256)
    toks["labels"] = batch["labels"]
    return toks

ds = ds.map(preprocess, batched=True, remove_columns=["text"])
ds.set_format(type="torch", columns=["input_ids","attention_mask","labels"])

# Load model and set problem_type/regression size
model = AutoModelForSequenceClassification.from_pretrained(
    model_name,
    num_labels=4,
    problem_type="regression"  # tells HF to use MSELoss
)

# If you want outputs naturally bounded to (-1,1):
# Option A (simpler): keep linear outputs and clip at inference
# Option B: modify final layer to include tanh (example below)
# Example: add tanh wrapper (optional)
class TanhRegressionModel(torch.nn.Module):
    def __init__(self, base_model):
        super().__init__()
        self.base = base_model
    def forward(self, **kwargs):
        out = self.base(**kwargs)
        # logits shape: (batch, 4)
        logits = out.logits
        return torch.nn.utils.stateless.functional_call(self.base, {}, labels=None) if False else out

# --- metrics ---
mse = evaluate.load("mse")
pearson = evaluate.load("pearsonr")

def compute_metrics(eval_pred):
    preds, labels = eval_pred
    # preds shape (N,4)
    preds = np.array(preds)
    labels = np.array(labels)
    # overall RMSE per factor
    mses = np.mean((preds - labels)**2, axis=0)
    rmses = np.sqrt(mses)
    # pearson per factor
    pears = []
    for i in range(labels.shape[1]):
        try:
            r = pearson.compute(predictions=preds[:,i], references=labels[:,i])['pearsonr']
        except Exception:
            r = 0.0
        pears.append(r)
    # return keys
    out = {f"rmse_{i}": rmses[i] for i in range(labels.shape[1])}
    out.update({f"pearson_{i}": pears[i] for i in range(labels.shape[1])})
    out["rmse_mean"] = float(np.mean(rmses))
    return out

# --- Training ---
training_args = TrainingArguments(
    output_dir="finetune-fearfactor",
    per_device_train_batch_size=8,
    per_device_eval_batch_size=16,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    num_train_epochs=3,
    fp16=torch.cuda.is_available(),  # if GPU + mixed precision
    logging_steps=50,
    learning_rate=2e-5,
    weight_decay=0.01
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=ds["train"],
    eval_dataset=ds["test"],
    compute_metrics=compute_metrics
)

trainer.train()
