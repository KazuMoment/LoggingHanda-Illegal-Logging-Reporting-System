

def main():
    # Start of Database Initialization Up Here

    print("=== Illegal Logging Reporting System ===")
    
    user = None 

    while not user:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Select an option: ")
        
        if choice == "1":
            User.register() # User class register
        elif choice == "2":
            user = User.login() # User class login
        elif choice == "3":
            print("Goodbye!")
            return
        else:
            print("Invalid choice! Try again.")

    while True:
        print("\n1. Submit a Report\n2. View Reports")
        if isinstance(user, Admin): # Check whether user is admin using boolean
            print("3. Update Report Status")
        print("4. Logout")
        
        choice = input("Select an option: ")

        if choice == "1":
            user.submit_report()
        elif choice == "2":
            user.view_reports()
        elif choice == "3" and isinstance(user, Admin): # Only be able to update report status if admin
            user.update_report_status()
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
