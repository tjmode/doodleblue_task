from flask_mysqldb import MySQL
import MySQLdb

class Db:
	def __init__(self):
		self.connection = MySQLdb.connect(host="localhost", user = "root", passwd = "123456", db = "doodleblue")
		
	def name_exists(self, name):
		cursor = self.connection.cursor()
		cursor.execute("select name from eg1 where name=(%s)",[name])
		value = cursor.fetchall()
		#this if condition to check name already is taken or not
		if len(value) != 0:
			return True
		return False
	def last_coupon_selecting(self):
		cursor = self.connection.cursor()
		cursor.execute("select coupon from eg1 order by id desc limit 1")
		last_coupon=cursor.fetchall()
		return last_coupon
	def when_coupon_not_null(self):
		cursor = self.connection.cursor()
		cursor.execute("select coupon from eg1")
		refered_user=cursor.fetchall()
		return refered_user
	def registering(self,name,age,city,genrated_coupon):
		cursor = self.connection.cursor()
		cursor.execute("insert into eg1(name,age,city,coupon) values(%s,%s,%s,%s)",(name,age,city,genrated_coupon))
		self.connection.commit()
	def refernce_table(self,coupon,name):
		'''
		this condition is to insert the referal and refree in table seprate table
		here i can also use cur.execute("insert into refernce (referral)select name from eg1 where coupon=(%s))",[coupon]) this is subquery 
		'''
		cursor = self.connection.cursor()
		cursor.execute("select name from eg1 where coupon=(%s)",[coupon])
		referral=cursor.fetchall()
		'''
		i did normal method to insert here
		'''
		cursor.execute("insert into refernce(referral, referee) values(%s,%s)",[referral[0][0],name])
		self.connection.commit()