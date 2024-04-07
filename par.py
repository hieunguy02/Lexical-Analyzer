from lexical import lexer, file_name, fileoutput, tokens, lexemes
#Finish 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29

#R1 
def RATS24(current_i, switch):
    fileoutput.write("Lexemes:    Tokens:\n")
    if current_i is not None and lexemes[current_i] == "$":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Rat24S> ::= $ <Opt Function Definitions> $ <Opt Declaration List> $ <Statement List> $\n")
        current_i = OptFunctionDef(current_i, switch)

        if current_i is not None and lexemes[current_i] == "$":
            fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
            current_i += 1
            current_i = OptDeclarationList(current_i, switch)

            if current_i is not None and lexemes[current_i] == "$":
                fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
                current_i += 1
                current_i = StatementList(current_i, switch)

                if current_i is not None and lexemes[current_i] == "$":
                    fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
                    current_i += 1
                else:
                    fileoutput.write("Syntax Error, expected a $\n")
            else:
                fileoutput.write("Syntax Error, expected a $\n")
        else:
            fileoutput.write("Syntax Error, expected a $\n")
    return current_i

#R2
def OptFunctionDef(current_i, switch):
    if lexemes[current_i] == "function":
        if switch == "1":
            fileoutput.write("<Opt Function Definitions> ::= <Function Definitions>\n")
        current_i = FunctionDef(current_i, switch)
    else:
        if switch == "1":
            fileoutput.write("<Opt Function Definitions> ::= <Epsilon>\n")
        Empty()
    return current_i

def FunctionDef(current_i, switch):
    if switch == "1":
        fileoutput.write("<Function Definitions> ::= <Function> <Function Definitions Prime>\n")
    current_i = Function(current_i, switch)
    current_i = FunctionDefPrime(current_i, switch)
    return current_i

def FunctionDefPrime(current_i, switch):
    if lexemes[current_i] == "function":
        if switch == "1":
            fileoutput.write("<Function Definitions Prime> ::= <Function Definitions>\n")
        current_i = FunctionDef(current_i, switch)
    else:
        if switch == "1":
            fileoutput.write("<Function Definitions Prime> ::= <Epsilon>\n")
        Empty()
    return current_i

def Function(current_i, switch):
    if lexemes[current_i] == "function":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        if switch == "1":
            fileoutput.write("<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>\n")
        current_i += 1
        
        if tokens[current_i] == "Identifier":
            fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
            if switch == "1":
                fileoutput.write("<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>\n")
            current_i += 1
            
            if lexemes[current_i] == "(":
                fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
                if switch == "1":
                    fileoutput.write("<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>\n")
                current_i += 1
                current_i = OptDeclarationList(current_i, switch)  
                
                if lexemes[current_i] == ")":
                    fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
                    if switch == "1":
                        fileoutput.write("<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>\n")
                    current_i += 1
                    
                    current_i = OptDeclarationList(current_i, switch)  
                    
                    current_i = Body(current_i, switch)  
                        
                else: fileoutput.write('Syntax Error, expected ) \n')
            else: fileoutput.write('Syntax Error, expected ( \n')
        else:  fileoutput.write('Syntax Error, expected identifier \n')    
    else: fileoutput.write('Syntax Error, expected function \n')
    return current_i

def OpParaList(current_i, switch):
    if tokens[current_i] == "Identifier":
        if switch == "1":
            fileoutput.write("<Opt Parameter List> ::= <Parameter List>\n")
        current_i = ParaList(current_i, switch)
    else:
        if switch == "1":
            fileoutput.write("<Opt Parameter List> ::= <Epsilon>\n")
        Empty()    
    return current_i
    
def ParaList(current_i, switch):
    if switch == "1":
        fileoutput.write("<ParameterList> ::= <Parameter> <ParameterListPrime>\n")
    current_i = Paramater(current_i, switch)
    current_i = ParaListPrime(current_i, switch)
    return current_i
    
def ParaListPrime(current_i, switch):
    if tokens[current_i] == "Identifier":
        if switch == "1":
            fileoutput.write("<Parameter List Prime> ::= <Parameter List>\n")
        current_i = ParaList(current_i, switch)
    else:
        if switch == "1":
            fileoutput.write("<Parameter List Prime> ::= <Epsilon>\n")
        Empty()
    return current_i
        
