


is_male = True
is_tall = False

if is_male and is_tall:
    print("you are a tall male")
elif not(is_male) and is_tall:
    print("you are a tall girl")
elif is_male and(not(is_tall)):
    print("you are short man")
else :
    print("you are a short girl")

camel = ["tall","short","alex","alex","brown"]
print(camel)

def min_num(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <=num3:
        return num2
    else:
        return num3


print(min_num(200,201,202))

