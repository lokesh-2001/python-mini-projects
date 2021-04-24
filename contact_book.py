#----------------------------------CLASS STARTS----------------------------------------#
class Contact:

    #----------------------------------CONSTRUCTOR STARTS----------------------------------------#
    def __init__(self):
        self.book=[]
        self.name=[]
        self.num=[]
    #----------------------------------CONSTRUCTOR ENDS----------------------------------------#


    #----------------------------------CREATE A CONTACT FUNCTION STARTS----------------------------------------#
    def create(self, name, num, email):
        self.book.append([name,num,email])
        self.name.append(name)
        self.num.append(num)
        print("Contact saved successfully!!")
    #----------------------------------CREATE A CONTACT FUNCTION ENDS----------------------------------------#


    #----------------------------------UPDATE A CONTACT FUNCTION STARTS----------------------------------------#
    def update(self, name=False, num=False):
    #UPDATE USING NAME

        if name:
            if name in self.name:
                inames=[i for i,x in enumerate(self.name) if x==name]
                print('No of contacts found: ',len(inames),inames)
                c=1
                for f in inames:
                   print(c,"name: ",self.name[f]," details: ",self.book[f],"\n")
                   c+=1
                d="y"
                while d:
                    inp=input("Press y to continue or n to exit:  ").lower()
                    if inp=="y":
                        nm=int(input("Enter index of listed contact above: "))
                        try:
                            data=inames[nm-1]
                            print("\n\nDetails: ",self.book[data])  
                            print(1,"- Name: ",self.book[data][0])
                            print(2,"- Number: ",self.book[data][1])
                            print(3,"- Email: ",self.book[data][2])
                            print(0,'- Exit')

                            v="y"
                            while v:
                                ch=int(input("Enter index of listed contact above: "))
                                if ch==1:
                                    ch_name=input("Enter name to update: ")
                                    self.book[data][0]=ch_name
                                    self.name[data]=ch_name

                                elif ch==2:
                                    ch_num=input("Enter number to update: ")
                                    self.book[data][1]=ch_num
                                    self.num[data]=ch_num
                                elif ch==3:
                                    ch_mail=input("Enter emial to update: ")
                                    self.book[data][2]=ch_mail
                                elif ch==0:
                                    v=False
                                else:
                                    v=False
                            print("--------Updated Contact--------")
                            print(self.book[data])
                            print(self.name[data])
                            print(self.num[data])
                            print("-------------------------------")
                        
                        except:
                            print("Index not found!")
                    else:
                        break
            else:
                print("Contact not found!")
    #UPDATE USING NUMBERS

        elif num:
            if num in self.num:
                inum=[i for i,x in enumerate(self.num) if x==num]
                print('No of contacts found: ',len(inum),inum)
                c=1
                for f in inum:
                   print(c,"number: ",self.num[f]," details: ",self.book[f],"\n")
                   c+=1
                d="y"
                while d:
                    inp=input("Press y to continue or n to exit:  ").lower()
                    if inp=="y":
                        nm=int(input("Enter index of listed contact above: "))
                        try:
                            data=inum[nm-1]
                            print("\n\nDetails: ",self.book[data])  
                            print(1,"- Name: ",self.book[data][0])
                            print(2,"- Number: ",self.book[data][1])
                            print(3,"- Email: ",self.book[data][2])
                            print(0,'- Exit')

                            v="y"
                            while v:
                                ch=int(input("Enter index of listed contact above: "))
                                if ch==1:
                                    ch_name=input("Enter name to update: ")
                                    self.book[data][0]=ch_name
                                    self.name[data]=ch_name

                                elif ch==2:
                                    ch_num=input("Enter number to update: ")
                                    self.book[data][1]=ch_num
                                    self.num[data]=ch_num
                                elif ch==3:
                                    ch_mail=input("Enter emial to update: ")
                                    self.book[data][2]=ch_mail
                                elif ch==0:
                                    v=False
                                else:
                                    v=False
                            print("--------Updated Contact--------")
                            print(self.book[data])
                            print(self.name[data])
                            print(self.num[data])
                            print("-------------------------------")
                        
                        except:
                            print("Index not found!")
                    else:
                        break
            else:
                print("Contact not found!")

        else:
            print("Contact not found!")
    #----------------------------------UPDATE A CONTACT FUNCTION ENDS----------------------------------------#


    #----------------------------------DELETE A CONTACT FUNCTION STARTS----------------------------------------#  
    def delete(self,name=False,num=False):
    #UPDATE USING NAME

        if name:
            if name in self.name:
                d='y'
                while d:
                    iname=[i for i,x in enumerate(self.name) if x==name]
                    if(len(iname)>0):
                        print("Number of Contacts found: ",len(iname),iname)
                        c=1
                        for f in iname:
                            print(c,'name: ',self.name[f],' details: ',self.book[f],'\n')
                            c=c+1
                        inp=input("Press y to continue or n to exit: ").lower()
                        if inp=='y':
                            nm=int(input("Enter index of listed contact above: "))
                            try:
                                data=iname[nm-1]
                                print("\nDetails: ",self.book[data])
                                y=input("Are you sure you want to delete..? (y/n): ")

                                if y=="y":
                                    del self.book[data]
                                    del self.num[data]
                                    del self.name[data]

                                    print("--------Updated Contact Book--------")
                                    print("\nDetails: ",self.book)
                                    print("\nName Entries: ",self.name)
                                    print("\nNumber Entries: ",self.num)
                                    print("-------------------------------")

                            except:
                                print("\nIndex not found!!")
                        else:
                            break

                    else:
                        print("No contact found!!")
                        break

            else:
                print("Contact not found!!")
    #UPDATE USING NUMBERS

        elif num:                
            if num in self.num:
                d='y'
                while d:
                    inum=[i for i,x in enumerate(self.num) if x==num]
                    if(len(inum)>0):
                        print("Number of Contacts found: ",len(inum),inum)
                        c=1
                        for f in inum:
                            print(c,'name: ',self.name[f],' details: ',self.book[f],'\n')
                            c=c+1
                        inp=input("Press y to continue or n to exit: ").lower()
                        if inp=='y':
                            nm=int(input("Enter index of listed contact above: "))
                            try:
                                data=inum[nm-1]
                                print("\nDetails: ",self.book[data])
                                y=input("Are you sure you want to delete..? (y/n): ")

                                if y=="y":
                                    del self.book[data]
                                    del self.num[data]
                                    del self.name[data]

                                    print("--------Updated Contact Book--------")
                                    print("\nDetails: ",self.book)
                                    print("\nName Entries: ",self.name)
                                    print("\nNumber Entries: ",self.num)
                                    print("-------------------------------")

                            except:
                                print("\nIndex not found!!")
                        else:
                            break

                    else:
                        print("No contact found!!")
                        break

            else:
                print("Contact not found!!")
    #----------------------------------DELETE A CONTACT FUNCTION ENDS----------------------------------------#


    #----------------------------------PHONEBOOK DISPLAY STARTS----------------------------------------#
    def phonebook(self):
        print("\n\nTotal contacts found:  ",len(self.book))
        for i in self.book:
            print("\nName: ",i[0])
            print("Number: ",i[1])
            print("Email: ",i[2])
    #----------------------------------PHONEBOOK DISPLAY ENDS----------------------------------------#

    #----------------------------------SEARCH A CONTACT FUNCTION STARTS----------------------------------------#
    def search(self,name=False,num=False):
    #search using name
        if name:
            if name in self.name:
                iname=[i for i,x in enumerate(self.name) if x==name]
                c=1
                for d in iname:
                    print(c,'name: ',self.name[d],' details: ',self.book[d],'\n')
                    c+=1
            else:
                print("No contact found")
    #search using number
        elif num:
            if num in self.num:
                inum=[i for i,x in enumerate(self.num) if x==num]
                c=1
                for d in inum:
                    print(c,'name: ',self.name[d],' details: ',self.book[d],'\n')
                    c+=1
            else:
                print("No contact found")
        else:
            print("No contact found")
    #----------------------------------SEARCH A CONTACT FUNCTION ENDS----------------------------------------#
