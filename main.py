print("Hello, World!")

# if- else-elseif
if 5 > 6:
  print("if true")
elif 4 < 5:
  print("else if true")
else:
  print("False")
 
# concact 
print('===============concact================')

x = "Uchi"
y = 22
print('age : ', y)

# casting
print('===============data type================')

x = str(3)
y = int(3)
z = float(3)

print('string : ', x, ', int : ', y, ' ,float : ', z)

# nested
print('===============nested================')

if 2 < 3:
    print("2")
    if 2 < 0:
        print("0")
    else:
        print("null")

# while loop
print('===============while================')

i = 1
while i < 6:
  print(i)
  i += 1

# array
print('===============array================')

fruits = ['orange', 'apple', 'mango']
print(fruits)
print(type(fruits))

# functions
print('===============function================')

def my_function():
  print("Hello from a function")
  
my_function()

# arguments and return
def multiplyNum(num1, num2):
    return (num1 * num2) + 1

print(multiplyNum(10, 20))

#Lists
print('===============Lists================')
List = ["apple", "cherry", "mango"]
print(List)
print(len(List)) #list length