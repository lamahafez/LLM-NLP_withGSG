stop_word = ["the", "and", "in", "is", "to", "of"]

#Word Cleaner
def preprocess_text(txt):
    final_split_word = [];
    txt = txt.lower();
    split_word = txt.split(" ")
    for i in split_word:
        if i in stop_word:
            continue;
        final_split_word.append(i);
    return final_split_word
    
#Word Frequency Counter
def word_frequancy(cleaned_words):
    frequency_dectionary = {};
    for word in cleaned_words:
        if word in frequency_dectionary:
            frequency_dectionary[word] += 1;
        else:
            frequency_dectionary[word] = 1;
    return frequency_dectionary

example = "The quick brown fox jumps over the lazy dog in the park";

cleaned_words = preprocess_text(example)
print(f"Cleaned Words: {cleaned_words}")

frequencies = word_frequancy(cleaned_words);
print(f"Word Frequencies: {frequencies}")

#example with user input: 
text = (input('Enter Text: '))
cleaned_words = preprocess_text(text)
print(f"Cleaned Words: {cleaned_words}")
frequencies = word_frequancy(cleaned_words);
print(f"Word Frequencies: {frequencies}")


