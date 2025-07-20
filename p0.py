print("Hello World")

name = "Yomama"
age = 66
height = 1.9
print(type(name))
print(type(age))
print (height)

a=10
b=2.2
print (a+b)
###


# List
fruits = ["apple", "banana", "cherry", 23]
print(fruits[1])
###

# Dictionary
students = {"name": "John", "age": 20, "grade": "A"}
print(students["name"])
###
temperature = 28
if temperature > 27:
  print("Too hot to go outside")
else:
    print("Decent to go outside")


    
###
    score = 75

if score >=90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
else:
  print("Grade: F")
  
  
####  
  # For loop
for i in range(5):
  print("value of i: ", i)
  
  
###  
  
  for i in range(10):
  if i == 5:
    print("i has value of 5")
    break
  print("Value of I is: ", i)
  
  
###
for i in range(10):
  if i == 5:
    print("Skip number 5")
    continue
  print("Value of I is: ", i)
  
  
  
   
###
 # while loop
count=0
while count <3:
  print("Print value: ", count)
  count +=1 #important daca nu o sa ai bucla infinita
  
  
###
for i in range(1,4):  # outert loop goes through 1 to 3
    for j in range(1,4):  # inner loop goes through 1 to 3
      print (i*j, end=' ')
    print()
    
    
### 
  for fruit in fruits:
  print("I like: ", fruit)
  
###
  def hello(name):
  return f"Hello, {name}"


###
hello2("Alex")
  
###
greet = hello2("Alex")
print(greet)


###
numbers =[3,4,9,2,7,0,79/3]
max_num = numbers[0]
for number in numbers:
  if number > max_num:
    max_num = number
print("The max nr is: ", max_num)


###