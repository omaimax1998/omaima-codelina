# Function to print the menu options
def print_menu():
    print("Menu Options:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Option 4")
    print("5. Quit")

# Main program
if __name__ == "__main__":
    while True:
        print_menu()
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            # Implement Option 1
            print("You selected Option 1.")
        
        elif choice == '2':
            # Implement Option 2
            print("You selected Option 2.")
        
        elif choice == '3':
            # Implement Option 3
            print("You selected Option 3.")
        
        elif choice == '4':
            # Implement Option 4
            print("You selected Option 4.")
        
        elif choice == '5':
            print("Goodbye!")
            break  # Exit the program
        
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4/5).")
