str = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
res= ""
for w in str:
	if(w.isalpha()):
			res+= chr(((ord(w)-ord('A')+2))%26 + ord('A'))
	else:
		res+=w

print res