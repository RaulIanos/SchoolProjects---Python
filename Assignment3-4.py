import random

def ui_read_list(my_list):
#Menu functionality for reading a list
    n = int(input("Only numerical values accepted! \nHow many numbers do you want to input? "))
    read_list(my_list,n)

def read_list(my_list,n):
#Reads a list of complex numbers
#input: my_list - a list of complex numbers , n - an integer that describes how many items you want to add to the list
#output: adds n numbers to the current list
    for i in range(0,n):
        ui_add_to_list(my_list)

def command_printer(commands):
#prints all the existent commands
    print("The existent commands are:", end= " " )
    st=[]
    for x in commands:
        st.append(x)
    st.append("exit")
    print(st)

def ui_complex_generator(my_list):
#Menu functionality for generating n random numbers
    n = int(input("How many random number do you want to insert? "))
    complex_generator(my_list,n)
    print(str(n)+ " random numbers were added to the list! ")

def complex_generator(my_list,n):
#generates a number of n complex numbers and adds them to the end of the list
#input: my_list - a list of complex numbers , n - an integer that describes how many random numbers you want to add
#output:
    for i in range(n):
        a=random.randint(1,100)
        b=random.randint(1,100)
        z=complex(a,b)
        my_list.append(z)

def add_to_list(my_list, z):
#adds one element to the end of the list
#input: my_list - complex number list , z - complex number
    my_list.append(z)

def ui_add_to_list(my_list):
#Menu functionality for adding one number to the list
    print("Give your complex number: ")
    a=input("Real part: ")
    b = input("Imaginary part: ")
    while True:
        try:
            a=int(a)
            b=int(b)
            z=complex(a,b)
            add_to_list(my_list,z)
            return
        except ValueError as ve:
            print("Please input valid numerical values!")
            print("Give your complex number: ")
            a = input("Real part: ")
            b = input("Imaginary part: ")
            z = complex(a, b)
            add_to_list(my_list, z)

def list_printer(my_list):
# print the whole list
    print(my_list)

def ui_list_printer(my_list):
#Menu functionality for printing the whole list
    print("The elements of your list are: ", end = "")
    list_printer(my_list)

def elem_printer(n,my_list):
#prints one element from the list based on it's index
#input: n- index of the element  my_list- complex number list
#output: the wanted element
    print(my_list[n-1])

def ui_elem_printer(my_list):
# Menu functionality for printing an element
    print("Give the index of the element you want to print!")
    print("Indexes take values from 1 to " + str(len(my_list)))
    x=int(input())
    print("The wanted element is :", end = "")
    elem_printer(x,my_list)

def equal_sum(my_list):
# The function determines the longest sequence of number pairs that have equal sums
# input: the program must get a list of complex numbers
# output: the program wil return a list which contains the wanted sequence
    fsq = []
    for i in range(1,len(my_list)-1):
        sum = complex(0,0)
        sq = []
        sum = sum + my_list[i-1] + my_list[i]
        sq.append(my_list[i-1])
        sq.append(my_list[i])
        j = i + 2
        while j < len(my_list) and my_list[j]+my_list[j-1] == sum:
            sq.append(my_list[j-1])
            sq.append(my_list[j])
            j = j+2
        if len(sq) > len(fsq):
            fsq.clear()
            fsq = sq.copy()
    return  fsq

def ui_equal_sum(my_list):
#Menu functionality for printing the list that contains the longest sequence of number pairs that have equal sums
    lst = equal_sum(my_list)
    print("The longest sequence of consecutive number pairs that have equal sum is :", end = "")
    list_printer(lst)

def sum_10(my_list):

#The function determines the longest sequence of numbers that have the sum equal to 10+10i
#input: the program must get a list of complex numbers
#output: the program wil return a list which contains the wanted sequence
    aux = complex(10,10)
    fsq= []
    for i in range(len(my_list)):
        sq=[]
        j=i
        sum = complex(0,0);
        while j < len(my_list) and sum  != aux :
            sum = sum + my_list[j]
            sq.append(my_list[j])
            j = j+1

        if len(sq) > len(fsq) and sum == aux:
            fsq.clear()
            fsq = sq.copy()
    return fsq

def ui_sum_10(my_list):
#Menu functionality for printing the list that contains
#the longest sequence of numbers that have the sum equal to 10+10i
    sq = sum_10(my_list)
    print("The longest sequence of numbers that have the sum equal to 10+10i is :", end = "")
    list_printer(sq)

def ui_empty(my_list):
#Menu functionality for deleting all the values from the list
    my_list.clear()

def ui_help(my_list):
#Menu functionality for printing all the existent commands
    print("The 'add' command inserts one more element to the end of the list ")
    print("The 'print list' command prints the elements of the list ")
    print("The 'print element' command prints one wanted element defined by it's index ")
    print("The 'read list' command inserts n wanted elements to the list ")
    print("The 'generator' command adds n random elements to the list ")
    print("The 'equal sum' command finds the longest sequence of pairs with the same sum")
    print("The 'sum_10' command finds the longest sequence of numbers that have the sum equal to 10+10i")
    print("The 'empty' command deletes all the elements from my list ")
    print("The 'exit' command stops the program ")


def run(my_list):
#runs the program and lets the user to give multiple commands in order to make several operations on a list
    commands = {"add": ui_add_to_list,
                "print list": ui_list_printer,
                "print element":ui_elem_printer,
                "read list": ui_read_list,
                "generator": ui_complex_generator,
                "equal sum": ui_equal_sum,
                "sum_10": ui_sum_10,
                "empty": ui_empty,
                "help": ui_help,
                }
    command_printer(commands)
    while True:
        cmd = input()
        if cmd == "exit":
            break
        if cmd in commands:
            commands[cmd](my_list)
        else:
            print("Invalid command!")
            print("Please enter one of the following commands!")
            command_printer(commands)

if __name__ == "__main__":
    my_list = []
    run(my_list)