def Paramater(current_i, switch):
    fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
    if switch == "1":
        fileoutput.write("<Parameter> ::= <IDs> <Qualifier> \n")
    current_i = IDs(current_i, switch)
    current_i = Qualifier(current_i, switch)
    return current_i

def OptDeclarationList(current_i, switch):
    if lexemes[current_i] == "integer":
        current_i = DeclarationList(current_i, switch)
        if switch == "1":
            fileoutput.write("<Opt Declaration List> ::= <Declaration List>\n") 
    elif lexemes[current_i] == "boolean":
        current_i = DeclarationList(current_i, switch)  
        if switch == "1":
            fileoutput.write("<Opt Declaration List> ::= <Declaration List>\n")  
    elif lexemes[current_i] == "real":
        current_i = DeclarationList(current_i, switch) 
        if switch == "1":
            fileoutput.write("<Opt Declaration List> ::= <Declaration List>\n") 
    else:    
        if switch == "1":
            fileoutput.write("<Opt Declaration List> ::= <Epsilon>\n")
        Empty()
    return current_i

def DeclarationList(current_i, switch):
    if switch == "1":
        fileoutput.write("<DeclarationList> ::= <Declaration> <DeclarationListPrime>\n")
    current_i = Declaration(current_i, switch)
    
    current_i = DeclarationListPrime(current_i, switch)
    
    return current_i

def DeclarationListPrime(current_i, switch):
    if lexemes[current_i] == ";":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
    if lexemes[current_i] == "integer":
        current_i = DeclarationList(current_i, switch)
        if switch == "1":
            fileoutput.write("<Opt Declaration List Prime> ::= <Declaration List>\n") 
    elif lexemes[current_i] == "boolean":
        current_i = DeclarationList(current_i, switch)  
        if switch == "1":
            fileoutput.write("<Opt Declaration List Prime> ::= <Declaration List>\n")  
    elif lexemes[current_i] == "real":
        current_i = DeclarationList(current_i, switch) 
        if switch == "1":
            fileoutput.write("<Opt Declaration List Prime> ::= <Declaration List>\n") 
    else:    
        if switch == "1":
            fileoutput.write("<Opt Declaration List Prime> ::= <Epsilon>\n")
        Empty()
    return current_i

def Declaration(current_i, switch):
    fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
    if switch == "1":
        fileoutput.write("<Parameter> ::= <Qualifier> <IDs> \n")
    current_i = Qualifier(current_i, switch)
    current_i = IDs(current_i, switch)
    return current_i

def StatementList(current_i, switch):
    if lexemes[current_i] == "{":
        if switch == "1":
            fileoutput.write("<Statement List> ::= <Statement><StatementListPrime> \n")
        current_i = Statement(current_i, switch)
        current_i = StatementListPrime(current_i, switch)
    
    elif tokens[current_i] == "Identifier":
        if switch == "1":
            fileoutput.write("<Statement List> ::= <Statement><StatementListPrime> \n")
        current_i = Statement(current_i, switch)
        current_i = StatementListPrime(current_i, switch)
        
    elif lexemes[current_i] == "if":
        if switch == "1":
            fileoutput.write("<Statement List> ::= <Statement><StatementListPrime> \n")
        current_i = Statement(current_i, switch)
        current_i = StatementListPrime(current_i, switch)  
        
    elif lexemes[current_i] == "return":
        if switch == "1":
            fileoutput.write("<Statement List> ::= <Statement><StatementListPrime> \n")
        current_i = Statement(current_i, switch)
        current_i = StatementListPrime(current_i, switch)   
        
    elif lexemes[current_i] == "print":
        if switch == "1":
            fileoutput.write("<Statement List> ::= <Statement><StatementListPrime> \n")
        current_i = Statement(current_i, switch)
        current_i = StatementListPrime(current_i, switch)
        
    elif lexemes[current_i] == "scan":
        if switch == "1":
            fileoutput.write("<Statement List> ::= <Statement><StatementListPrime> \n")
        current_i = Statement(current_i, switch)
        current_i = StatementListPrime(current_i, switch)               

    elif lexemes[current_i] == "while":
        if switch == "1":
            fileoutput.write("<Statement List> ::= <Statement><StatementListPrime> \n")
        current_i = Statement(current_i, switch)
        current_i = StatementListPrime(current_i, switch)  
    return current_i

