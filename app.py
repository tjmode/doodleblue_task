from flask import Flask, render_template,request
import os
from new_coupon import newcoupon
from database import Db
app=Flask(__name__)
db = Db()
@app.route('/register',methods=['GET','POST'])
def register():
	'''
	this is to make a connection between flask and mysqlDB 
	'''
	if request.method=="POST":
		'''
		getting data from the user (its mean from html to flask to store in mysqlDB)
		'''	
		getdata=request.form
		name=getdata["name"]
		age=getdata["age"]
		city=getdata["city"]
		coupon=getdata["coupon"]
		'''
		this if condition to check weather user entered all the required fields || I can check this in frontend itself using required function in form
		'''
		if all([name,city,age]):
			if db.name_exists(name):
				return"Name is already taken"
				#i can also use alret method to display these errors
			else:
				'''
				if name not taken will be genrating the coupon for new user
				coupon genrator
			    i made auto increment ID so selection of last coupon will be use full to genrate next cupon for new user
				'''
				last_coupon=db.last_coupon_selecting()

				'''
				i used some simple tech to genrate different coupons to new users 
				
				'''
				genrated_coupon=newcoupon(name,last_coupon)
				'''
				last_cupon_split=str(last_coupon[0][0])
				intval=int(last_cupon_split[2::])
				intval=intval+1
				genrated_coupon=name[0:2]+str(intval)
				'''


			'''
			done with coupon genration
			this one to check weather user entered coupon is vaild or not
			'''
			if coupon!='':
				refered_user=db.when_coupon_not_null()
				if len(refered_user)!=0:
					try:
						db.refernce_table(coupon,name)
					except:
						return "invaild coupon"
				else:
					return"invaild coupon"
			'''
			registing the data into table if alll the condition is ok with it
			'''
			db.registering(name,age,city,genrated_coupon)
			'''
			after done with register i displaying thank you page to display the new coupon of the new  user
			'''
			return render_template("thankyou.html",name=name,genrated_coupon=genrated_coupon)

		else:
			#when user not enter the required field
			return "plz enter the required field"
	'''		
	to display the form 
	'''
	return render_template("register.html")
	'''
	I tested with some testcases its working good 
	if you found any bugs kindly report me i try to resolve it
	'''

if __name__ == '__main__':
	app.run(debug=True)