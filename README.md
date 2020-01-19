# doodleblue_task

###  step-1
- getting data from user 

------------


### step-2
- checking whether user entered the needed data

------------
### step-3
- checking whether user entered name is in database already or not 
- if not goes for other conditions otherwise a condition break
------------
### step-4
- after checking name new coupon will be generated for the new user

------------
### step-5
- if new user entered any referal coupon will be checking it 
- if coupon is excit will be storing the referral and referee in separate table in db
- if coupon is invaild condition will break

------------

### step-6
- after all condition gets ok atlast new user will be registered in databse

------------

## database models 
- table-1 (details)
	1. name (to store the user name)
	1. age 
	1. city
	1. Id 
	1. coupon (New coupon for the new user or coupon for that user)
- table-2 (refernce)
	1. this table is used to save the referral and referee
	

------------


