text = """ g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. """
table = {}
for i in range(97, 123):
    table[i] = i + 2
table[121] = 97
table[122] = 98

print(text.translate(table))
#применям то, что было написано в расшифрованной инструкции
url = "map"
print(url.translate(table))
