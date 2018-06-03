equationa = "(2 + 2) * 6 + 3"
equationa.replace (" ", "")
operators = "+-*/"
operators1 = "*/"
operators2 = "-+"

while "(" in equationa:
    start = equationa.find("(")
    end = equationa.find(")")
    equationb = (equationa[start:end])

 # '''  if equationb[start + 1] in operators:
    #    for i in range(end)'''
    if operators in equationb:
        equationb.replace(" ","")
    while operators1 in equationb:

        if "*" in equationb:
            a = equationb.find("*")
            c = int(equationb[a - 1]) * int(equation[a + 1])
            equationb[a-1] = c
            equationb[a] = ""
            equationb[a + 1] = ""
        if "/" in equationb:
            a = equationb.find("/")
            c = equationb[a - 1] / equation[a + 1]
            equationb[a-1] = c
            equationb[a] = ""
            equationb[a + 1] = ""

    while operators2 in equationb:

        if "-" in equationb:
            a = equationb.find("-")
            c = equationb[a - 1] - equation[a + 1]
            equationb[a-1] = c
            equationb[a] = ""
            equationb[a + 1] = ""
        if "+" in equationb:
            a = equationb.find("+")
            c = equationb[a - 1] + equation[a + 1]
            equationb[a-1] = c
            equationb[a] = ""
            equationb[a + 1] = ""
    else:
        equationa.replace("equationa[start:end]", equationb)
        equationb.replace("(","")
        equationb.replace(")","")
        equationa.replace(" ","")
        equationa = int(equationa)
        answer = equationa
        print(answer)
