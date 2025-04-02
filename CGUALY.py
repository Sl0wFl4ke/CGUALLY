'''
DISCLAIMER : Concieved by sl0w encouraged by Constant Lebreton, Arnaud Guarrigues, Kevin Rosaz
Notabene : hope my folks still alive.
<3 ALL


Should be unhackable except by python ways.
Use clear operation like i = 1+1
or s = "1"+"2"
or else.

anyway it won't compile

OPENSOURCE Licence
'''

import re 

##### CGUALLY #####
def CONCATSTR(A, B):
    try:
        str(A)+str(B)
        return True
    except:
        exit("Wrong type or missuse of type Str Concatenate")

def EVALINT(I):
    if int(I):
        pass
    else:
        exit("Wrong Int i : "+I)   
def EVALINTNOTZERO(I):
    if int(I):
        pass
    else:
        exit("Division by zero : "+I)
def MATHP(A, B):
    EVALINT(A);EVALINT(B)
    return True

def MATHS(A, B):
    EVALINT(A);EVALINT(B)
    return True

def MATHM(A, B):
    EVALINT(A);EVALINT(B)
    return True

def MATHD(A, B):
    EVALINT(A);EVALINT(B);EVALINTNOTZERO(B)
    return True
def MATHMod(A,B):
    EVALINT(A);EVALINT(B)
    return True


def EVALFLOA(I):
    try:
        float(I)
        return True
    except:
        exit("Wrong type float f : "+I)     
def EVALFLOATNOTZERO(I):
    if float(I) and I != 0.0:
        pass
    else:
        exit("Division by zero : "+I)
def MATHFP(A, B): # +
    EVALFLOA(A);EVALFLOA(B)
    return True
def MATHFS(A, B): # -
    EVALFLOA(A);EVALFLOA(B)
    return True
def MATHFM(A, B): # *
    EVALFLOA(A);EVALFLOA(B)
    return True
def MATHFD(A, B): # /
    EVALFLOA(A);EVALFLOA(B);EVALFLOATNOTZERO(B)
    return True
def MATHFMod(A,B): # %
    EVALFLOA(A);EVALFLOA(B)
    return True

def Compile(fileStr, code):
    f = open(fileStr, "r")
    text = f.read()
    for instruction in text.split("\n"):
        ## INT Check
        regint = r"(-{0,1}[0-9]+) ([+\-*/%]{1,1}) (-{0,1}[0-9]+)"
        print("Evaluating : "+ instruction)
        if re.match(regint, instruction):
            match = re.search(regint, instruction)
            match match.groupe(1):
                case "+":
                    MATHP(match.groupe(0),match.groupe(2))
                    break
                case "-":
                    MATHS(match.groupe(0),match.groupe(2))
                    break
                case "*":
                    MATHM(match.groupe(0),match.groupe(2))
                    break
                case "/":
                    MATHD(match.groupe(0),match.groupe(2))
                    break
                case "%":
                    MATHMod(match.groupe(0),match.groupe(2))
                case _:
                    exit("MathInt Op Not supported.")

        ## FLOAT Check
        regfloat = r"#-{0,1}[0-9]+\.[0-9]) ([+\-*/%]{1,1}) (-{0,1}[0-9]+\.[0-9]+)"
        if re.match(regint, instruction):
            match = re.search(regfloat, instruction)
            match match.groupe(1):
                case "+":
                    MATHFP(match.groupe(0),match.groupe(2))
                    break
                case "-":
                    MATHFS(match.groupe(0),match.groupe(2))
                    break
                case "*":
                    MATHFM(match.groupe(0),match.groupe(2))
                    break
                case "/":
                    MATHFD(match.groupe(0),match.groupe(2))
                    break
                case "%":
                    MATHFMod(match.groupe(0),match.groupe(2))
                case _:
                    exit("MathFloat Op Not supported.")
                

        ## STR Check
        regfloat = r"([\w\s]+) ([+]{1,1}) ([\w\s]+)"
        if re.match(regint, instruction):
            match = re.search(regfloat, instruction)
            if match.groupe(1):
                CONCATSTR(match.groupe(0),match.groupe(2))
            else:
                exit("Concat Failed : " + instruction)
        try:
            eval(instruction)
            code += instruction+"\n"
        except:
            exit("Wrong synthax in python.")
    return True
if __name__ == "__main__":
    import sys
    _args = sys.argv[1:]
    if(len(_args) != 1):
        exit("Pass a .py fullpath please.")
    code = ""
    if Compile(_args[0], code):
        import os
        os.system("nuitka --standalone "+ _args[0] + " --output-filename="+_args[0]+".x")
        exit("[SUCCESS] Compiled as foo.x")
    else:
        exit("[ERROR] Compile error.")
