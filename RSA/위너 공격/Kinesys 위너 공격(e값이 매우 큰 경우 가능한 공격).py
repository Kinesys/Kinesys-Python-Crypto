import math

def DevContinuedFraction(num, denum) :
	partialQuotients = []
	divisionRests = []
	for i in range(int(math.log(denum, 2)/1)) :
		divisionRests = num % denum
		partialQuotients.append(num / denum)
		num = denum
		denum = divisionRests
		if denum == 0 :
			break
	return partialQuotients

""" (cf. useful link p.2) Theorem :
p_-2 = 0 p_-1 = 1   p_n = a_n.p_n-1 + p_n-2
q_-2 = 1 q_-1 = 0   q_n = a_n.q_n-1 + q_n-2 
"""
def DivergentsComputation(partialQuotients) :
	(p1, p2, q1, q2) = (1, 0, 0, 1)
	convergentsList = []
	for q in partialQuotients :
		pn = q * p1 + p2
		qn = q * q1 + q2
		convergentsList.append([pn, qn])
		p2 = p1
		q2 = q1
		p1 = pn
		q1 = qn
	return convergentsList    

"""  
https://dzone.com/articles/cryptographic-functions-python
Be careful to physical attacks see sections below
"""
def SquareAndMultiply(base,exponent,modulus):
	binaryExponent = []
	while exponent != 0:
		binaryExponent.append(exponent%2)
        	exponent = exponent/2
	result = 1
	binaryExponent.reverse()
	for i in binaryExponent:
		if i == 0:
			result = (result*result) % modulus
		else:
			result = (result*result*base) % modulus
	return result

def WienerAttack(e, N, C) :
	testStr = 42 
	C = SquareAndMultiply(testStr, e, N)
	for c in DivergentsComputation(DevContinuedFraction(e, N)) :
		if SquareAndMultiply(C, c[1], N) == testStr :
			FullReverse(N, e, c)
			return c[1]
	return -1

"""
Credit for int2Text : 
https://jhafranco.com/2012/01/29/rsa-implementation-in-python/
"""
def GetTheFlag(C, N, d) :
	p = pow(C, d, N)
	print p
	size = len("{:02x}".format(p)) // 2
	print "Flag = "+"".join([chr((p >> j) & 0xff) for j in reversed(range(0, size << 3, 8))])

"""
http://stackoverflow.com/questions/356090/how-to-compute-the-nth-root-of-a-very-big-integer
"""
def find_invpow(x,n):
	high = 1
	while high ** n < x:
		high *= 2
	low = high/2
	while low < high:
		mid = (low + high) // 2
		if low < mid and mid**n < x:
			low = mid
		elif high > mid and mid**n > x:
			high = mid
		else:
			return mid
	return mid + 1

"""
On reprend la demo on cherche (p, q), avec la recherche des racines du P
de scd degre : x^2 - (N - phi(N) + 1)x + N
"""
def FullReverse(N, e, c) :
	phi = (e*c[1]-1)//c[0]
	a = 1
	b = -(N-phi+1)
	c = N
	delta =b*b - 4*a*c
	if delta > 0 :
		x1 = (-b + find_invpow((b*b - 4*a*c), 2))/(2*a)
		x2 = (-b - find_invpow((b*b - 4*a*c), 2))/(2*a)
		if x1*x2 == N :
			print "p = "+str(x1)
			print "q = "+str(x2)
		else :
			print "** Error **"
	else :
		print "** ERROR : (p, q)**"

"""
Si N, e, C en hex ::> int("0x0123456789ABCDEF".strip("0x"), 16)
"""
if __name__ == "__main__":
	C = 60627434129028814567404969251697807879433775099089276036015410639261901886263220690479587955645647729237126627894599166136756811335873604339498869129719440656776867314172756225023754233476201217843405147707204606506489409981939998604644568471901388086489470619171927867919622384085722093956759241836499067639379179411120052281316958208007504576202137300342827418254852620085360302233358835951034932808393567658291851385064158525774666702382955852511233053362902277921857534414199997716231020668999139795251740005513044276574836799364555665560793535452231662835543599932725511766192196706414172508995359134072584232582 
	e = 30749686305802061816334591167284030734478031427751495527922388099381921172620569310945418007467306454160014597828390709770861577479329793948103408489494025272834473555854835044153374978554414416305012267643957838998648651100705446875979573675767605387333733876537528353237076626094553367977134079292593746416875606876735717905892280664538346000950343671655257046364067221469807138232820446015769882472160551840052921930357988334306659120253114790638496480092361951536576427295789429197483597859657977832368912534761100269065509351345050758943674651053419982561094432258103614830448382949765459939698951824447818497599
	N = 109966163992903243770643456296093759130737510333736483352345488643432614201030629970207047930115652268531222079508230987041869779760776072105738457123387124961036111210544028669181361694095594938869077306417325203381820822917059651429857093388618818437282624857927551285811542685269229705594166370426152128895901914709902037365652575730201897361139518816164746228733410283595236405985958414491372301878718635708605256444921222945267625853091126691358833453283744166617463257821375566155675868452032401961727814314481343467702299949407935602389342183536222842556906657001984320973035314726867840698884052182976760066141

	print "e : "+str(e)
	print "N : "+str(N)
	print "C : "+str(C)
	d = WienerAttack(e, N, C)
	if d != -1 :
		print "d = "+str(d)
		GetTheFlag(C, N, d)
	else :
		print "** ERROR : Wiener's attack Impossible**"
