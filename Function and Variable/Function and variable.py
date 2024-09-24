name="Hello"
def my_name():
    global name
    name="Dhanes"
    print(name)
# print(name)
# my_name()
# print(name)
# project 2
y=lambda x : x * 10
times=lambda a, b, c : a*b*c
def x(x):
    return x * 9
# print(times(10,10,10))

def getFormula(num):
    return lambda x : x + num
myformula=getFormula(3)
# print(myformula(10))
def name1(*name):
    print(name)
# name1("Dhanes","Iori","Hello")
number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
list1=[]
list1=list(map(lambda num: (num % 3), number))
list2=list(filter(lambda num: (num % 3), number))
print(list2)