def StatementListPrime(current_i, switch):
    if lexemes[current_i] == "{":
        if switch == "1":
            fileoutput.write("<Statement List Prime> ::= <Statement List> \n")
        current_i = StatementList(current_i, switch)
    
    elif tokens[current_i] == "Identifier":
        if switch == "1":
            fileoutput.write("<Statement List Prime> ::= <Statement List> \n")
        current_i = StatementList(current_i, switch)
        
    elif lexemes[current_i] == "if":
        if switch == "1":
            fileoutput.write("<Statement List Prime> ::= <Statement List> \n")
        current_i = StatementList(current_i, switch) 
        
    elif lexemes[current_i] == "return":
        if switch == "1":
            fileoutput.write("<Statement List Prime> ::= <Statement List> \n")
        current_i = StatementList(current_i, switch)   
        
    elif lexemes[current_i] == "print":
        if switch == "1":
            fileoutput.write("<Statement List Prime> ::= <Statement List> \n")
        current_i = StatementList(current_i, switch) 
        
    elif lexemes[current_i] == "scan":
        if switch == "1":
            fileoutput.write("<Statement List Prime> ::= <Statement List> \n")
        current_i = StatementList(current_i, switch)               

    elif lexemes[current_i] == "while":
        if switch == "1":
            fileoutput.write("<Statement List Prime> ::= <Statement List> \n")
        current_i = StatementList(current_i, switch) 
        
    else:
        if switch == "1":
            fileoutput.write("<Statement List> ::= Epsilon \n") 
        Empty()
         
    return current_i

def Statement(current_i, switch):
    if lexemes[current_i] == "{":
        if switch == "1":
            fileoutput.write("<Statement> ::= <Compound> \n")
        current_i = Compound(current_i, switch)
        
    elif tokens[current_i] == "Identifier":
        if switch == "1":
            fileoutput.write("<Statement> ::= <Assign> \n")
        current_i = Assign(current_i, switch)
        
    elif lexemes[current_i] == "if":
        if switch == "1":
            fileoutput.write("<Statement> ::= <If> \n")
        current_i = If(current_i, switch)    
        
    elif lexemes[current_i] == "return":
        if switch == "1":
            fileoutput.write("<Statement> ::= <Return> \n")
        current_i = Return(current_i, switch)     
        
    elif lexemes[current_i] == "print":
        if switch == "1":
            fileoutput.write("<Statement> ::= <Print> \n")
        current_i = Print(current_i, switch)
        
    elif lexemes[current_i] == "scan":
        if switch == "1":
            fileoutput.write("<Statement> ::= <Scan> \n")
        current_i = Scan(current_i, switch)                

    elif lexemes[current_i] == "while":
        if switch == "1":
            fileoutput.write("<Statement> ::= <while> \n")
        current_i = While(current_i, switch)     
    
    else:
        fileoutput.write("Syntax error, expected compound or assign or if or return or print or scan or while \n")    

    return current_i

def Body(current_i, switch):
    if lexemes[current_i] == "{":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Body> ::= { < Statement List> } \n")
            
        current_i = StatementList(current_i, switch)    
        
        if lexemes[current_i] == "}":
            fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
            current_i += 1
            if switch == "1":
                fileoutput.write("<Body> ::= { < Statement List> } \n")
        else:fileoutput.write("Syntax error, expected } \n")        
    else:fileoutput.write("Syntax error, expected { \n")              
    return current_i

def Compound(current_i, switch):
    if lexemes[current_i] == "{":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Compound> ::= { <Statement List> } \n")
            
        current_i = StatementList(current_i, switch)    
        
        if lexemes[current_i] == "}":
            fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
            current_i += 1
            if switch == "1":
                fileoutput.write("<Compound> ::= { <Statement List> } \n")
                
    return current_i

def Assign(current_i, switch):
    if tokens[current_i] == "Identifier":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write(" <Assign> ::= <Identifier> = <Expression> ; \n")
        
        if lexemes[current_i] == "=":
            fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
            current_i += 1
            if switch == "1":
                fileoutput.write(" <Assign> ::= <Identifier> = <Expression> ;\n")
                
            current_i = Expression(current_i, switch)
            
            if lexemes[current_i] == ";":
                fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
                current_i += 1
                if switch == "1":
                    fileoutput.write(" <Assign> ::= <Identifier> = <Expression> ;\n")
            else: fileoutput.write("Syntax error, expected ; \n")
        else: fileoutput.write("Syntax error, expected = \n")
              
    return current_i

