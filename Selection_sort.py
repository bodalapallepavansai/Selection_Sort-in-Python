#Selection Sort in Python

def prints(arr):
    print("Sorted List =",arr)

def Selection_sort(seq):
    for i in range(0,len(seq)):
        min=i
        for j in range(i+1,len(seq)):
            if seq[i]>seq[j]:
                min=j
        temp=seq[min]
        seq[min]=seq[i]
        seq[i]=temp
        print(seq)
    
    return prints(seq)

fhand=open(input("pl enter the name of the file:  "))
a=list()

for line in fhand:
    for i in line.split():
        a.append(i)
print("Entered List =",a)
Selection_sort(a)

