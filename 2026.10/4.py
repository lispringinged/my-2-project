scores = {"alice": 90, "bob": 85, "carol": 78}
scores_a = sum(scores.values())
scores_b = scores_a / len(scores)
print(scores_b)
max_score = max(scores.values())
for k, v in scores.items():
    if v == max_score:
        print(k)


