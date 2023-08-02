from OOP.EXAMS.Re_Take_April_2023.E_Drive_Rent.user import User


class UserFactory:
    @staticmethod
    def create_user(first_name, last_name, driving_license_number):
        return User(first_name, last_name, driving_license_number)
