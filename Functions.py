
# def greet():
#     print("Hello")
#     print("Hi")
#     print("Vanakkam!")

# greet()
# greet()


def printExpo(a,b):
    print(f'The answer is :{a**b}')

# printExpo(3,2)
# printExpo(4,1)

def printInfo(fName,lName,age):
    print(f"First Name: {fName}")
    print(f"Last Name: {lName}")
    print(f"Age: {age}")
    
# printInfo("Livin","kumar",98)

# printInfo(lName="kumar",age=78,fName="livin")

def greetUser(name="person"):
    print(f"Have a nice day {name}!")
    
# greetUser()
# greetUser("Livin")

def findSum(*nums):
    ans=0
    for i in nums:
        ans+=i
    print(f"Added Value: {ans}")

# findSum(3,324,34,312,3,234,45)

def sayHello():
    print("Hello!")
    print("Hello!")
    print("Hello!")
    print("Hello!")
    print("Hello!")
    return "Surprize"
    

# print(sayHello())

def expoAndDiv(a,b):
    return a*b  


# print(expoAndDiv(2,expoAndDiv(3,expoAndDiv(4,2))))



def sayVanakkam():
    a=20
    print("a's value from inside the function1 is: "+str(a))

def sayMorning():
    print("a's value from inside the function2 is: "+str(a))

  

sayVanakkam()
sayMorning()

# print("a's value from outside the function is: "+str(a))
    