import json 
import matplotlib.pyplot as plt

f = open("20211203_062608.log.json", "r")
l = []
for cnt, line in enumerate(f.readlines()):
    d = line.split("\"")
    
    if len(d) > 13 and cnt % 2 == 1:
        x = d[12].split(":")[1].split(",")[0]
        if float(x) < 1:
            l.append(float(x))
print(l)

plt.title("mAP@0.5:0.95")
plt.plot(l)
plt.show()