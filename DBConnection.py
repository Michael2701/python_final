from pymysql import *


class DBConnection:

    connection = None  # Database connection reference
    host = 'localhost'
    username = 'root'
    password = '4652581'
    # password = 'rootroot'
    db = 'python_final'
    table = 'passwords'

    @classmethod
    def connect(cls) -> None:
        """
        Function is responsible to set connection to a database
        :return: None
        """
        try:  # Try to connect and work with the specific database
            if cls.connection is None:
                cls.connection = connect(
                    host=cls.host,
                    user=cls.username,
                    database=cls.db,
                    password=cls.password,
                    cursorclass=cursors.DictCursor
                )
        except MySQLError:  # If there was a problem while connecting the database
            print("Couldn't connect the database")

    @classmethod
    def fetch_records(cls, query: str) -> object:
        """
        Function is responsible to count rows, according to the given query
        :param query: SQL query to execute
        :return: Rows that were effected by the query, None if there was a problem fetching results
        """
        records = []

        try:
            if cls.connection is None:
                cls.connect()

            if cls.connection is not None:
                with cls.connection.cursor() as cursor:
                    # Query to execute
                    cursor.execute(query)

                    records = cursor.fetchall()  # Getting all records
        except Exception as e:
            print("Oops!", e.__class__, "occurred.")
            print("In fetch_records function")
        finally:
            if cls.connection is not None:
                cls.connection.close()
                cls.connection = None
        return records

    @classmethod
    def insert(cls, query: str, params: tuple) -> bool:
        """
        Suits insert prepared query
        @param query: string - prepared query
        @param params:  - tuple with all needed params
            sorted in o same order like in query
        return: boolean
        """
        success = True

        try:
            if cls.connection is None:
                cls.connect()

            if cls.connection is not None:
                cls.connection.cursor().execute(query, params)
                cls.connection.commit()
        except MySQLError as e:
            success = False
            print(e)
        finally:
            cls.connection.close()
            cls.connection = None
            return success
