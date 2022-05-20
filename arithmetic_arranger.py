import re
from operator import add, sub

def arithmetic_arranger(problems, answers=False):
    '''
    @param list problems - Ex: ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
    @param boolean[optional] answers - [False]
    '''
    arr = [[], [], [], []]

    if len(problems) > 5:
      return "Error: Too many problems."

    for problem in problems:
        m = re.split("([+-])", problem)

        # Checking input
        if len(m) != 3:
          return "Error: Operator must be '+' or '-'."

        a  = m[0].strip()
        op = m[1]
        b  = m[2].strip()

        if not (a.isdigit() and b.isdigit()):
          return "Error: Numbers must only contain digits."

        length = max(len(a), len(b))

        if length > 4:
          return "Error: Numbers cannot be more than four digits."

        # Formatting output
        arr[0].append(a.rjust(length+2, " "))
        arr[1].append(op + " " + b.rjust(length, " "))
        arr[2].append("-"*(length+2))

        if answers:
          plus = (sub, add)[op == "+"]
          arr[3].append(str(plus(int(a), int(b))).rjust(length+2, " "))

    # Concat all answers
    output  = "    ".join(arr[0]) + "\n"
    output += "    ".join(arr[1]) + "\n"
    output += "    ".join(arr[2])
    
    if answers:
      output +=  "\n" + "    ".join(arr[3])

    print(output)
    return output
