def gcd(b,c):
 if(c==0):
  return b
 return gcd(c,b%c)
 
def di(a,b,c):
 lcm=b*c/gcd(b,c)
 return a//lcm

a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))

print(di(a,b,c))