def If(current_i, switch):
    if lexemes[current_i] == "if":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<If> ::= <If><IfPrime> \n")
        
        if lexemes[current_i] == "(":
            fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
            current_i += 1
            if switch == "1":
                fileoutput.write("<If> ::= <If><IfPrime> \n" )
                
            current_i = Condition(current_i, switch)    
                
            if lexemes[current_i] == ")":
                fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
                current_i += 1
                if switch == "1":
                    fileoutput.write("<If> ::= <If><IfPrime> \n")   
                    
                current_i = Statement(current_i, switch) 
                current_i = IfPrime(current_i, switch)
    
    return current_i

def IfPrime(current_i, switch):
    if lexemes[current_i] == "endif":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<If> ::= if ( <Condition> ) <Statement> endif \n")
    
    elif lexemes[current_i] == "else":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<If> ::= if ( <Condition> ) <Statement> else <Statement> endif \n")
        
        current_i = Statement(current_i, switch)
        
        if lexemes[current_i] == "endif":
            fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
            current_i += 1
            if switch == "1":
                fileoutput.write("<If> ::= if ( <Condition> ) <Statement> else <Statement> endif \n")
        else: fileoutput.write("Syntax error, expected endif \n")
    else: fileoutput.write("Syntax error, expected endif or else \n")

    return current_i

def While(current_i, switch):
    if lexemes[current_i] == "while":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<While> ::= while ( <Condition> ) <Statement> endwhile \n")
         
        if lexemes[current_i] == "(":
            fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
            current_i += 1
            if switch == "1":
                fileoutput.write("<While> ::= while ( <Condition> ) <Statement> endwhile \n")
                
            current_i = Condition(current_i, switch)
            
            if lexemes[current_i] == ")":
                fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
                current_i += 1
                if switch == "1":
                    fileoutput.write("<While> ::= while ( <Condition> ) <Statement> endwhile \n")
                
                current_i = Statement(current_i, switch)
                
                if lexemes[current_i] == "endwhile":
                    fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
                    current_i += 1
                    if switch == "1":
                        fileoutput.write("<While> ::= while ( <Condition> ) <Statement> endwhile \n")
                else: fileoutput.write("Syntax error, expected endwhile \n")
            else:  fileoutput.write("Syntax error, expected ) \n") 
        else: fileoutput.write("Syntax error, expected ( \n")      
    return current_i

def Condition(current_i, switch):
    if switch == "1":
        fileoutput.write("<Condition> ::= <Expression> <Relop> <Expression> \n")
    current_i = Expression(current_i, switch)
    current_i = Reloop(current_i, switch)
    current_i = Expression(current_i, switch)
    return current_i

def IDs(current_i, switch):
    if tokens[current_i] == "Identifier":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<IDs> ::= <Identifier> <IDsPrime>\n")
        current_i = IDSPrime(current_i, switch)             
    return current_i

def IDSPrime(current_i, switch):
    if lexemes[current_i] == ",":
        current_i += 1
        if switch == "1":
            fileoutput.write("<IDsPrime> ::= <IDs>\n")
        current_i = IDs(current_i, switch)
    else:
        if switch == "1":
            fileoutput.write("<IDsPrime> ::= <Epsilon>\n")
        Empty()
    return current_i

def Qualifier(current_i, switch):
    if lexemes[current_i] == "integer":
        current_i += 1
        if switch == "1":
            fileoutput.write("<Qualifier> ::= integer \n")
    elif lexemes[current_i] == "boolean":
        current_i += 1
        if switch == "1":
            fileoutput.write("<Qualifier> ::= boolean \n")
    elif lexemes[current_i] == "real":
        current_i += 1
        if switch == "1":
            fileoutput.write("<Qualifier> ::= real \n")
    else: fileoutput.write("Syntax error, expected a qualifier integer, boolean or real \n")     
    return current_i

