scores = {"语文": 88, "数学": 95, "英语": 76}
name = input("请输入要查询的科目名称：")
if name in scores:
    print(f"{name}: {scores[name]}")
else:
    print("没有这个科目")

    





