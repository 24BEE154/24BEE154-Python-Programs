print("Name:Shubh Raval")
print("Roll No.: 24BEE154")
n = int(input("Enter a number:"))
a = 0
b = 1
print(a)
print(b)
for i in range(2, n):
        c = b
        b = b + a
        a = c
        print(b)
