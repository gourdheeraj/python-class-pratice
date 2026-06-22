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

# #! wap to sum of indices of tuple,marks_tuple=(50,55,69,34,89)
marks_tuple=(50,55,69,34,89)
sum_indx=0
for i in range (len(marks_tuple)):
    sum_indx+=i
print(sum_indx)