def main():
    # Database initialization here

    print("=== Illegal Logging Reporting System ===")

    user = None

    while not user:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            register() # auth module implementation
        elif choice == "2":
            user = login() # auth module implementation
        elif choice == "3":
            print("Goodbye!")
            return
        else:
            print("Invalid choice! Try again.")

    while True:
        print("\n1. File a Report\n2. View Reports")
        if isinstance(user, Admin): # admin module implementation
            print("3. Mark Report")
        print("4. Logout")

        choice = input("Select an option: ")

        if choice == "1":
            location = input("Enter location of illegal logging: ")
            description = input("Enter description of the incident: ")
            user.file_report(location, description)

        elif choice == "2":
            user.view_reports()
            report_id = input("Enter report ID to view details (or press Enter to return): ").strip()
            if report_id:
                user.view_report_details(report_id)

        elif choice == "3" and isinstance(user, Admin):# admin module implementation
            report_id = input("Enter report ID to update: ")
            status = input("Enter new status (confirmed/dismissed/investigated): ").lower()
            user.mark_report(report_id, status)

        elif choice == "4":
            print("Logging out...")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
