grammar yapl;

// Tokens
LBRACE: '{';
RBRACE: '}';
LPAREN: '(';
RPAREN: ')';
SEMI: ';';
COMMA: ',';
EQUALS: '=';
ASSIGN: '<-';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
EQ: '==';
NEQ: '!=';
LT: '<';
GT: '>';
GT_EQ: '>=';
LT_EQ: '<=';
AND: '&&';
OR: '||';
COLON: ':';
// Palabras Reservadas
TRUE: 'true';
DOT: '.';
FALSE: 'false';
CLASS: 'class';
INHERITS: 'inherits';
SELF: 'self';
SELF_TYPE: 'SELF_TYPE';
ELSE: 'else';
FI: 'fi';
IF: 'if';
WHILE: 'while';
NEW: 'new';
ISVOID: 'isvoid';
NOT: 'not';
RETURN: 'return';
INT: 'int';
STRING_TYPE: 'string';
BOOL: 'bool';
VOID: 'void';
LET: 'let';
IN: 'in';

program: classDeclaration* EOF;

classDeclaration:
	CLASS TYPE_ID (INHERITS TYPE_ID)? LBRACE classBody RBRACE;

classBody: (
		attributeDeclaration
		| methodDeclaration
		| assignmentDeclaration
		| statement
	)*;

attributeDeclaration: type ID SEMI;

assignmentDeclaration: ID ASSIGN expression SEMI;

type: INT | STRING_TYPE | TYPE_ID | BOOL | VOID | SELF_TYPE;

methodDeclaration: type ID LPAREN parameterList? RPAREN block;

parameterList: parameter (COMMA parameter)*;
parameter: type ID;

statement:
	variableDeclaration
	| letDeclaration
	| ifStatement
	| whileStatement
	| methodCallStatement
	| expressionStatement
	| returnStatement
	| block;

variableDeclaration: type ID (ASSIGN statement)?;

letDeclaration:
	LET type ID (ASSIGN expression)? (
		COMMA type ID (ASSIGN expression)?
	)* IN expression SEMI;

ifStatement:
	IF LPAREN expression RPAREN statement (ELSE statement)? FI;

whileStatement: WHILE LPAREN expression RPAREN statement;

methodCallStatement: ID LPAREN expressionList? RPAREN SEMI;

expressionStatement: expression SEMI;

returnStatement: RETURN expression? SEMI;

expressionList: expression (COMMA expression)*;

block: LBRACE statement* RBRACE;

expression:
	expression MULT expression							
	| expression DIV expression							
	| expression PLUS expression						
	| expression MINUS expression						
	| expression EQ expression							
	| expression LT expression							
	| expression GT expression							
	| expression LT_EQ expression						
	| expression GT_EQ expression						
	| expression NEQ expression							
	| expression AND expression							
	| expression OR expression							
	| expression DOT ID LPAREN expressionList? RPAREN	
	| NEW TYPE_ID										
	| NOT expression									
	| MINUS expression									
	| expression ASSIGN expression						
	| ID												
	| SELF												
	| INTEGER											
	| STRING											
	| TRUE												
	| FALSE												
	| VOID;

// Lexical Specifications
ID: [a-z][a-zA-Z0-9_]*;
TYPE_ID: [A-Z][a-zA-Z0-9_]*;
INTEGER: [0-9]+;
STRING: '"' ( ~["\n\r\t\\] | EscapeSequence)* '"';
fragment EscapeSequence:
	'\\' ('\\' | 'b' | 't' | 'n' | 'r' | 'f');
COMMENT: ('--' .*? '\n' | '(*' .*? '*)') -> skip;
WS: [ \t\r\n]+ -> skip;