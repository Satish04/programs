"""This program is translate text into Swedish for "robber's language"). 
That is, double every consonant and place an occurrence of "o" in between.
For example, translate("this is fun") should return the string "tothohisos isos fofunon"."""

def trns(var):
	cons = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
	nvar = list(var)
	for s in nvar:
		if s == s in cons:
			nvar[nvar.index(s)] =  s + 'o' + s
	print  ''.join(nvar)

if __name__ == "__main__":
	st = str(raw_input("Enter any type of string: ")).lower()
	trns(st)