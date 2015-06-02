str = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
res= ""
for w in str:
	if(w.isalpha()):
			res+= chr(((ord(w)-ord('a')+2))%26 + ord('a'))
	else:
		res+=w

print res

# original thought is to use ascii value for each character, plus 2 to it, then mod 26 to make sure y and z could turn into a and b