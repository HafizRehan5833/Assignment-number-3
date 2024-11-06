#. Use a loop to print numbers in reverse order within a given range.
start=int(input("Enter minimum number:"))
end=int(input("Enter maximum number:"))
a=end

#for i in range(end,start -1,-1):
 #   print(i)

while(a>=start):
    print(a)
    a-=1 