# print("Step1")
# print("Step2")
# print("Step3")

# print(6/0)
# if True:
# print(1)

# a=1+"Hi"
# print(b)

# a=1+"Hi" #flow should not be interrupted.

# try:
#     a=1+"Hi"
#     print(a)
# except TypeError:
#     print("You cannot add str to an int!")


try:
    num1=int(input("Enter a Number1: "))
    num2=int(input("Enter a Number2: "))
    print(f"The answer is: {num1/num2}")
except ValueError:
    print("Please enter a Valid Input!")
except ZeroDivisionError:
    print("Number cannot be divided by 0!")
finally:
    print("Finished....!")

