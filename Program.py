from DBConnection import DBConnection
from helpers import generate_random_numbers_string


class Program:

    @staticmethod
    def get_passwords() -> object:
        """
        Return all rows from passwords data base
        :return: object - rows
        """
        passwords = DBConnection.fetch_records("SELECT * FROM passwords")
        return passwords

    @staticmethod
    def save_password(password: str) -> bool:
        """
        Insert password to passwords data base
        :param password:
        :return: true if success otherwise false
        """
        query = "INSERT INTO passwords (password) VALUES(%s)"
        return DBConnection.insert(query, (password))

    @staticmethod
    def generate_password(path: str, number: int) -> str:
        """
        Build string of passwords.
        :param path:
        :param number:
        :return: string - password
        """
        password = ""
        for i in range(number):
            rand_line = generate_random_numbers_string()
            password += Program.find_string_by_number(rand_line, path)

        return password

    @staticmethod
    def make_password(path: str, number: int) -> bool:
        """
        Build password and save it to data base
        :param path:
        :param number:
        :return: true if success otherwise false
        """
        password = Program.generate_password(path, number)
        return Program.save_password(password)

    @staticmethod
    def find_string_by_number(number, path) -> str:
        """
        Search right string in file by given number
        :param number:
        :param path:
        :return: string with sub-password
        """
        with open(path, 'r') as f:
            line = f.readline()
            while line:
                line_list = (line.strip().split('\t'))
                if line_list[0] == number:
                    return line_list[1]
                line = f.readline()
