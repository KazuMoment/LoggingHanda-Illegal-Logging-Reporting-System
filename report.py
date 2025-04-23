from database import get_db_connection

class Report:
    def __init__(self, location: str, description: str, status = "pending"):
        self.__location = location  
        self.__description = description 
        self._status = status 

    def save_to_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO reports (location, description, status) VALUES (?, ?, ?)", 
            (self.__location, self.__description, self._status)
        )
        conn.commit()
        conn.close()
        print("Report filed successfully!")

    @staticmethod
    def get_all_reports():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, location, status FROM reports")
        reports = cursor.fetchall()
        conn.close()
        return reports

    @staticmethod
    def get_report_details(report_id: int):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, location, description, status FROM reports WHERE id=?", (report_id,))
        report = cursor.fetchone()
        conn.close()
        return report

    @staticmethod
    def update_status(report_id: int, status: str, check_only=False):
        if not check_only and status not in ["confirmed", "dismissed", "investigating", "pending"]:
            print("Invalid status!")
            return False

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM reports WHERE id=?", (report_id,))
        report = cursor.fetchone()

        if not report:
            conn.close()
            return False

        if check_only:
            conn.close()
            return True

        cursor.execute("UPDATE reports SET status=? WHERE id=?", (status, report_id))
        conn.commit()
        conn.close()
        print(f"Report {report_id} marked as {status}.")
        return True



