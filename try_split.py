book = {}
with open("contacts.txt", "r", encoding="utf-8") as f:
    for line in f:
        name, phone = line.strip().split(": ")
        book[name] = phone
print(book)


