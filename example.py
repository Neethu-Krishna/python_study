words=["red","red","orange","blue"]
result=sorted(words,key=words.count,reverse=True)[0]
print(result)
result1 =sorted(set(words))
print(result1)
a=sorted(words,key=len)
print(a)
n1=sorted(words,key=words.count,reverse=True)
print(n1)

words3={"red":words.count("red"), 
        "orange":words.count("orange")}
print(words3)

number=[1,2,2,3,3,3,2,8]
# number.sort()
# print(number)
n=sorted(number)
print(n)

a="  python         program             desktop   "
a1=a.strip().lower()
print(a1)
a2=" ".join(a.split())
print(a2)
c=a.count(" ")
print(c)
a2=a.replace(" ","")
print(a2)