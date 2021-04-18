s = (input().strip())
s = s.lower()
for i in s:
    if (i < 'a' or i > 'z') and i != ' ':
        s = s.replace(i, "")
res = s.split(" ")

for i in range(len(res) - 1):
    temp = res[i]
    if(len(temp) > 0):
        print(temp[0].upper(), end = '')
print(".", end = '')

temp = res[len(res) - 1]
print(temp.capitalize())