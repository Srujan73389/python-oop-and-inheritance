# a=int(input("a:"))
# b=int(input("b:"))
# try:
#     print(a/b)
# except Exception as e:
#     print("barlilla:",e)
# else:
#     print("barlilla enu")
# finally:
#     print("baruto baralla gotilla")
try:
    num=int(input("Enter a num:"))
    res=10/num
    print("RESULT:",res)
except ZeroDivisionError:
    print(gIve a number greater than 0")
except ValueError:
    print("
