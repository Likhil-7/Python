
'''
formula for compound interest
A = P(1 + R/100) t 
Compound Interest = A – P 
Where, 
A is amount 
P is principle amount 
R is the rate and 
T is the time span
'''
p=int(input("Enter a principal amount:"))
t=int(input("Enter  time:"))
r=float(input("Enter rate:"))

a=p*(1+r/100)**t
print("compound interest is ",a)