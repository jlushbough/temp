import string
#data ="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
data ="map.html"
trans = string.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
print (data.translate(trans))

#for x in data:
#	if (ord(x) + 2 >= 97) and (ord(x) +2 <=122):
#		y = ord(x) + 2
#		print (chr(y),end="")
#	else:
#		print(x,end="")
