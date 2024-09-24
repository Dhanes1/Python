num=1
list=[lambda km : km * 1000,lambda km : km * 0.62,lambda km : km * 3280.84]
list_name=['Km to m','Km to ml','Km to feet']
for i in list_name:
    print(str(num)+". "+i)
    num+=1
user_input=int(input("Please pick from the list: "))
km_h=lambda km,h : km * h
km_h=lambda km,h : km * h
function=None
if user_input==1:
    function=list[0]
elif user_input==2:
    function=list[1]
elif user_input == 3:
    function = list[2]
user_input=int(input("Please input Km: "))
print(function(user_input))
# for i in list:
#     print(i(10))
# print(km_h(10,1))