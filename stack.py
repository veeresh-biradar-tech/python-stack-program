# Performing Stack Operation In Python

stack= []

def push(stack : list, ele : int):
    stack.append(ele)
    print(f"Element {ele} Pushed In Stack Successfully")

def pop(stack : list):
    if not len(stack)== 0:
        return f"Element {stack.pop()} Popped  Successfully"
    return "Stack Is Empty"

def display(stack : list):
    if not len(stack)== 0:
        print("Elements In Stack:")
        for item in stack[ : : -1]:
              print(f"| {item} |")

    print("Stack Is Empty")
    

while True:
    print("Select The Operation You Want To Perform On Stack ")
    print("1 -- push")
    print("2 -- pop")
    print("3 -- display")
    print("4 -- exit")

    try:
        choice= int(input("Enter Your Choice :"))

        if choice== 1:
            try:
                element= int(input("Enter The Element Want To Push In Stack "))
                push(stack, element)
            except ValueError:
                print("Please Enter A Valid Integer")
        elif choice== 2:
            print(pop(stack))
        elif choice== 3:
            display(stack)
        elif choice== 4:
            exit()
        else:
            print("Invalid Choice")
    except ValueError:
        print("Please Enter A Valid Integer")