import csv
with open("1000-people-names.csv") as f:
  data=f.readlines()
  for i in data:
    print(i)
print(f)
f.close()
with open("1000-people-names.csv") as f:
  data=csv.reader(f)
  data_list=list(data)
total=0
for i in data_list:
  total += 1
print("Total people in data list is ",total-1)
people=[]

for i in data_list[1:]:
  # print("The job title of",i[2],i[3],"in the data is",i[8])
  # print("The person", i[2], i[3], "have the email of", i[5], "and a gender of", i[4])
  # print()
  people.append(int(i[8]))
print("Total people in data list is ",sum(people))
for i in data_list:
  print("Website from ",i[2], "organisation is ",i[3])