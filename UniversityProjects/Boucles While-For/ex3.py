m=int(input("Donner un entier >= 10 :"))
while(m<10):
    m=int(input("Donner un entier >= 10 :"))
number=m
unite=m%10
m=m//10
m=m-2*unite
m=abs(m)
if(m==0 or m==7):
    print(number,"est divisible par 7")
else:
    print(number,"n'est pas divisible par 7")