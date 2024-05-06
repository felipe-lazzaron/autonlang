%{
#include "autonlang.tab.h"  // Inclui o arquivo gerado pelo Bison
%}

%%

[ \t\n]+              ;  // Ignora espaços em branco

"var"                 { return VAR; }
"if"                  { return IF; }
"while"               { return WHILE; }
"send"                { return SEND; }
"receive"             { return RECEIVE; }

[a-zA-Z_][a-zA-Z0-9_]*    { yylval.str = strdup(yytext); return IDENTIFIER; }
[0-9]+                   { yylval.num = atoi(yytext); return NUMBER; }
\"([^"\\]|\\.)*\"        { yylval.str = strdup(yytext); return STRING_LITERAL; }

"+"                     { return PLUS; }
"-"                     { return MINUS; }
"*"                     { return MULT; }
"/"                     { return DIV; }

.                       { return *yytext; }  // Retorna o próprio caractere para todos os outros caracteres

%%
