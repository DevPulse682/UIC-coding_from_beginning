def word_count(sentence: str) -> int:
    if not sentence:
        return 0
    
    words: list = sentence.split()
    freq: dict =  dict()
    
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    
    return freq


print(word_count("Hello world from Python"))  