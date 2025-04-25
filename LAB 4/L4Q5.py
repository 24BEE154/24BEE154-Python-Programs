print("Name:Shubh Raval")
print("Roll No.: 24BEE154")
import math as m
for a in range(1, 31):
    for b in range(a, 31): 
        for c in range(b, 31):
            if m.pow(m.pow(a, 2) + m.pow(b, 2),0.5) == c:
                print("Triplets:", a, b, c)




