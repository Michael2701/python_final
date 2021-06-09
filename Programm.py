from DBConnection import DBConnection
from helpers import generate_random_numbers_string


class Programm:

    @staticmethod
    def get_passwords():
        passwords = DBConnection.fetch_records("SELECT * FROM passwords")
        return passwords

    @staticmethod
    def save_password(password: str) -> bool:
        query = "INSERT INTO passwords (password) VALUES(%s)"
        return DBConnection.insert(query, (password))

    @staticmethod
    def generate_password(path: str, number: int) -> bool:
        password = ""
        for i in range(number):
            rand_line = generate_random_numbers_string()
            password += Programm.find_string_by_number(rand_line, path)

        return password

    @staticmethod
    def make_password(path: str, number: int) -> bool:
        password = Programm.generate_password(path, number)
        return Programm.save_password(password)

    @staticmethod
    def find_string_by_number(number, path) -> str:
        with open(path, 'r') as f:
            line = f.readline()
            while line:
                line_list = (line.strip().split('\t'))
                if line_list[0] == number:
                    return line_list[1]
                line = f.readline()
