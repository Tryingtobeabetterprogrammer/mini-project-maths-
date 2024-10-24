a1=4
a2=5
a3=6
a4=7
a5=8
b1=10
b2=11
b3=12
b4=13
b5=14

a = [a1, a2, a3, a4, a5]
b=[b1,b2,b3,b4,b5]
lamda = [0,0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
delta_l= []
delta_u=[]
mu_l=[]
mu_u=[]
first_a = a[0]
last_a = a[-1]
for i in lamda:
    
    delta_l.append((i+first_a))  
    delta_u.append(last_a-i)

first_b=b[0]
last_b=b[-1]

for j in lamda:
    mu_l.append(j+first_b)
    mu_u.append(last_b-j)
print(delta_l)
print(delta_u)
print(mu_l)
print(mu_u)

r_l = []
for d, m in zip(delta_l, mu_l):
    r_l.append(d / m)
print(r_l)
r_u = []
for o, p in zip(delta_u, mu_u):
    r_u.append(o / p)
print(r_u)