def Scan(current_i, switch):
    if lexemes[current_i] == "scan":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write(" <Scan> ::= scan ( <IDs> ); \n")
        if lexemes[current_i] == "(":
            fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
            current_i += 1   
            if switch == "1":
                fileoutput.write(" <Scan> ::= scan ( <IDs> ); \n")
            current_i = IDs(current_i, switch)
            if lexemes[current_i] == ")":
                fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
                current_i += 1   
                if switch == "1":
                    fileoutput.write("<Scan> ::= scan ( <IDs> ); \n")
                if lexemes[current_i] == ";":
                    fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
                    current_i += 1   
                    if switch == "1":
                        fileoutput.write("<Scan> ::= scan ( <IDs> ); \n")
                else: fileoutput.write("Syntax error, expected a ; \n")    
            else: fileoutput.write("Syntax error, expected a ) \n")     
        else: fileoutput.write("Syntax error, expected a ( \n")     
    return current_i

def Return(current_i, switch):
    if lexemes[current_i] == "return":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<return> ::= <return> <returnPrime>\n")
        current_i = ReturnPrime(current_i, switch)                 
    return current_i

def ReturnPrime(current_i, switch):
    if tokens[current_i] == "Identifier":
        if switch == "1":
            fileoutput.write("<returnPrime> ::= <Expression>;\n")
        current_i = Expression(current_i, switch)
        if lexemes[current_i] == ";":
            current_i += 1
            fileoutput.write("<returnPrime> ::= <Expression>;\n")
        else:
            fileoutput.write("Syntax error, expected a ; \n")
    elif tokens[current_i] == "Integer":
        if switch == "1":
            fileoutput.write("<returnPrime> ::= <Expression>;\n")
        current_i = Expression(current_i, switch) 
        if lexemes[current_i] == ";":
            current_i += 1
            fileoutput.write("<returnPrime> ::= <Expression>;\n")
        else:
            fileoutput.write("Syntax error, expected a ; \n")
    elif tokens[current_i] == "Real":
        if switch == "1":
            fileoutput.write("<returnPrime> ::= <Expression>;\n")
        current_i = Expression(current_i, switch)
        if lexemes[current_i] == ";":
            current_i += 1
            fileoutput.write("<returnPrime> ::= <Expression>;\n")
        else:
            fileoutput.write("Syntax error, expected a ; \n")
    elif lexemes[current_i] == "(":
        if switch == "1":
            fileoutput.write("<returnPrime> ::= <Expression>;\n")
        current_i = Expression(current_i, switch)
        if lexemes[current_i] == ";":
            current_i += 1
            fileoutput.write("<returnPrime> ::= <Expression>;\n")
        else:
            fileoutput.write("Syntax error, expected a ; \n")
    elif lexemes[current_i] == "true":
        if switch == "1":
            fileoutput.write("<returnPrime> ::= <Expression>;\n")
        current_i = Expression(current_i, switch) 
        if lexemes[current_i] == ";":
            current_i += 1
            fileoutput.write("<returnPrime> ::= <Expression>;\n")
        else:
            fileoutput.write("Syntax error, expected a ; \n")        
    elif lexemes[current_i] == "false":
        if switch == "1":
            fileoutput.write("<returnPrime> ::= <Expression>;\n")
        current_i = Expression(current_i, switch)       
        if lexemes[current_i] == ";":
            current_i += 1
            fileoutput.write("<returnPrime> ::= <Expression>;\n")
        else:
            fileoutput.write("Syntax error, expected a ; \n")      
    else:
        if switch == "1":
            fileoutput.write("<returnPrime> ::= <Epsilon>;\n")
        Empty()
        if lexemes[current_i] == ";":
            current_i += 1
            fileoutput.write("<returnPrime> ::= <Epsilon>;\n")
        else:
            fileoutput.write("Syntax error, expected a ; \n")  
    return current_i

def Print(current_i, switch):
    if lexemes[current_i] == "print":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write(" <Print> ::= print ( <Expression>); \n")
        if lexemes[current_i] == "(":
            fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
            current_i += 1   
            if switch == "1":
                fileoutput.write(" <Print> ::= print ( <Expression>); \n")
            current_i = Expression(current_i, switch)
            if lexemes[current_i] == ")":
                fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
                current_i += 1   
                if switch == "1":
                    fileoutput.write(" <Print> ::= print ( <Expression>); \n")
                if lexemes[current_i] == ";":
                    fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
                    current_i += 1   
                    if switch == "1":
                        fileoutput.write(" <Print> ::= print ( <Expression>); \n")
                else: fileoutput.write("Syntax error, expected a ; \n")    
            else: fileoutput.write("Syntax error, expected a ) \n")     
        else: fileoutput.write("Syntax error, expected a ( \n")     
    return current_i

