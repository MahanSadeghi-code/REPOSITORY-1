while true :
    a = int(input("enter first number"))
    b = int(input("enter second number"))
    c = input("enter (+ , / , * , - , break)")

    if c == "+" :
        print(a + b)
    elif c == "-" :
        print(a - b)
    elif c == "/" :
        print (a / b)
    elif c == "*" :
        print ( a + b)
    elif c == "break" 
        break
    else :
        print ("eror the input was not + - / * or break")
