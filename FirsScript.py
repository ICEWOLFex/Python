number1 = float(input("Введите первое число: "))
c=number1
i=0
for i in range(5):
    znak = input("Введите знак действия: ")
    b = float(input("Введите второе число: "))
    if znak == "+":
        c=c+b
        print(c)
        i+=1
    elif znak == "-":
        c=c-b
        print(c) 
        i+=1
    elif znak == "*":
        c=c*b
        print(c)
        i+=1
    elif znak == "/":
        if b != 0:
            c=c/b
            print(c)
            i+=1
        else:
            print("Нельзя делить на ноль")
    elif znak == "^":
        c=c**b
        print(c)
        i+=1
    else:
        print("Error updating data")