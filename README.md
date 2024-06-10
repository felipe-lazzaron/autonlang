# Compilador para AutonLang

![image](https://github.com/felipe-lazzaron/autonlang/assets/78042819/3c87f592-d877-4ab7-aceb-50ba2fa209a4)

Compilador: my_compiler.cpp

Build do Compilador LLVM: https://drive.google.com/file/d/1b9y8k9Qslb9YpC0zKZ3jx-X-C5st8M-V/view?usp=sharing

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

## Exemplo

```
// Teste de Inicialização de Veículo
var status: string = "inativo";
var velocidade: int = 0;
var destino: gps;

// Função para iniciar o veículo
function iniciarVeiculo() {
    status = "ativo";
    print("Veículo ativado.");
}

// Função para definir destino
function definirDestino(lat: float, long: float) {
    destino.lat = lat;
    destino.long = long;
    print("Destino definido para: ", destino);
}

// Função para ajustar velocidade
function ajustarVelocidade(v: int) {
    if (v >= 0) {
        velocidade = v;
        print("Velocidade ajustada para: ", velocidade, " km/h");
    } else {
        print("Valor de velocidade inválido!");
    }
}

// Função para parar o veículo
function pararVeiculo() {
    velocidade = 0;
    print("Veículo parado.");
}

// Simulação de recebimento de dados de outro veículo
receive(vehicleData: string, message: string) {
    if (message == "obstaculo_proximo") {
        print("Obstáculo detectado! Reduzindo velocidade.");
        ajustarVelocidade(velocidade / 2);
    }
}

// Main program
iniciarVeiculo();
definirDestino(35.6895, 139.6917); // Coordenadas para Tóquio
ajustarVelocidade(60);
send(status, "Veículo se aproximando do destino com velocidade de 60 km/h");
pararVeiculo();
```

## Licença

Este projeto está licenciado sob a Licença MIT.
  
---
