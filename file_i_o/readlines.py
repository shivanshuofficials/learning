f = open("readlines.txt")
lines1 = f.readline()
print(lines1,type(lines1))
lines2 = f.readline()
print(lines2,type(lines2))
lines3 = f.readline()
print(lines3,type(lines3))


# line = f.readline()
# while (line != ""):
#     print(line)
#     line = f.readline()
f.close()