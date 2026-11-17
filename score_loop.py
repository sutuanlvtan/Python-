scores = {"语文": 88, "数学": 95, "英语": 76}
while True:
    name = input("科目（输入 q 退出）")
    if name == "q":
        break
    if name in scores:
        print(f"{name}: {scores[name]}")
    else:
        print("没有这个科目")
print("程序结束")







    
