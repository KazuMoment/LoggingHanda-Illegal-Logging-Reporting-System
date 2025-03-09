from report import Report

class User:
    def __init__(self, username: str):
        self.__username = username  
        self._role = "user"  
    
    def get_username(self):
        return self.__username 

    def file_report(self, location: str, description: str):
        report = Report(location, description)
        report.save_to_db()

    def view_reports(self):
        reports = Report.get_all_reports()
        print("\n=== Reports ===")
        for report in reports:
            print(f"ID: {report[0]} | Location: {report[1]} | Status: {report[2]}")
        print("================\n")

        report_id = input("Enter report ID to view details (or press Enter to return): ").strip()
        if report_id:
            details = Report.get_report_details(report_id)
            if details:
                print("\n=== Report Details ===")
                print(f"ID: {details[0]}")
                print(f"Location: {details[1]}")
                print(f"Description: {details[2]}")
                print(f"Status: {details[3]}")
                print("======================\n")
            else:
                print("Report not found!")
