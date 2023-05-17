from random import randint
#1.
print('1.')
def min3(num1,num2,num3):
    if num1 < num2 and num1 < num3:
        smallest=num1     
    elif num2 < num1 and num2 < num3:
        smallest = num2   
    elif num3 <num1 and num3< num2:
       smallest = num3
    else:
        smallest = num1
    return smallest

print(min3(4, 7, 5))
print(min3(4, 5, 5))
print(min3(4, 4, 4))
print(min3(-2, -6, -100))
print(min3("Z", "B", "A"))
print()
#2
print('\n2.')
def box(x,y):
    for row in range(x):
        for column in range (y):
            print('*',end = '')
        print()
                  
box(7,5)  # Print a box 7 high, 5 across
print()   # Blank line
box(3,2)  # Print a box 3 high, 2 across
print()   # Blank line
box(3,10) # Print a box 3 high, 10 across  
print()

#3
print('\n3.')
def find(my_list,key):
    pos = 0
    for i in my_list:
        if key == i:
            print('found ', str(key), ' at position ', str( pos))
        pos += 1
        
my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]
    
find(my_list, 12)
find(my_list, 91)
find(my_list, 80)      

#4
print('\n4.')
def create_list(size):
    num_list = []
    for i in range(size):
        num_list.append(randint(1,6))
    return num_list

my_list = create_list(5)
print(my_list)

def count_list(x, y):
    n = 0
    for i in x:
        if y == i:
            n+=1
    return n
count = count_list([1,2,3,3,3,4,2,1],3)
print(count)

def average_list(x):
    add = 0
    divide = 0
    for i in x:
        add += i
        divide +=1
    return add//divide
    
avg = average_list([1,2,3])
print(avg)

#5

print('\n5.')

my_list = create_list(10000)

count = count_list(my_list,1)
print('1 appears ', str(count))
count = count_list(my_list,2)
print('2 appears ', str(count))
count = count_list(my_list,3)
print('3 appears ', str(count))
count = count_list(my_list,4)
print('4 appears ', str(count))
count = count_list(my_list,5)
print('5 appears ', str(count))
count = count_list(my_list,6)
print('6 appears ', str(count))

avg = average_list(my_list)
print(avg)

    

