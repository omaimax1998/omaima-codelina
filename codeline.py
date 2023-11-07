menu_options = {
    1: 'Print Pattern',
    2: 'Rotate Array ',
    3: ' Help',
    4: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )
        
def option1():
    try:
        num = int(input("Enter a positive number: "))
        if num <= 0:
            print("Please enter a positive number.")
        else:
            for i in range(num, 0, -1):
                print("*" * i)
    except ValueError:
        print("Invalid input. Please enter a positive number.")

option1()


def option2(arr, k):
    n = len(arr)
    k = k % n  # Ensure k is within the range of the array length

    # Rotate the array
    rotated = arr[-k:] + arr[:-k]

    return rotated

# Input
n = int(input("Enter the number of elements (n): "))
k = int(input("Enter the number of steps (k): "))
arr = [int(x) for x in input("Enter the array of integers, separated by spaces: ").split()]

# Rotate the array
rotated_array = option2(arr, k)

# Display the rotated array
print("Rotated array:", rotated_array)
    
    
# except ValueError:
#     print("Invalid input. Please enter valid integers for n, k, and array elements.")

def option3():
     print(''' --Help-- 
           Option 1: Print a  pattern with 'n' rows of decreasing asterisks.
            Option 2: Rotate an array of  'n' elements of the right by  'k' steps.
            Option 3: Display this help message.
            Option 4: Exit the program.
        ''')
        
def option4():
    print('Exiting the program. Goodbye!')
    exit()  # This will terminate the program immediately

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
         option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')

