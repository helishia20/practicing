count = 0
list = []

for i in range(100, 1000):
    string = str(i)
    a = int(string[0])
    b = int(string[1])
    c = int(string[2])
    if (a == 0) or (b == 0) or (c == 0):
        continue
    if (a == b != c) or (b == c != a) or (c == a != b):
        list.append(i)
        count += 1
print("LIST  IS :", list)
print("COUNTER : ", count)