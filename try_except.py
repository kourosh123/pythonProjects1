try :
    number = 10/0
    value = int(input("write a number :"))
    print(value)
except ZeroDivisionError as err :
    print(err)
except ValueError :
    print("invalid input! Write a number please")

