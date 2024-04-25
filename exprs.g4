// Gramàtica per expressions senzilles
grammar exprs;
root : expr             // l'etiqueta ja és root
     ;
expr : '(' expr ')' #parentesi
     | <assoc=right> expr '^' expr # potencia
     | expr ('/'|'*') expr    # divisioProducte
     | expr ('+'|'-') expr    # sumaResta
     | NUM              # numero
     ;
NUM : [0-9]+ ;
WS  : [ \t\n\r]+ -> skip ;
WORD : [a-zA-Z\u0080-\u00FF]+ ;