// Gramàtica per expressions senzilles
/*
grammar hm;
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
*/

grammar hm;
root : terme             // l'etiqueta ja és root
     ;

terme : PARAULA       #paraula
      | NUM           #numero
      | '(' terme ')' #parentesi
      | abstraccio    #termeAbstraccio
      | terme terme   #termeAplicacio
      | ('+'|'-'|'*'|'/') #termeOperador
     ;

abstraccio : '\\' PARAULA '->' terme 
     ;
NUM : [0-9]+ ;
WS  : [ \t\n\r]+ -> skip ;
PARAULA  : [a-zA-Z\u0080-\u00FF]+ ;