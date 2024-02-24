# Code for a lexical analyzer using a Finite State Machine goes
#Helper Function
# separator_check(), operator_check(), keyword_check()
#Check to see if the char is a separator

def separator_check(char):
  separator = {'(', ')', '{', '}', '%', '@', ',', '[', ']', ';'}
  if char in separator:

    return 1
  else:
    return 0


#Check to see if the char is a operator
def operator_check(char):
  operator = {'+', '-', '*', '/', '>', '<', '=', ':'}
  if char in operator:

    return 1
  else:
    return 0


#Check to see if the str is a keyword
def keyword_check(word):
  keywords = ['integer', 'if', 'else', 'endif', 'while', 'return', 'scan', 'print', 'for', 'elseif']
  if word in keywords:
    #print ("Keyword", word)
    return 1
  else:
    return 0


def char_to_col(char):
  if (char.isdigit()):
    return 1
  elif (char == '.'):
    return 2
  elif (char.isalpha()):
    return 3
  elif (char == '_'):
    return 4
  else:
    return 5


def dfsm_int(str):
  '''
    starting state 1 accepting state 2
    array[state][col]
    array[1][1]
    array[3][1]
    0  1(d) 2(.)  3(l)  4(_)  5(invalid)      

    1   2    0      0     0      0             

    2   2    0      0     0      0             
    '''

  state = 1
  accepting_state = [2]
  table = [[0, 1, 2, 3, 4, 5], [1, 2, 0, 0, 0, 0], [2, 2, 0, 0, 0, 0]]

  for i in range(len(str)):
    col = char_to_col(str[i])
    state = table[state][col]
    if state == 0:
      break

  if state == accepting_state[0]:

    return 1
  else:
    return 0


def dfsm_real(str):
  '''

  0  1(d) 2(.)  3(l)  4(_)  5(invalid)

  1   2    0      0     0      0    

  2   2    3      0     0      0   

  3   4    0      0     0      0

  4   4    0      0     0      0
  '''
  state = 1
  accepting_state = [2, 3, 4]
  table = [[0, 1, 2, 3, 4, 5], [1, 2, 0, 0, 0, 0], [2, 2, 3, 0, 0, 0],
           [3, 4, 0, 0, 0, 0], [4, 4, 0, 0, 0, 0]]

  for i in range(len(str)):
    col = char_to_col(str[i])
    state = table[state][col]
    if state == 0:
      break

  if state == accepting_state[0] or state == accepting_state[1] or state == accepting_state[2]:
    return 1
  else:
    return 0


##Double check my work yall!
def dsfm_id(str):
  '''
  DFSM to recognize identifiers

  0  1(d) 2(.)  3(l)  4(_)  5(invalid)

  1   0    0      2     0      0    

  2   3    0      3     3      0   

  3   4    0      4     4      0

  4   4    0      4     4      0

  '''
  state = 1
  accepting_state = [2, 3, 4]
  table = [[0, 1, 2, 3, 4, 5], [1, 0, 0, 2, 0, 0], [2, 3, 0, 3, 3, 0],
           [3, 4, 0, 4, 4, 0], [4, 4, 0, 4, 4, 0]]

  for i in range(len(str)):
    col = char_to_col(str[i])
    state = table[state][col]
    if state == 0:
      break

  if state == accepting_state[0] or state == accepting_state[
      1] or state == accepting_state[2]:
    return 1
  else:
    return 0



def lexer(filename):
  with open(filename, "r") as file:
    content = file.read()
    word = ""
    white_space = ""
    contain_white_space = False
    contain_operator = False
    contain_seperator = False
      
    if contain_white_space == False and contain_operator == False and contain_seperator == False:
            while not contain_white_space or contain_operator or contain_seperator:
                i = 0
                for i in range(len(content)):
                    word = content[i]
                    if word == white_space:
                        word = word[0:i-1]
                        contain_white_space = True
                    elif operator_check(word) == 1:
                        word = word[0:i-1]
                        contain_operator = True
                    elif separator_check(word) == 1:
                        word = word[0:i-1]
                        contain_seperator = True
        
        
    elif contain_white_space == True or contain_operator == True or contain_seperator == True:
        
            for char in word:
                if operator_check(word[char]) == 1:
                    print(word, "                   Operator")
                    word = ""
                    contain_white_space = False
                    contain_operator = False
                    contain_seperator = False

                
                elif separator_check(word[char]) == 1:
                    print(word, "                   Separator")
                    word = ""
                    contain_white_space = False
                    contain_operator = False
                    contain_seperator = False
                
                
                elif word[char].isalpha():
                    if keyword_check(word) == 1:
                        print(word, "               Keywords")
                    else:
                        dsfm_id(word)
                        if dsfm_id == 1:
                            print(word, "                   Identifier")
                        elif dsfm_id == 0:
                            print(word, "                   Invalid")
                    word = ""
                    contain_white_space = False
                    contain_operator = False
                    contain_seperator = False
                    
                elif word[char].isdigit():
                    if dfsm_int(word) == 1:
                        print(word, "                   Integers")
                elif dfsm_int(word) == 0:
                    dfsm_real(word)
                    if dfsm_real(word) == 1:
                        print(word, "                 Reals")
                    elif dfsm_real(word) == 0:
                        print(word, "                   Invalid")
                    word = ""
                    contain_white_space = False
                    contain_operator = False
                    contain_seperator = False
                    
                

find = True
while(find):
  try:
    file_name = input('Enter the filename: ')
    print("Tokens:              Lexemes:")
    lexer(file_name)
    find = False
  except OSError:
     print("Can not find the file.")
