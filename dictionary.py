# Date=24-06-26

# ----------------- dictionary -------------------------
# Defination and property of dictionary.
# creation of dictionary.
# indexing and slicing. ❌
# Traversing
# In-built methods
# dictionary comprehension 
# Assignment and class Activity.


#--------Dictionary----------
#defination and property of dictionary
#1.dictionary is a data structure in python used store multiple data in
#key:value fprmat.
#2.oredred,mutable
#3.indexed by key,not position.
#4.key must be unique (immutable).
#5.value can be any type of data.
#6.used in fast lookup.

#-----ceration of dictionary------
# stu_profile={"dheeraj":"gwalior","rohit":"dehli"}
# print(type(stu_profile))
# print(stu_profile)

# stu_marks=dict([('amna',50),('rahul',70)])
# print(stu_marks)


#updates
# stu_profile={"dheeraj":"gwalior","rohit":"dehli"}
# stu_profile['rohit']='nodia'
# print(stu_profile)

#-------- inbuilt-method------

# stu_marks={"aman":300, 'shivam':80,'abhi':44}  #(items,values,keys)
# v=stu_marks.values()
# k=stu_marks.keys()
# i=stu_marks.items()
# r=stu_marks.get('soumya',"n/a")
# print(k)
# print(v)
# print(i)    
# print(r)

#-----updates-----

# stu_marks={"aman":300, 'shivam':80,'abhi':44}
# new_marks={'dev':70,'deeraj':90}
# stu_marks.update(new_marks)
# print(stu_marks)


# profile={
#     'aman':{
#         'address':["Noida","Delhi","mumbai"],
#         'hobbies':["reading","cooking","travelling"],
#         'password':{"insta":443534,"fb":87898},
#         },

#     'dev':{
#         'address':["Noida","Delhi","mumbai","varanasi"],
#         'hobbies':["reading","cooking","travelling"],
#         'password':{"insta":"000000","fb":"1097867"},
#         },

# }
# res=profile["dev"]["password"]["insta"]
# res=profile["aman"]["password"]["insta"]
#-----------------------------------------------------------------
# print(res)
# employee = {
#     "name": "Alice",
#     "salary": 50000,
#     "city": "Mumbai"
# }


# # v=employee.values()
# # print(v)
# for i in employee.values():
#     print(i)
#-------------------------------------------------------------
#Print all keys and values using a for loop.
# student = {
#     "name": "John",
#     "age": 21,
#     "course": "Python"
# }
# for key,value in student.items():
#     print(key,":",value)

#------------------------------------------------------------
#Add a new key "city" with value "gwalior".
# student={
#     "name":"john",
#     "age":21,
#     "course":"python"
# }
# student["city"]="gwalior"
# print(student)

#------------------------------------------------------------------------
# student={
#     "name":"dheeraj",
#     "age":23,
#     "course":"python"
# }
# student["age"]=27
# print(student)
#-------------------------------------------------------------------
#remove city in dictionary.
# student = {
#     "name": "John",
#     "age": 21,
#     "course": "Python",
#     "city": "Delhi"
# }
# student.pop("city")
# print(student)
# -----------------------------------------------------------------
# #for loop ka use karke sirf subjects print karo jinke marks 80 se zyada hain.
# marks = {
#     "Math": 85,
#     "Science": 90,
#     "English": 78,
#     "Computer": 95
# }
# for key,value in marks.items():
#     if value>80:
#         print(key)
#---------------------------------------------------------------------
#Dictionary ke sabhi marks ka total sum nikaalo.
# marks ={
#     "math":90,
#     "english":78,
#     "computer":95
#     }
# total=0
# for value in marks.values():
#     total+=value
# print(total)
#--------------------------------------------------------------------
#Check karo ki "course" key dictionary me present hai ya nahi.
# student = {
#     "name": "John",
#     "age": 21,
#     "course": "Python",
#     "city": "Delhi"
# }

# if "course" in student:
#     print("key found")
# else:
#     print("key not found")
#--------------------------------------------------------------
#  👉 for loop ka use karke sabhi subjects aur unke marks is format me print kar
# Math -> 85
# Science -> 90
# English -> 78
# Computer -> 95

# marks = {
#     "Math": 85,
#     "Science": 90,
#     "English": 78,
#     "Computer": 95
# }


# for key,value in marks.items():
#     print(key, "->",value)
#------------------------------------------------------------------
# #only print key.using for loop.
# student = {
#     "name": "Dheeraj",
#     "age": 23,
#     "city": "Gwalior"
# }
# for key in student:
#     print(key)
#--------------------------------------------------------------
#print only value using for loop.
# student = {
#     "name": "Dheeraj",
#     "age": 23,
#     "city": "Gwalior"
# }
# for value in student.values():

#     print(value)
#----------------------------------------------------------------
