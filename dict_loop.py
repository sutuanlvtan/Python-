scores = {"语文": 88, "数学": 95, "英语": 76}
for k in scores:
    print(k)
for k, v in scores.items():
    print(f"{k}: {v}")
print(scores.get("物理", 0))
print(scores.get("数学"))




