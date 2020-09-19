def Hanoi(disk , src, dest, additional): 
    if disk==1: 
        print("Transfer disk 1 from source",src,"to destination",dest) 
        return
    Hanoi(disk-1, src, additional, dest) 
    print("Transfer disk",disk,"from source",src,"to destination",dest) 
    Hanoi(disk-1, additional, dest, src) 
          
disk = int(input("For how many rings you want to search.?"))
Hanoi(disk,'A','B','C')
