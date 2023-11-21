from antlr4.error.ErrorListener import ErrorListener
from antlr4 import *
from antlr4 import InputStream, CommonTokenStream

from symbol_table  import SymbolTable
from grammar.yaplLexer import yaplLexer
from grammar.yaplListener import yaplListener
from grammar.yaplParser import yaplParser
from grammar.yaplVisitor import yaplVisitor
from three_address_code_listener import TAC_LISTENER
from three_address_code_visitor import TAC_VISITOR
from error_listener import ErrorListenerC
from tac_to_mips import tac_mips
import json

code = """class Main inherits IO{
    void main() {
        int a = 1;
        int b = 2;
        int c = 3;
        int d = 4;
        if (a < b) {
            if (b < c) {
                if (c < d) {
                    out_int(1);
                } else {
                    out_int(2);
                }
            } else {
                out_int(3);
            }
        } else {
            out_int(4);
        }
    }
}"""


code2 = """class Main inherits IO {
    void simpleFn(int z) {
        int x;
        int y;
        x <- 5;
        y <- 3;
        x <- x*y*z;
        out_int(x);
    }

    void main() {
        int numero;
        numero <- 137;
        simpleFn(numero);
        
    }
}"""

code3 = """class Person {
    int checkSight(int assist) {
        return assist;
    }
}

class NewClass inherits Object {
    int years;
    string fullName;
    int hairColor;
    years <- 5;
    let int first, int second, int third in first + second + third;
    Person human;
    human <- new Human;

    int sight;
    sight <- human.checkSight(6);
    
    int talk() {
        if (years < 10) {
            bool kiss;
            years + 30;
            return 0;
        } else {
            return 1;
        }
        fi
    }
    
    int start() {
        return 1;
    }
}
"""

code4 = """class NewClass inherits IO {
    int years;
    string fullName;
    int hairColor;
    years <- 5;
    let int first, int second, int third in first + second + third;

    int talk() {
        if (years < 10) {
            bool kiss;
            years + 30;
            return 0;
        } else {
            return 1;
        }
        fi
    }

    int add(int num1, int num2) {
        int total <- num1 + num2;
        return total;
    }

    void start() {
        int num1 <- 5;
        int num2 <- 10;
        int num3 <- add(num1, num2);
        out_int(num3);
    }
}"""




input_stream = InputStream(code4)
lexer = yaplLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = yaplParser(stream)
code_errors = ErrorListenerC()
lexer.removeErrorListeners()
lexer.addErrorListener(code_errors)
parser = yaplParser(stream)
parser.removeErrorListeners()
parser.addErrorListener(code_errors)
tree = parser.program()
listener = TAC_LISTENER(code_errors)
visitor = TAC_VISITOR(listener)
result = visitor.visit(tree)

if code_errors.errors:
    print('errors')
    print(code_errors.errors)

else:
    print('TAC')
    formatted_data = json.dumps(visitor.tac, indent=4)
    print(formatted_data)
    mips = tac_mips(listener, visitor)
    for line in mips:
        print(line)
