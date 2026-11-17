book = {}

with open("contacts.txt", "r", encoding="utf-8") as f:
    for line in f:
        name, phone = line.strip().split(": ")
        book[name] = phone


def ask_name():
    return input("姓名：")


def format_entry(name, phone):
    return f"{name}: {phone}"


while True:
    choice = input("1 添加 / 2 列出 / 3 查找 / 4 删除 / q 退出：")
    if choice == "q":
        break
    elif choice == "1":
        name = ask_name()
        phone = input("电话：")
        book[name] = phone
    elif choice == "2":
        if not book:
            print("通讯录是空的")
        else:
            for name, phone in book.items():
                print(format_entry(name, phone))
    elif choice == "3":
        name = ask_name()
        if name in book:
            print(format_entry(name, book[name]))
        else:
            print("没找到这个人")
    elif choice == "4":
        name = ask_name()
        if name in book:
            del book[name]
            print("已删除")
        else:
            print("没找到这个人")

    else:
        print("没有这个选项")
        
        
with open("contacts.txt", "w", encoding="utf-8") as file:
    for name, phone in book.items():
        file.write(format_entry(name, phone) + "\n")
        
        

print("再见")
