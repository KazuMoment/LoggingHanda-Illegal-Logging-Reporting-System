from user import User
from report import Report

class Admin(User):
    def __init__(self, username: str):
        super().__init__(username)
        self._role = "admin" 

    def mark_report(self, report_id: int, status: str, check_only=False):
        return Report.update_status(report_id, status, check_only)


