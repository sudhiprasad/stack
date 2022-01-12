stack = []

def isEmpty(stk):
    if(stk == []):
        return True
    else:
        return False

def Push(stk):
    std=input("Enter the Class :")
    phy="Phy:"+input("Number of students opted Physics :")
    math="Math:"+input("Number of students opted Math :")
    bio="Bio:"+input("Number of students opted Bio :")
    item={std:{phy,math,bio}}

    stk.append(item)

    return stk

def Delete(stk):
    index = int(input("Enter the index number of the record for Deleting :"))
    a = stk.pop(index)

    return a

def Display(stk):
    if(isEmpty(stk)):
        print("Stack is Empty !")
    else:
        print(stk)

while True:
    print("Menu :-")
    print('1) Insert into Stack')
    print('2) Delete Form Stack')
    print('3) Display the Stack')
    print('4) Exit')
    print()

    ch = int(input("Select Your Choice :"))

    if(ch==1):
        Push(stack)
        print('Successfully Added')
        input("Press any key to continue...")
    
    elif(ch==2):
        item = Delete(stack)
        print('deleted record from the Stack is :',item)
        input("Press any key to continue...")

    elif(ch==3):
        Display(stack)
        input("Press any key to continue...")

    elif(ch==4):
        break

    else:
        print("Please enter any choice between 1-4 from the menu",)
        input("Press any key to continue...")