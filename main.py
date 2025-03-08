from database import setup_database

def main():
    setup_database() 

    print("=== Illegal Logging Reporting System ===")

    current_user = None  

    while not current_user:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role (user/admin): ").lower()
            Auth.register(username, password, role) # auth.py implementation
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            current_user = Auth.login(username, password) # auth.py implementation
        elif choice == "3":
            print("Goodbye!")
            return
        else:
            print("Invalid choice! Try again.")

    while True:
        print("\n1. File a Report\n2. View Reports")
        if isinstance(current_user, Admin):   # admin.py implementation
            print("3. Mark Report")
        print("4. Logout")

        choice = input("Select an option: ")

        if choice == "1":
            print(f"\n{current_user.get_username()}, please enter report details:")
            location = input("Enter location: ")
            description = input("Enter description: ")
            current_user.file_report(location, description)
        elif choice == "2":
            current_user.view_reports()
        elif choice == "3" and isinstance(current_user, Admin): # admin.py implementation
            report_id = input("Enter report ID: ")
            status = input("Enter new status (confirmed/dismissed/investigated/pending): ")
            current_user.mark_report(report_id, status)
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
