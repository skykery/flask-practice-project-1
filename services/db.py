
class DBService:

    def __init__(self, user, password, host, database):
        # initiate your class variables
        self.connection = None
        pass

    def get_connection(self):
        # self.connection = mysql.connector.connect(
        #     user='USER',
        #     password='PASSWORD',
        #     host='HOST',
        #     database='DATABASE'
        # )
        # return ?
        raise NotImplemented()

    def close(self):
        # closing the connection
        raise NotImplemented()

    def commit(self):
        # commit the current transaction
        raise NotImplemented()

    def insert_quote(self, author, quote):
        raise NotImplemented()

    def get_quotes_by_author(self, author):
        raise NotImplemented()

    def get_quotes(self):
        raise NotImplemented()


if __name__ == '__main__':
    pass
