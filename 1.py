str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
res= ""
for w in str:
	if(w.isalpha()):
		if(w != 'z' and w != 'y' and w!='Z' and w!='Y'):
			res+= chr(ord(w)+2)
		else:
			res+= chr(ord(w)-24)
	else:
		res+=w

print res