#----------------------------------CLASS ENDS----------------------------------------#


#----------------------------------VARIABLE DECLARATION----------------------------------------#
menu='''

    1. Create
    2. Update
    3. List Contacts
    4. Search
    5. Delete
    6. Exit

'''


#----------------------------------MAIN FUNCTION STARTS----------------------------------------#
if __name__=="__main__":
#inside main
    c=Contact()

    a=True
    while a:
        print("\n", menu , "\n")
        choice=int(input("Enter your choice: "))
    # create the contact
        if choice == 1:
            name=input("Name: ")
            num=input("Phone Number: ")
            mail=input("E-mail Address: ")
            c.create(name,num,mail)
    # update the contact
        elif choice == 2:
            k=True
            while k:
                print(
                    '''
                    1. Update through name
                    2. Update through number
                    3. Exit
                    '''
                )
                inp=int(input("Enter your choice: "))
                if inp==1:
                    name=input("enter name: ")
                    c.update(name=name)
                elif inp==2:
                    num=input("enter number: ")
                    c.update(num=num)
                else:
                    k=False
    # list the contact        
        elif choice == 3:
            c.phonebook()
    # search the contact
        elif choice == 4:
            k=True
            while k:
                print(
                    '''
                    1. Search through name
                    2. Search through number
                    3. Exit
                    '''
                )
                inp=int(input("Enter your choice: "))
                if inp==1:
                    name=input("enter name: ")
                    c.search(name=name)
                elif inp==2:
                    num=input("enter number: ")
                    c.search(num=num)
                else:
                    k=False
    # delete the contact
        elif choice == 5:
            k=True
            while k:
                print(
                    '''
                    1. Delete through name
                    2. Delete through number
                    3. Exit
                    '''
                )
                inp=int(input("Enter your choice: "))
                if inp==1:
                    name=input("enter name: ")
                    c.delete(name=name)
                elif inp==2:
                    num=input("enter number: ")
                    c.delete(num=num)
                else:
                    k=False
    # exit 
        elif choice == 6:
            a=False
    #  exit
        else:
            break
#----------------------------------MAIN FUNCTION ENDS----------------------------------------#