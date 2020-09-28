'''

gas = 45
while gas > 0:
    print("Vroom")
    gas = gas - 1
    if gas ==10:
     print("Fill Up!")
     continue

#For LOOP

ages = [18,21,16,12]
for age in ages:
        if age >= 18:
               print("come on in")
        elif age >=16:
               print("Not quite yet")
        else: print("Get ootta Here")

#Nested LOOPS

adj = ["red","big","tasty"]
fruits = ["apple","banana","cherry"]

for x in adj:
    for y in fruits:
        print(x,y)
'''

#Exercise

#num=1
#while x <= 100 :
    #print("")

num = int(input("Enter Number ranging from 1-100 : "))

while num % 3 == 0 :
    print("Fizz")
    num = num -1

    if num % 5 == 0 :
        print("Buzz")

    elif num % 3 /5 == 0:
        print("FizzBuzz")

    else:
        print("")

#example2
'''
x = 1
while x <=100:
    if x / 3 ==0:
        print("Fizz")
    if x / 5 ==0:
        print("Buzz")
    elif x / 5 ==0 and x /3 == 0:
        print("FizzBuzz")
    else:
        print("hi")

    #x = x + 1
'''