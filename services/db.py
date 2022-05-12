import mysql.connector
import csv


class DBService:

    def __init__(self, user='user', password='test', host='127.0.0.1', database='test'):
        # initiate your class variables
        self.connection = None
        self.cursor = None
        self.user = user
        self.password = password
        self.host = host
        self.database = database

    def get_connection(self):
        # create db connection and cursor
        if not self.connection:
            try:
                self.connection = mysql.connector.connect(user=self.user, password=self.password,
                                                          host=self.host,
                                                          database=self.database)
                self.connection.autocommit = True
                self.cursor = self.connection.cursor(buffered=True)
                self.cursor.execute("""USE test;""")
            except mysql.connector.Error as err:
                print(f"Database error: {err}")
        return self.connection

    def close(self):
        # closing the connection
        if self.connection:
            self.connection.close()

    def commit(self):
        # commit the current transaction
        self.connection.commit()

    def insert_quote(self, author, quote):
        try:
            self.cursor.execute(
                f"""INSERT INTO famous_quotes (author, quote) VALUES(%s, %s); """,
                (author, quote)
            )
            return self.cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Error inserting quote: {err}")

    def get_quotes_by_author(self, author):
        try:
            self.cursor.execute(
                f"""SELECT quote FROM famous_quotes WHERE author=%s;""", (author,)
            )
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error retrieving {author} quotes: {err}")

    def get_quotes(self):
        try:
            self.cursor.execute(
                f"""SELECT author, quote FROM famous_quotes"""
            )
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error retrieving quotes: {err}")

    def load_data(self, file_path='data.csv'):
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for item in reader:
                if not any(item['quote'] in db_quote for db_quote in self.get_quotes_by_author(item['author'])):
                    self.insert_quote(item['author'], item['quote'])
                    assert any(item['quote'] in db_quote for db_quote in self.get_quotes_by_author(item['author']))


if __name__ == '__main__':
    db = DBService()
    db.get_connection()
    db.cursor.execute(
        """CREATE TABLE IF NOT EXISTS famous_quotes """
        """(id INT NOT NULL AUTO_INCREMENT, author VARCHAR(100) NOT NULL, quote VARCHAR(255), PRIMARY KEY (id));""")
    db.load_data()
    db.close()
