#Difference sets without loops
s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}   

#solution 1
print(s1 - s2)
#soltion 2
print(s1.difference(s2))

#With loops

s3 = set()
for n in s1:
    if n not in s2:
        s3.add(n)
print(s3)

#You should get {1, 2, 3} three times