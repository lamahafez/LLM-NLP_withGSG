positive_word = ["good", "happy", "excellent"]
negative_word = ["bad", "sad", "terrible"]

#T3: Simple Sentiment Estimator
def word_sentiment_estimator(split_word):
    positive_count = 0
    negative_count = 0
    for word in split_word: 
        if word in positive_word:
            positive_count += 1
        elif word in negative_word:
            negative_count += 1
    
    #print(f"Pos{positive_count}, Neg{negative_count}")
    if positive_count > negative_count:
        return "positive"
    elif negative_count > positive_count:
        return"negative"
    else:
        return "neutral"
    
text = (input('Enter Text: '))
text = text.lower()
split_word = text.split(" ")
sentiment_estimator_message = word_sentiment_estimator(split_word)
#print sentiment_estimator_message:
print(f"the sentiment estimator is: {sentiment_estimator_message}")

