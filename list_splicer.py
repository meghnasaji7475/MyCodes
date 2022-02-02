
#cropping == splicing
def list_splicer():

    list_1 = []
    list_2 = [] 
    cropped_list = [] # list variable to store the cropped lists from list_1
    final_list = [] # list variable to store all the cropped_list 
    i = 0 #loop variable

    n1=int(input("Number of elements in first list\n"))
    n2=int(input("Number of elements in second list\n"))
    print("\nStart entering elements of first list")

    while i<int(n1):
        list_1.append(int(input())) #adding elements to first list
        i=i+1

    i=0 #resetting loop variable
    print("\nStart entering elements of second list")

    while i<int(n2):
        list_2.append(int(input())) #adding elemetnts to second list
        i=i+1

    k=0 #kind of a place holder variable. essentinal for the following loop

    for elem in list_2: #this loop will crop list_1 to necessery "mini lists"
        cropped_list=list_1[k:(elem-1)] #elem-1 is used bcoz the intial postition value of list is '0' not '1'
        k=elem #this is necessery to create the "next" cropped_list 
        final_list.append(cropped_list) #adding the cropped_list to final_list

    cropped_list=list_1[elem:(n1)] #don't use 'n1-1' the last number wont be stored. don't know why that happens
    final_list.append(cropped_list) #adding the numbers right to "elem" that is remaining after cropping in list_1 to the  final_list

    print("\n",final_list,"\n") #output

list_splicer()