# Emotion Detection Project - README
Here I will explain how to use the code in [emotion_analyzer.py](./emotion_analyzer.py)

# Requirements
Make sure you are using python 3.10.11 (newer versions may also work)
In your project terminal run: `pip install torch transformers`

# File setup
Save the emotion_analyzer.py file into your projects root directory

# Running in terminal
In the directory that this file is saved in run 'python3 emotion_analyzer.py' and you will be prompted for text.
Type out your input text and hit enter and you will see the output values based on the given text.

# Importing and initialization
Import the EmotionAnalyzer class 
(The first time you initialize the class it will download the model weights)

```
from emotion_analyzer import EmotionAnalyzer

# Initialize the analyzer
# By default, it uses 'j-hartmann/emotion-english-distilroberta-base'
analyzer = EmotionAnalyzer()
```
# Example usage

```
text = "The sudden news of the layoffs spread quickly, leaving everyone feeling uncertain and anxious about the future."

results = analyzer.predict_levels(text)
print(results)
# Output Example: {'Fear Level': 2, 'Stress Level': 3, 'Morale Level': 1, 'Trust Level': 1}
```
