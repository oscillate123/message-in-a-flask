import mysql.connector
from mysql.connector import errorcode


class MysqlInstance():

	__instance   = None
	__host       = None
	__user       = None
	__password   = None
	__database   = None
	__session    = None
	__connection = None

	def __init__(self, host='0.0.0.0', user='root', password='', database=''):
		self.__host 	= host
		self.__user 	= user
		self.__password = password
		self.__database = database

	def __open(self):
		try:
			conn = mysql.connector.connect(host=self.__host, user=self.__user, password=self.__password, database=self.__database)
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Something is wrong with your user name or password")
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print("Database does not exist")
			else:
				print(err)
		else:
			self.__connection = conn
			self.__session    = conn.cursor()

	def __close(self):
		self.__session.close()
		self.__connection.close()

	def __query(self, query):
		result = None
		self.__open()
		self.__session.execute(query)
		number_rows = self.__session.rowcount
		number_columns = len(self.__session.description)

		if number_rows >= 1 and number_columns > 1:
			result = [item for item in self.__session.fetchall()]
		else:
			result = [item[0] for item in self.__session.fetchall()]
		self.__close()

		return result

	def select(self, *args, table):
		result = None
		query = 'SELECT '
		keys = args
		l = len(keys) - 1

		for i, key in enumerate(keys):
			query += "`"+key+"`"
			if i < l:
				query += ","

		self.__open()
		self.__session.execute(query, values)
		number_rows = self.__session.rowcount
		number_columns = len(self.__session.description)

		if number_rows >= 1 and number_columns > 1:
			result = [item for item in self.__session.fetchall()]
		else:
			result = [item[0] for item in self.__session.fetchall()]
		self.__close()

		return result

	def hostname(self):
		query = 'select @@hostname;'
		return self.__query(query=query)

	def host_ip_and_port(self):
		query = 'select host from information_schema.processlist;'
		return self.__query(query=query)

	def host_ip(self):
		query = "SELECT SUBSTRING_INDEX(USER(), '@', -1);"
		return self.__query(query=query)

	def user(self):
		query = "SELECT SUBSTRING_INDEX(USER(), '@', 1);"
		return self.__query(query=query)