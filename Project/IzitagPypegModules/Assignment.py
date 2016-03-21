from __future__ import unicode_literals, print_function
from pypeg2 import *

#This modules works on assigning a value to a variable
#An assignment has the following characteristics
"""
//Defining what an assignment statement can be:
<assignStatement> := <datatype> <identifier> '=' <sumexpression> | <expression>';'
"""

class Type(Keyword):
    grammar = Enum( K("int"), K("bool") , K("String") )

class Identifier(str):
    grammar = re.compile(r"[^\d\W]\w*")

class Expression(str):
    grammar = word
    
class String(str):
    grammar = re.compile(r"\"[^\"]+\"")

class BoolLiteral(Symbol):
     grammar = Enum( K("True"), K("False") )
     
class Digit(str):
     grammar = re.compile(r"\d+")
    
class Assignment(str):
    grammar = attr("type", Type), attr("identifier",Identifier ), ":=" , attr("expression", String) , ";"
    
    
stringToParse = "String myFirstVariable:=  \"escaped quote\" ;"
f = parse(stringToParse, Assignment)

print(f.type)
print(f.identifier)
print(f.expression)