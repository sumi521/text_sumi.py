"""
このファイルに解答コードを書いてください


"""
import re

list=[]

num = []
str_1=[]
box=[]
ind=[]
ans =[]
n=0

f = open('input.txt')
text = f.read()
f.close()

text = re.split('[\n:]',text)

for i in text:
    n+=1
    if n%2==1:
        num.append(i)
    else:
        str_1.append(i)

q = int(num[-1])

for i in num:
    y=int(i)
    if q%y==0:
        box.append(y)

box = sorted(box)

for m in box:
  ind.append(num.index(str(m)))
      
for m in ind:
    z = int(m)
    ans.append(str_1[m])

print(''.join(ans))