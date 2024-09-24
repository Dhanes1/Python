user_input=int(input("Pick a number: "))
for i in range(1,user_input+1):
  print(" "*(user_input-i)+"* "*i)