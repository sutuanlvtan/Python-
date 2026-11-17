def total(price, count):
    return price * count


def show(name, price, count):
    print(f"{name} x{count} = {total(price, count)} 元")


show("篮球", 100, 2)
show("球鞋", 300, 1)
