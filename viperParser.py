#ViperParser.py

#This program parses the parsed viper files that were created with the shell scripting in order to extract
#only the frame number, x, y, width, and height for each human in the frame.

#import statements
import numpy as np

f = open('C:\\Users\\Joshua\\Desktop\\New Folder\\AerialTape3part1\\tape3_part1.txt','r')
g = open('C:\\Users\\Joshua\\Desktop\\New Folder\\AerialTape3part1\\tape3_part1_1.txt','w')
N = np.loadtxt(f, dtype=str, delimiter = ",")
for i in N:
    if(i[0]=="man"):
        tmpStr = i[2]+","+i[3]+","+i[4]+","+i[5]+","+i[6]+"\n"
        g.write(tmpStr)
f.close()
g.close()

f = open('C:\\Users\\Joshua\\Desktop\\New Folder\\AerialTape3part1\\tape3_part1_1.txt','r')
g = open('C:\\Users\\Joshua\\Desktop\\New Folder\\AerialTape3part1\\tape3_part1_2.txt','w')
N = np.loadtxt(f, dtype=str, delimiter = ",")
for i in N:
    l = i[0].split(":")
    k = int(l[1])-int(l[0])
    j = 0
    while j<=k:
        tmpStr = str(int(l[0])+j)+","+i[1]+","+i[2]+","+i[3]+","+i[4]+"\n"
        print(tmpStr)
        g.write(tmpStr)
        j=j+1
f.close()
g.close()

f = open('C:\\Users\\Joshua\\Desktop\\New Folder\\AerialTape3part1\\tape3_part1_2.txt','r')
g = open('C:\\Users\\Joshua\\Desktop\\New Folder\\AerialTape3part1\\tape3_part1_parsed.txt','w')
N = np.loadtxt(f, dtype=int, delimiter = ",")
print(N.shape[0])
l1 = []
i = 0
while i < N.shape[0]:
    j = 0
    while j < N.shape[0]:
        if i==N[j][0]:
            tmpStr = str(N[j][0])+','+str(N[j][1])+','+str(N[j][2])+','+str(N[j][3])+","+str(N[j][4])+'\n'
            g.write(tmpStr)
        j=j+1
    i=i+1
print(l1)
f.close()
g.close()
