# Tasks 1 & 2: Word Cleaner and Frequency Counter

## Description

This script performs basic text preprocessing and word frequency analysis. It follows these steps:

1. **Text Cleaning**
   - Converts the entire input text to lowercase.
   - Removes common stopwords:  
     `["the", "and", "in", "is", "to", "of"]`
   - Splits the cleaned text into individual words.

2. **Frequency Counting**
   - Counts how often each remaining word appears in the text.

---

# Task 3: Simple Sentiment Estimator

## Description

This script estimates the **sentiment** of a given text as one of the following:
- **Positive**
- **Negative**
- **Neutral**

### Steps:
1. Converts the text to lowercase.
2. Splits the text into individual words.
3. Counts the number of positive and negative words.
4. Compares the counts:
   - If **positive > negative** → returns **positive**
   - If **negative > positive** → returns **negative**
   - Otherwise → returns **neutral**

### Word Lists
- **Positive words**: `["good", "happy", "excellent"]`  
- **Negative words**: `["bad", "sad", "terrible"]`

---

# How to Run the Script

## Prerequisites
- Python 3 must be installed on your system.
- No external libraries are required.

## Steps to Execute
1. Open your terminal or command prompt.
2. Navigate to the folder containing the script.
3. Run the script using the following command:
   ```bash
   python wordCleaner&wordFrequencyCounter.py
   python sentimentEstimator.py