def Expression(current_i, switch):
    if switch == "1":
        fileoutput.write("<Expression> ::= <Term> <Expression> \n")
    current_i = Term(current_i, switch)
    current_i = ExpressionPrime(current_i, switch)    
    return current_i

def ExpressionPrime(current_i, switch):
    if lexemes[current_i] == "+":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Expression Prime> ::= + <Term> <Expression Prime> \n")
        current_i = Term(current_i, switch)
        current_i = ExpressionPrime(current_i, switch)      
            
    elif lexemes[current_i] == "-":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Expression Prime> ::= - <Term> <Expression Prime> \n")
        current_i = Term(current_i, switch)
        current_i = ExpressionPrime(current_i, switch)   
            
    else:
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        if switch == "1":
            fileoutput.write("<Term Prime> ::= <Epsilon> \n")   
        Empty() 
            
    return current_i

def Term(current_i, switch):
    if switch == "1":
        fileoutput.write("<Term> ::= <Term> <TermPrime> \n")
    current_i = Factor(current_i, switch)
    current_i = TermPrime(current_i, switch)    
    return current_i

def TermPrime(current_i, switch):
     
    if lexemes[current_i] == "*":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Term Prime> ::= * <Factor> <Term Prime> \n")
        current_i = Factor(current_i, switch)
        current_i = TermPrime(current_i, switch)      
            
    elif lexemes[current_i] == "/":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Term Prime> ::= / <Factor> <Term Prime> \n")
        current_i = Factor(current_i, switch)
        current_i = TermPrime(current_i, switch)  
            
    else:
        if switch == "1":
            fileoutput.write("<Term Prime> ::= <Epsilon> \n")   
        Empty() 
            
    return current_i

def Factor(current_i, switch):
    if lexemes[current_i] == "-":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Factor> ::= - <Primary>\n")
        current_i = Primary(current_i, switch)
    else:    
        current_i = Primary(current_i, switch)
        if switch == "1":
            fileoutput.write("<Factor> ::= <Primary>\n")
    return current_i

def Primary(current_i, switch):
    if tokens[current_i] == "Identifier":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Primary> ::= <Identifier> \n")
        if lexemes[current_i] == "(":
            fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
            current_i += 1
            if switch == "1":
                fileoutput.write("<Primary> ::= <Identifier> (<IDs>) \n")
                
            current_i = IDs(current_i, switch)
            
            if lexemes[current_i] == ")":
                fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
                current_i += 1 
                if switch == "1":
                    fileoutput.write("<Primary> ::= <Identifier> (<IDs>) \n")
            else: fileoutput.write("Syntax error, expected a )")

                      
    elif tokens[current_i] == "Integer":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Primary> ::= <Integer> \n")
            
    elif tokens[current_i] == "Real":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Primary> ::= <Real> \n")
            
    elif lexemes[current_i] == "true":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Primary> ::= <true> \n")        
        
    elif lexemes[current_i] == "(":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Primary> ::=  (<Expression>) \n") 
            
        current_i = Expression(current_i, switch)
        
        if lexemes[current_i] == ")":
            current_i += 1
            if switch == "1":
                fileoutput.write("<Primary> ::= (<Expression>) \n") 
        else: fileoutput.write("Syntax error, expected a ) \n")           
        
    
    elif lexemes[current_i] == "false":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Primary> ::= <false> \n")  
            
    else: fileoutput.write("Syntax error, expected Identifier or Integer or (Expression) or Real or true or false \n")   
    
    return current_i

def Reloop(current_i, switch):
    relop = ["==", "!=", "!=", ">", "<", "<=", "=>"]
    if lexemes[current_i] in relop:
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Relop> ::= == | != | > | < | <= | =>\n")
        else:
            fileoutput.write("Syntax Error, expected a == or != or > or < or <= or =>\n")
    return current_i

def Empty():
    return

def ParCheck(current_i, switch):
    current_i = RATS24(current_i, switch)
    return current_i

try:
    lexer(file_name)
    switch = input("Enter 0 (Turn off syntax) or 1 (Turn on syntax): ")
    current_i = ParCheck(0, switch)


except OSError:
    print("Can not find the file.")