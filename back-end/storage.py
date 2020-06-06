import pymysql.cursors


class Storage(object):
    def __init__(self, mysql_uri, username, password, database_name, port=3306):
        self.mysql_uri = mysql_uri
        self.username = username
        self.password = password
        self.port = port
        self.database_name = database_name
        self.connection = pymysql.connect(host=self.mysql_uri,
                                          user=self.username,
                                          password=self.password,
                                          db=self.database_name,
                                          cursorclass=pymysql.cursors.DictCursor)

    def find_one_with_query(self, query):
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            return result

    def get_by_id(self):
        pass

    def save(self):
        pass

    def test(self):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `steam_user` LIMIT 1"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result
