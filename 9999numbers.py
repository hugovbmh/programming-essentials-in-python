import random 

i=0

kind = [17,16,18,19,26,27]

destFile = r"D:\hugov\Escritorio\num\num.txt"
while (i<10000):
    with open(destFile, 'a') as f:
        print("{}\n".format(random.choice(kind)), file=f)
        i=i+1
    
    #print(random.choice(kind))