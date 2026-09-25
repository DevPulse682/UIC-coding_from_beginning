words = []

def build_sentence(*words, sep=" "):
    return sep.join(words)
    res = ''
    for word in words:
        res += word + sep
    return res

res = build_sentence("Hello", "world", "from", "Python")

print(res)  # Output: Hello world from Python
