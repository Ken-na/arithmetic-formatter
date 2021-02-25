def arithmetic_arranger(problems, printAnswers = False):
    arranged_problems = "\n"
    seperatedTop = []
    seperatedSum = []
    seperatedBot = []
    longest = 0
    if len(problems) > 5:
        return 'Error: Too many problems.'

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

    top = ""
    bot = ""
    line = ""
    answer = ""
    pos = 0

    for s in problems:
        width = 0
        if len(seperatedTop[pos]) > len(seperatedBot[pos]):
            width = len(seperatedTop[pos])
        else:
            width = len(seperatedBot[pos])
        width += 2 #count for symbol
        if pos != 0:
            top += "    "
            bot += "    "
            line += "    "
            answer += "    "

        p = len(seperatedTop[pos])
        while p < width:
            top += " "
            p += 1
        top += seperatedTop[pos]

        bot += seperatedSum[pos]

        p = len(seperatedBot[pos]) + 1
        while p < width:
            bot += " "
            p += 1
        bot += seperatedBot[pos]

        p = 0
        while p < width:
            line += "-"
            p += 1

        if printAnswers:
            #print answers, should be conditional.
            val = -1
            if seperatedSum[pos] == "+":
                val = int(seperatedTop[pos]) + int(seperatedBot[pos])
            elif seperatedSum[pos] == "-":
                val = int(seperatedTop[pos]) - int(seperatedBot[pos])
            p = len(str(val))
            while p < width:
                answer += " "
                p += 1
            answer += str(val)

        pos += 1

    arranged_problems = top + "\n" + bot + "\n" + line
    if printAnswers:
        arranged_problems += "\n" + answer
    return arranged_problems
