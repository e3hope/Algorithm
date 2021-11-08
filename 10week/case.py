def case(words):
    answer = []
    for w in words:
        answer.append(w.lower() if w.isupper() else w.upper())
    return ''.join(answer)

words = list(input())
print(case(words))