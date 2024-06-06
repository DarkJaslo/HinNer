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
     | def
     ;

// Admet TYPEID a l'esquerra perque coses com 'Var' no es reconeixen a ID...
def : (ID | TYPEID | NUM | '(' OP ')') '::' TYPEID   #definicio
     ;

terme : ID       #paraula
      | NUM           #numero
      | '(' terme ')' #parentesi
      | terme terme   #termeAplicacio
      | '\\' ID '->' terme #termeAbstraccio
      | OP #termeOperador
     ;

OP : ('+'|'-'|'*'|'/');
NUM : [0-9]+ ;
WS  : [ \t\n\r]+ -> skip ;
TYPEID : ('A'..'Z') ('a'..'z'|'A'..'Z')* ;
ID : ('a'..'z'|'A'..'Z') (NUM|'_'|PARAULA)* ;
PARAULA : ('a'..'z'|'A'..'Z')+ ;
//PARAULA  : [a-zA-Z\u0080-\u00FF]+ ; //Macro per ID, no es fa servir per res mes