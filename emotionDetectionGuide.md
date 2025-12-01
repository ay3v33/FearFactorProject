# Emotion Detection Project - README

This README explains how to use the `emotionDetection.ipynb` notebook, which uses an existing emotion detection model to estimate values from 1 to 3 for fear, stress, morale and trust.

## What You Need Before You Start

* **Python 3.8+** installed on your computer
* **Jupyter Notebook** (comes with the Anaconda distribution or can be installed separately)
* Basic familiarity with running Jupyter 

If you’ve never used Jupyter before:

1. Open a terminal (or Anaconda Prompt).
2. Navigate to the folder where the notebook is located.
3. Run: `jupyter notebook`
4. A browser window will open—click on `emotionDetection.ipynb`.

---

## How to Run the Notebook

Here you can go through the notebook and run each cell in order.

### 1. **Importing Libraries**

This loads tools the notebook needs. Just run the cell—no changes necessary.

### 2. **Loading the Model and Tokenizer**

The notebook loads a pre‑trained emotion‑classification model. This may take a moment.

### 3. **Entering Text to Analyze**

This is done in python by storing the text from given json files
If you cloned the repository this should work automatically

### 4. **Running the Model**
First there is a function called avg_emotion_scores, which will calculate emotion values from 0 to 1 for different emotions, including fear.

Then after storing the results from the avg_emotion_scores function in a results variable, pass that variable into the emotions_to_fsmt function.

### 5. **Viewing the Output**
The output from the fsmt function should something like this

text_title {'Fear Level': 3, 'Stress Level': 3, 'Morale Level': 1, 'Trust Level': 1}
