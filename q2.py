from operator import itemgetter

stack = []

def isEmpty(stk):
    if(stk == []):
        return True
    else:
        return False


def isIndex(stk):
    if(stk==False):
        print("Index not found...!")
    else:
        return True


def AddEmployee(stk):
    e_name=input("Enter the Name of Emplpoyee :")
    e_salary=int(input("Enter the Salary :"))
    item={'name':e_name,'salary':e_salary}

    stk.append(item)

    return stk


def RemoveEmployee(stk):
    name = input("Enter the name for Deleting Employee :")
    for i in range(len(stk)):
        if stk[i]['name'] == name:
            del stk[i]
            break
    return name

        


def Display(stk):
    if(isEmpty(stk)):
        print("Stack is Empty !")
    else:
        val = sorted(stk, key=itemgetter('name'))
        print(val)
            


while True:
    print("Menu :-")
    print('1) Add a new Employee')
    print('2) Remove an Employee')
    print('3) Show the list of Employees in ascending order of their names')
    print('4) Exit')
    print()

    ch = int(input("Select Your Choice :"))

    if(ch==1):
        AddEmployee(stack)
        print()
        print('Successfully Added')
        print()
        input("Press any key to continue...")
    
    elif(ch==2):
        item = RemoveEmployee(stack)
        print()
        print('The record with the following Name has been Deleted :',item)
        print()
        input("Press any key to continue...")

    elif(ch==3):
        Display(stack)
        print()
        input("Press any key to continue...")

    elif(ch==4):
        break

    else:
        print("Please enter any choice between 1-4 from the menu",)
        input("Press any key to continue...")