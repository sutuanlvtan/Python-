scores = {"语文": 88, "数学": 95, "英语": 76, "物理": 92}
for k, v in scores.items():
    if v >= 90:
        print(k)
del scores["英语"]
print(scores)


