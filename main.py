
f1=open("a.txt")
f2=open("b.txt","w")
for line in f1:
    f2.write(line)
f1.close()
f2.close()

