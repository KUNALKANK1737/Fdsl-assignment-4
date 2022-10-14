
def selection_sort():
    marks=[]
    n=int(input("Enter the number of students to be taken in sorting :"))
    for i in range (n):
        r=float(input("Enter the marks to be inserted :"))
        marks.append(r)
    print(marks)
    
    for i in range (len(marks)):
       min_m=i
       for j in range (i+1,len(marks)):
          if(marks[min_m]>marks[j]):
            temp=marks[min_m]
            marks[min_m]=marks[j]
            marks[j]=temp
    print("The sorted list is :")
    print(marks)
    if(n>=5):
       a=marks[::-1]
       print("The top five members are :")
       i=0
       for i in range (5):
           print(a[i])
def bubble_sort():
    marks=[]
    n=int(input("Enter the number of students to be taken in sorting :"))
    for i in range (n):
        r=float(input("Enter the marks to be inserted :"))
        marks.append(r)
    print(marks)
    for i in range (n-1):
        
        for j in range (0,n-i-1):
            if(marks[j]>marks[j+1]):
                temp=marks[j]
                marks[j]=marks[j+1]
                marks[j+1]=temp
    print("The sorted list is :")
    print(marks)
    if(n>=5):
       a=marks[::-1]
       print("The top five members are :")
       i=0
       for i in range (5):
        print(a[i])
               
        
while(True):
    print("press 1:selection sort\npress 2:bubble sort")
    d=int(input("Enter your choice :"))
    if(d==1):
     selection_sort()
    if(d==2):
     bubble_sort()



