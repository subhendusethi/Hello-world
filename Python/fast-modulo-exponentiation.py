# a^b (modulo c)
# https://discuss.codechef.com/questions/20451/a-tutorial-on-fast-modulo-multiplication-exponential-squaring
def exponent(a,b,c):
	result=1
	p=a
	while b>0:
		if(b%2 == 1):
			result=(result*p)%c
		p=(p*p)%c
		b=b/2
	return result
