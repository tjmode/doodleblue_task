def newcoupon(name,last_coupon):
	last_cupon_split=str(last_coupon[0][0])
	intval=int(last_cupon_split[2::])
	intval=intval+1
	genrated_coupon=name[0:2]+str(intval)
	return genrated_coupon