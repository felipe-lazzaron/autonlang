# Compilador para AutonLang

![image](https://github.com/felipe-lazzaron/autonlang/assets/78042819/3c87f592-d877-4ab7-aceb-50ba2fa209a4)


## Sobre a AutonLang

A AutonLang é uma linguagem de programação projetada especificamente para facilitar a comunicação e operação segura entre veículos autônomos, incluindo carros, motos, drones e aviões. A motivação por trás dessa linguagem é criar um sistema universal que permita que esses veículos trafeguem e interajam de forma segura em qualquer ambiente terrestre ou aéreo, melhorando a coordenação e eficiência no trânsito e na logística global.

## EBNF da AutonLang

Aqui está a EBNF (Extended Backus-Naur Form) que define a sintaxe da AutonLang:

```ebnf
<program> ::= <statement>+

<statement> ::= <var_declaration> | <assignment> | <if_statement> | <while_loop> | <function_call> | <communication>

<var_declaration> ::= "var" <identifier> ":" <type> ["=" <expression>] ";"

<assignment> ::= <identifier> "=" <expression> ";"

<if_statement> ::= "if" "(" <condition> ")" "{" <statement>+ "}" ["else" "{" <statement>+ "}"]

<while_loop> ::= "while" "(" <condition> ")" "{" <statement>+ "}"

<function_call> ::= <identifier> "(" [<expression> {"," <expression>}] ")"

<communication> ::= "send" "(" <identifier> "," <message> ")" | "receive" "(" <identifier> "," <message> ")"

<expression> ::= <term> {("+" | "-" | "*" | "/") <term>}

<term> ::= <identifier> | <number> | <function_call> | "(" <expression> ")"

<condition> ::= <expression> ("==" | "!=" | "<" | "<=" | ">" | ">=") <expression>

<type> ::= "int" | "float" | "string" | "bool" | "gps"

<identifier> ::= <letter> {<letter> | <digit> | "_"}

<message> ::= <string_literal> | <function_call>

<number> ::= <digit>+

<string_literal> ::= '"' <char>* '"'

<letter> ::= "a" | ... | "z" | "A" | ... | "Z"

<digit> ::= "0" | ... | "9"

<char> ::= <letter> | <digit> | <special_char>

<special_char> ::= " " | "!" | "?" | "." | "," | ";" | ":"
```

## Como usar este compilador

Em breve

## Contribuições

Em breve

## Licença

Este projeto está licenciado sob a Licença MIT.
  
---
