%union {
    int num;      // Usado para números inteiros e valores booleanos de condições
    char *str;    // Usado para identificadores e strings literais
}

%token <str> IDENTIFIER STRING_LITERAL TYPE
%token <num> NUMBER
%token VAR IF WHILE SEND RECEIVE PLUS MINUS MULT DIV EQUALS NEQ LT LTE GT GTE LPAREN RPAREN LBRACE RBRACE SEMICOLON COMMA ELSE

%type <num> expression term condition number
%type <str> identifier string_literal type

%%

program:
    statements
    ;

statements:
    statement
    | statements statement
    ;

statement:
    var_declaration
    | assignment
    | if_statement
    | while_loop
    | function_call
    | communication
    ;

var_declaration:
    VAR identifier ":" type SEMICOLON
    | VAR identifier ":" type EQUALS expression SEMICOLON
    ;

assignment:
    identifier EQUALS expression SEMICOLON
    ;

if_statement:
    IF LPAREN condition RPAREN LBRACE statements RBRACE
    | IF LPAREN condition RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE
    ;

while_loop:
    WHILE LPAREN condition RPAREN LBRACE statements RBRACE
    ;

function_call:
    identifier LPAREN expression_list RPAREN SEMICOLON
    ;

expression_list:
    /* Empty */
    | expression
    | expression_list COMMA expression
    ;

communication:
    SEND LPAREN identifier COMMA string_literal RPAREN SEMICOLON
    | RECEIVE LPAREN identifier COMMA string_literal RPAREN SEMICOLON
    ;

expression:
    term
    | expression PLUS term
    | expression MINUS term
    | expression MULT term
    | expression DIV term
    ;

term:
    number
    | identifier
    | STRING_LITERAL
    | function_call
    | LPAREN expression RPAREN
    ;

condition:
    expression EQUALS expression
    | expression NEQ expression
    | expression LT expression
    | expression LTE expression
    | expression GT expression
    | expression GTE expression
    ;

type:
    TYPE
    ;

identifier:
    IDENTIFIER
    ;

number:
    NUMBER
    ;

string_literal:
    STRING_LITERAL
    ;

%%
