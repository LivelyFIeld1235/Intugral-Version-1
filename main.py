class Function:
    def __init__(self,func):
        self.funcName = func[0];
        self.function = func[1];
    def integrate(self):
        pass
    def differentiate(self):
        pass
    def __add__(self,otherFUNC):
        pass
    def __sub__(self, other):
        pass
    def __mul__(self,other):
        pass
    def display(self):
        pass
def listTerms(terms, func,withSign):
    if(not withSign):
        arithmeticIndices = []
        if ('-' in func or '+' in func):
            for i in range(len(func)):
                if (func[i] in ['-', '+']):
                    arithmeticIndices.append(i)
            for i in range(len(arithmeticIndices)):
                if (i == 0):
                    terms.append(func[0:arithmeticIndices[i]])
                    if (len(arithmeticIndices) != 1):
                        terms.append(func[arithmeticIndices[i] + 1:arithmeticIndices[i + 1]])
                elif (i != 0 and i + 1 != len(arithmeticIndices)):
                    terms.append(func[arithmeticIndices[i] + 1:arithmeticIndices[i + 1]])
                else:
                    terms.append(func[arithmeticIndices[i] + 1:]) if func[arithmeticIndices[i] + 1:] != '' else terms
        else:
            terms = [func];
    else:
        pass
def isValidFunc(func):
    validVariables = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    notValid = ['A' in func,'B' in func,'C' in func,'D' in func,'E' in func,'F' in func,'G' in func,'H' in func,'I' in func,'J' in func,'K' in func,'L' in func,'M' in func,'N' in func,'O' in func,'P' in func,'Q' in func,'R' in func,'S' in func,'T' in func,'U' in func,'V' in func,'W' in func,'X' in func,'Y' in func,'Z' in func]
    isValid = False;
    try:
        if(func.count("=") == 1 and not any(notValid)  and not any(['!' in func, '@' in func, '#' in func, '$' in func, '%' in func, '&' in func, '*' in func, '_' in func, ';' in func, '[' in func, ']' in func, '{' in func, '}' in func, '\\' in func, '|' in func])):
            if(func.split("=")[0] != ""):
                func = func.split("=")[1]
            else:
                return isValid;
            variableCounter = 0;
            varibaleIs = '';

            for i in validVariables:
                if(i in func):
                    varibaleIs = i;
                    variableCounter += 1;
            terms = [];
            if(variableCounter == 1):
                listTerms(terms,func, False)
                for i in terms:
                    try:
                        int(i)
                    except ValueError:
                        if i[i.find(varibaleIs) + 1] != "^":
                            isValid = False
                            return isValid
                        else:
                            termisVAR = i.replace("^","").split(varibaleIs)
                        try:
                            for i in termisVAR:
                                termisVAR[termisVAR.index(i)] = int(i)
                                isValid = True
                        except ValueError:
                            isValid = False
                return isValid
            else:
                if(not any(["+" in func,"-" in func])):
                    try:
                        int(func)
                        isValid = True;
                        return isValid
                    except ValueError:
                        return isValid;
                else:
                    listTerms(terms, func, False)
        else:
            isValid = False;
            return isValid;
    except UnboundLocalError:
        return isValid
if __name__ == "__main__":
    print("valid function examples: \n f(x) = 3x^2 + 4x^3 + 82 \n y = 9c^2 - 4c^3 + 82 \n var = 82z^3 - 87z^4 +832", end= "\n\n")
    func = input("Enter a single variable function ->");
    func = func.replace(" ", "");
    print("this is a valid function") if isValidFunc(func) else print("this is not a valid function")
    while(isValidFunc(func) == False):
        func = input("Please enter a valid function >")
        print("this is a valid function") if isValidFunc(func) else print("this is not a valid function")
        func = func.replace(" ", "")
    func = func.split("=")
    terms = []; listTerms(terms, func[1],False)
    print("terms are ", end= ': ')
    for i in terms:
        if(i != terms[-1]):
            print(i, end = ", ")
        else:
            print(i, end= "")

