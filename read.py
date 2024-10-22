def read_file(): #Function is defined with name : 'read_file'
    file=open("products.txt","r") #open stock file (products.txt) in read mode. 
    lines=file.readlines() 
    L=[] # assign empty listwith name 'L'
    for line in lines:
        L.append(line.replace("\n","").split(","))
    file.close()
    print("Following options are available for parking")
    print("--------------------------------------------")
    print("WHEELS\t\tPRICE\t\tSLOTS")
    print("--------------------------------------------")
    for i in range(len(L)):
        print(L[i][0],"\t\t",L[i][1],"\t\t",L[i][2]) # prints the available Wheels, price and Slots available
    print("--------------------------------------------")
    return L
    
