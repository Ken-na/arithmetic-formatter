def arithmetic_arranger(problems, printAnswers = False):
    arranged_problems = "\n"
    seperatedTop = []
    seperatedSum = []
    seperatedBot = []
    longest = 0
    for s in problems:
        seperated = s.split()
        seperatedTop.append(seperated[0])
        seperatedSum.append(seperated[1])
        seperatedBot.append(seperated[2])

        if len(seperated[0]) >> longest:
            longest = len(seperated[0])
        if len(seperated[2]) >> longest:
            longest = len(seperated[0])


        if "." in seperated[0] or "." in seperated[2]:
            return 'Error: Numbers must only contain digits.'
        if len(seperated[0]) > 4 or len(seperated[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if "+" not in seperated[1] and "-" not in seperated[1]:
            return 'Error: Operator must be \'+\' or \'-\'.'
        if seperated[0].isdigit() == False or seperated[2].isdigit() == False:
            return 'Error: Numbers must only contain digits.'
    longest += 4
    #for s in problems:
    if len(seperatedTop) > 4:
        return 'Error: Too many problems.'
    for r in seperatedTop:
        arranged_problems += '{:>11}  '.format(r)
        arranged_problems += "    "
    pos = 0
    arranged_problems += "\n"

    lineCount = []

    for r in seperatedBot:
        s = seperatedSum[pos]
        t = 0
        if len(seperatedTop[pos]) > len(seperatedBot[pos]):
            g = len(seperatedTop[pos])
            while t < abs(len(seperatedTop[pos]) - len(seperatedBot[pos])):
                s += " "
                t += 1
        else:
            g = len(seperatedBot[pos])
        s += " "
        s += seperatedBot[pos]
        arranged_problems += '{:>11}  '.format(s)
        pos += 1
        lineCount.append(g)
        arranged_problems += "    "
    arranged_problems += "\n"
        #arranged_problems = '{:>11}  {:>11}  {:>11}'.format(seperatedTop[0], seperatedTop[1], seperatedTop[2])

    for r in lineCount:
        s = ""
        g = 0
        while g < (r + 2):
            s += "-"
            g += 1
        arranged_problems += '{:>11}  '.format(s)
        arranged_problems += "    "
        pos = 0
    arranged_problems += "\n"
    if printAnswers:
        #print answers, should be conditional.
        for r in problems:
            val = -1
            if seperatedSum[pos] == "+":
                val = int(seperatedTop[pos]) + int(seperatedBot[pos])
            elif seperatedSum[pos] == "-":
                val = int(seperatedTop[pos]) - int(seperatedBot[pos])

            arranged_problems += '{:>11}  '.format(str(val))
            arranged_problems += "    "
            pos += 1

    return arranged_problems
