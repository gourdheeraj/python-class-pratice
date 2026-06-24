# print ("hello")
# print ("hello")
# print ("hello")

#tuples
#---------defination and property of tuple-----
#tuple is a data structure in python of tuple
#multiple data of different types with comma(,) in round braces.
#immutable
#support indexing slicing and  oredered.

#--creation of tuple

# t1=(50,60,70)
# print(type(t1))
# print(t1)

# t1,t2,t3=(50,60,"dheeraj")
# print(type(t3))
# print(t1)
# print(t2)
# print(t3)

# indexing and slicing.

# marks_tuple=(50,60,76,98,89)
# marks_tuple=[2]
# print(marks_tuple)

#traversing
# #! wap to ectract all number greater than 55,marks_tuple=(50,55,69,34,89)
# def tuple_fun(m):
#     new_value=[]
#     for i in m:
#         if i>=55:
#             new_value.append(i)
#     return new_value
# marks_tuple=(50,55,69,34,89)
# res=tuple_fun(marks_tuple)
# print(res) 

# # #! wap to sum of indices of tuple,marks_tuple=(50,55,69,34,89)
# marks_tuple=(50,55,69,34,89)
# sum_indx=0
# for i in range (len(marks_tuple)):
#     sum_indx+=i
# print(sum_indx)

# for i in range (1,20):
#     if i % 2 == 0:
#         print(i)
#q Create a tuple containing 5 different fruits and print it.
# fruits = ("mango","banana","apple","grapes")
# print(fruits)

#q2 Create a tuple with numbers (10, 20, 30, 40, 50) and print the first and last elements.

# tup = (10,20,30,40,50)
# print(tup[0])
# print(tup[-1])
#----------------------------------------------------------------------------------------------------------
# str1 = "this is python"

# vowels = "aeiouAEIOU"
# result = ""

# for i in range(len(str1)):
#     if str1[i] not in vowels:
#         result += str1[i]

# print(result)


# lst = [10, 20, 30, 40, 50]
# total = 0
# for i in lst:
#     total = total + i
#     total+=1
# print(total)

# def greet():
#     print("hello dheeraj")
# greet()

# def sum():
#     a=10
#     b=20
#     print(a+b)
# sum()


# def add(a,b):
#     print(a+b)

# add(10,80)
    
# def sum(a,b):
#     print(a+b)

# sum(20,50)
# sum(50,40)
# def square(n):
#     return(n**2)
# x=square(5)
# # print(x)

# def cube(n):
#     return(n**3)
# x = cube(3)
# print(x)

# def square(n):
#     return(n**2)
# # x = square(4)
# # print(x)

# def even_odd(i):
#     if i % 2 == 0:
#         return "even"
#     else:
#         return "odd"
# print(even_odd(1))
# print(even_odd(3))

# def largest(a,b,c):
#     if a>=b and a>=c:
#         return a
#     elif b>=a and b>=c:
#         return b
#     else:
#         return c
# l = largest(10,79,32)
# print("largest:",l)

# def m_len(s):
#     count = 0
#     for i in s:
#         count+=1
#     return count
# x=m_len("dheeraj")
# print(x)


# def sum_list(n):
#     total = 0
#     for i in n:
#         total = total + i
#     return total
# x = sum_list([10,20,30,40])
# print(x)

# def find_largest(lst):
#     largest = lst[0]

#     for i in lst:
#         if i > largest:
#             largest = i

#     return largest
# x = find_largest([10,34,54,67,87,45,3,4,56,76])
# print(x)

# def get_even(lst):
#     even_lst = []

#     for i in lst:
#         if i % 2 == 0:
#             even_lst.append(i)

#     return even_lst
# x= get_even([10,3,2,4,5,3,5,77,6])
# # print(x)


# def get_vowels(s):
#     vowels=0
#     for i in s:
#         if i in "aeiouAEIOU":
#             vowels+=1
#     return vowels
# x = get_vowels("python programming")
# print(x)

# def rev_lst(s):
#     reverse = ""
#     for i in s:
#         reverse = i + reverse
#     return reverse
# x = rev_lst("dheeraj")
# print(x)

# def is_palindrome(s):
#     reverse = ""

#     for i in s:
#         reverse = i + reverse

#     if s == reverse:
#         return True
#     else:
#         return False
    
# x = is_palindrome("nitin")
# print(x)
                  
# def even_count(s):
#     count=0
#     for i in s:
#         if i%2==0:
#             count+=1
#     return count
# x=even_count([1,4,5,67,8,5,6,67,7,3,4,3,4])
# print(x)

#-----------------------------------------------------------------------------------------

#Date=24-06-2026











