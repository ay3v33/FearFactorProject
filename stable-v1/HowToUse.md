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

When you run the emotion analyzer it will ask you for text.
When you run the csv analyzer it will ask you for the name of the csv file, then for the column name of the text you want to analyze

```
Enter the path to your CSV file: data/MILDEC_short_out.csv
Loaded 1713 rows.
Columns: ['postId', '_type', 'requestForContentId', 'agentId', 'language', 'text', 'hashtags', 'image', 'tick', 'timestamp']
Enter the column name containing the text to analyze: text
Analyzing text and updating columns... (this may take a moment)
------------------------------
Success! Analyzed file saved as: data/MILDEC_short_out_analyzed.csv
   Fear Level  Stress Level  Morale Level  Trust Level
0           2             3             1            1
1           3             3             1            1
2           3             3             1            1
3           3             3             1            1
4           3             3             1            1
```
