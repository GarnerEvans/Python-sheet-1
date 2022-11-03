#!/usr/bin/env python
# coding: utf-8

# # Week 2 - Monday Lesson (variable assignment, loops, lists)

# ## Tasks Today:
# 
# 1) Int & Float assignments <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Assigning int <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Assigning float <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Performing Calculations on ints and floats <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Addition <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Subtraction <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Multiplication <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Division <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Floor Division <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Modulo <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Exponential <br>
# 2) String Input-Output <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) String Assignment <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) print() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) String Concatenation <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Type Conversion <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) input() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) format() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) Old Way (python 2) <br>
# 3) <b>In-Class Exercise #1</b> <br>
# 4) If Statements <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) 'is' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) 'in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) 'not in' keyword <br>
# 5) <b>In-Class Exercise #2</b> <br>
# 6) Elif Statements <br>
# 7) Else Statements <br>
# 8) <b>In-Class Exercise #3</b> <br>
# 9) For Loops <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Using 'in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Continue Statement <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Break Statement <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Pass Statement <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Double For Loops <br>
# 10) While Loops <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Looping 'While True' <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) While and For Loops Used Together <br>
# 11) Built-In Functions <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) range() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) len() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) help() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) isinstance() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) abs() <br>
# 12) Try and Except <br>
# 13) Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Declaring Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Indexing a List <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) .append() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) .insert() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) .pop() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) .remove() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) del() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; h) Concatenating Two Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; i) Lists Within Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; j) Looping Through Lists <br>

# ### Int & Float Assignments

# ##### Assigning int

# In[ ]:





# ##### Assinging float

# In[ ]:





# #### Performing Calculations on ints and floats

# ##### Addition

# In[2]:


num1 = 2
num2 = 5.4

result = num1 + num2

print(result + 2)


# ##### Subtraction

# In[4]:


result_diff = num2 - num1
print(result_diff)

result_diff -= 1
print(result_diff)


# ##### Multiplication

# In[6]:


result_mul = num1 * num2
print(result_mul)

result_mul *= 2
print(result_mul)


# ##### Division

# In[ ]:





# ##### Floor Division

# In[8]:


result_floor = num2 // num1
print(result_floor)


# ##### Modulo

# In[10]:


result_mod = num2 % num1
print(result_mod)


# ##### Exponential

# In[12]:


square = 5 ** 2
print(square)

square **= 2
print(square)


# ### String Input-Output

# ##### String Assignment

# In[16]:


name = "Brandon"
print(name)


# ##### print() <br>
# <p>Don't forget about end=' '</p>

# In[23]:


print("This is my first name: ",name)
print("Full Name: ",name, end=" Apol")


# ##### String Concatenation

# In[30]:


first_name = "John"
last_name = "Smith"
full_name = first_name + ' ' + last_name
print(full_name)
full_name += " Jr"
print(full_name)


# ##### Type Conversion

# In[32]:


number = '32'
change_type_num = int(number)
print(number)
print(change_type_num)


# ##### input()

# In[ ]:


#input will always return a string

name = input('what is your name?')
print("nice to meet you " + name)

age = int(input('what is your age?'))
add_age = int(age + 5)
print("in five years you will be ", add_age ," years old.")


# ##### format()

# In[ ]:


age = input('what is your age:')

# result_string = "You are {} {} and you are getting wiser".format(age.name)
# print(result_string)




# ##### Old Way (python 2)

# In[ ]:





# # In-Class Exercise 1 <br>
# <p>Create a format statement that asks for color, year, make, model and prints out the results</p>

# In[5]:


car_color = input('what is the color of your car?')
car_year = input('what is the year of your car?')
car_model = input('what is the model of your car?')

result_string = 'color: {} year: {} model: {}'.format(car_color,car_year,car_model)
print(result_string)


# ### If Statements

# In[21]:


# Available operators: Greater(>), Less(<),Equal(==)
# Greater or Equal(>=), Less or Equal (<=)

# Truth Tree:
# T && F = F
# T && T = T
# T || F = T
# F || T = T
# F || F = F

num1 = 5
num2 = 3
num3 = 0
# if num1 == num2:
#     print('equal values')
# else:
#     print('not equal')

if num2 > num1 or num3 > 0:
    print('num2 is greater')
elif num1 > num2:
    print('num1 is greater')
else:
    print('equal')


# ##### 'is' keyword

# In[22]:


num3 = 55
if num3 == 55:
    print('thats the number alright')


# ##### 'in' keyword

# In[24]:


#check if a character is in a string

character_name = 'Frodo Baggins'

if "Frodo" in character_name:
    print('The ring bearer')


# ##### 'not in' keyword'

# In[25]:


sega_character = 'sonic'

if 'a' not in sega_character:
    print('not in name')


# # In-Class Exercise 2 <br>
# <p>Ask user for input, check to see if the letter 'p' is in the input</p>

# In[27]:


response = input('What is your favorite animal?')

if 'p' in response:
    print('Animal contains the letter P')
else:
    print('No letter P')


# ## Using 'and'/'or' with If Statements

# In[7]:


num_11 = 15
num_12 = 3
num_13 = 10
num_14 =3 

if num_11/5 == num_12 and num_13 - 7 == num_14:
    print('true and true')
    
if num_11 > num_12 or num_13 == num_14:
    print('true and false')


# ### Elif Statements

# In[13]:


first_name = input('What is your name?')

if first_name == 'Smith':
    print('the name is smith')
elif first_name == 'Brandon':
    print('the name is Brandon')
elif first_name != 'Max':
    print('The name is not Max')
