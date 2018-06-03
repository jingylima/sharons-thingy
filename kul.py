equationa = "(2 + 2) * 6 + 3"
equationa = equationa.replace(' ','')
#print(equationa)
operators = "+"
operators1 = "*/"
operators2 = "+"

while "(" in equationa:
	start = equationa.find("(")
	end = equationa.find(")")
	equationb = (equationa[start:end+1])
	#print(1)
	#print(equationb)	

 # '''  if equationb[start + 1] in operators:
	#	for i in range(end)'''
	if operators in equationb:
		equationb.replace(" ","")
		#print(2)
	else:
		break
	while operators1 in equationb:

		if "*" in equationb:
			a = equationb.find("*")
			c = float(equationb[a - 1]) * float(equationb[a + 1])
			equationb[a-1] = str(c)
			equationb[a] = ""
			equationb[a + 1] = ""
		if "/" in equationb:
			a = equationb.find("/")
			c = float(equationb[a - 1]) / float(equationb[a + 1])
			equationb[a-1] = str(c)
			equationb[a] = ""
			equationb[a + 1] = ""

	while operators2 in equationb:

		if "-" in equationb:
			a = equationb.find("-")
			c = float(equationb[a - 1]) - float(equationb[a + 1])
			equationb[a-1] = str(c)
			equationb[a] = ""
			equationb[a + 1] = ""
		if "+" in equationb:
			a = equationb.find("+")
			c = int(equationb[a - 1]) + int(equationb[a + 1])
			equationb = equationb.replace(equationb, str(c))
	equationa = equationa.replace(equationa[start:end+1], equationb)
	answer = equationa
print(answer)
