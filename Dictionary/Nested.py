students={"students1":{"Name":"Monica","Class": 4,"Gender":"Female"},
          "students2":{"Name":"Dhanes","Class": 4,"Gender":"Male"},
          "students3":{"Name":"Dave","Class": 4,"Gender":"Male"},
          "students4":{"Name":"Buby","Class": 4,"Gender":"Male"},}
for i,j in students.items():
    print()
    print(i)
    for h,q in j.items():
        print(h,end=":")
        print(q)