else:
    print('the name is max')


# ### Else Statements

# In[ ]:


# see above


# ### For Loops

# In[15]:


#for counter in condition
#for each thing in another thing do something
name = 'Brandon Apol'
a_list = [1,2,3,4]
for i in a_list:
    print(i)


# ##### Using 'in' keyword

# In[ ]:


# see above
#tells you what you are targeting


# ##### Continue Statement

# In[ ]:


# will continue to next iteration


# In[19]:


for i in range(20):
    if i == '4':
        continue
    print(i)


# ##### Break Statement

# In[ ]:


# will break out of current loop


# In[20]:


for i in range(20):
    if i == 5:
        break
    print(i)


# ##### Pass Statement

# In[ ]:


# mostly used as a placeholder, and will continue on same iteration


# In[ ]:


name = "brandon apol"
for i in name:
    pass


# ##### Double For Loops

# In[21]:


#can cause things to run slower

for i in range(5):
    for j in range(5):
        print('i = ', i, 'j = ', j)


# ### While Loops

# In[22]:


#will keep happening while something is true
#syntax: while keyword, condition statement

num = 0
while num < 10:
    print(num)
    num += 1


# ##### Looping 'While True'

# In[25]:


# bad practice

game_over = True

while game_over:
    print('Infinite loop')
    user_input = input('Would you like to stop?')
    if user_input == 'Yes':
        game_over = False


# ##### While & For Loops Used Together

# In[27]:


num = 0

while num < 5:
    print('\n While loop iteration:' + str(num))
    
    for i in range(2):
        print('For loop iteration: ', str(i))

    num += 1


# ### Built-In Functions

# ##### range()

# In[31]:


#range(Start, stop, step)

for i in range(0, 21, 2):
    print(i)


# ##### len()

# In[33]:


#checks length of variable

name = input('what is your name?')
length = len(name)
print(length)


# ##### help()

# In[34]:


#using this function to view more info about a python function

help(range)


# ##### isinstance()

# In[36]:


#check a variable to see what object family or data type it belongs to
#isinstance(var, type)

print(isinstance(4.5, int))

if isinstance(4.5,float):
    print(float)


# ##### abs()

# In[37]:


#same as absolute value in math... how far from 0.
# useful to return only positive's

print(abs(-5))


# ### Try and Except

# In[ ]:


#a way to do something other than throw an error when things go wrong
#does not stop the program

try: 
    input_num = int(input('give us a number'))
    if input_num != input_num + number_test:
        input_num = input_num + number_test
        print('your number is: ' + str(input_num))
        
except:
    print('that didnt work change pls')


# ### Lists
##### Declaring Lists
# In[38]:


list_1 = []

names = ['Max', 'Cindy', 'Kathy', 'Bob', 'Nate']
print(names)


# ##### Indexing a List

# In[49]:


#list_name[start: stop: step]

#Single Index
# print(names[4])
# print starting at a point and going to another using :
print(names[1:])

#print starting at the begining of a list up until a number
print(names[:2])

#print starting at index 1 and go up by two each iteration
print(names[1::2])

#print starting at the back and present in reverse order
print(names[::-1])


# ##### .append()

# ##### .insert()

# In[52]:


names.insert(3,'Devon')
print(names)


# In[ ]:





# ##### .pop()

# In[55]:


# defaults to the last value if no parameter (index) is given.
# It returns the element that was removed in case you want 
# # to assign it to a new variable.

my_name = names.pop(2)
print(my_name)
print(names)


# 
# ##### .remove()

# In[58]:


#will take the value rather than index number 
#syntax: remove(value) note that pop, insert, etc take an index instead

# names.remove('Bob')
# print(names)

while "brandon" in names:
    names.remove('brandon')
print(names)


# ##### del()

# In[59]:


#goes by index rather than value. Be carful to avoid indexing errors

del(names[1])
print(names)


# ##### Concatenating Two Lists

# In[63]:


#will append two lists together, will not add the values

list_2 = [0, 1, 2]
list_3 = [3, 4, 5]

large_list = list_2 + list_3
print(large_list)


# ##### Lists Within Lists

# In[ ]:


# lists can hold any type of other data type including other lists. 
# Can be nested endlessly.

names = ['Max', 'Sam', 'Josh', ['Sally', 'Sue', 'Tamika']]

print(names[3])
print(names[3][1])


# ##### Looping Through Lists

# In[68]:


# Two ways to loop through a list 1. index 2. 'in' keyword

# by index

for i in range(len(names)):
    print(names[i])
    
# loop with in
for i in names:
    print(i)


# ## Exercise #1 <br>
# <p>Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.</p>

# In[27]:


num_list = range(1,100,1)
    
for i in num_list:
    if i**3 < 1000:
        print(i**3)
        


# ## Exercise #2 <br>
# <p>Get first prime numbers up to 100</p>

# In[30]:


# HINT::
# An else after an if runs if the if didn’t
# An else after a for runs if the for didn’t break


prime_list = [3, 5, 7, 11]

for i in range(100):
    if i % 2 == 0:
        continue
    elif i % 3 == 0:
        continue
    elif i % 5 == 0:
        continue
    elif i % 7 == 0:
        continue
    elif i % 11 == 0:
        continue
    else:
        prime_list.append(i)
        
print(prime_list)

print(len(prime_list))


# # Exercise 3 <br>
# <p>Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors</p>

# In[6]:


user_age = int(input('How old are you?'))

if user_age < 18: 
    print('kids')
elif user_age > 18 and user_age < 65:
    print('adults')
else: 
    print('senior')
    


# In[ ]:




