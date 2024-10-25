INPUT= input("Enter only 0 & 1 four digits seperating comma")
numbers=INPUT.split(",")
dec=()
for i in numbers:
    for j in i:
       dec=dec+(j*pow(2,i))
  if dec%5==0:
print(i)
     
