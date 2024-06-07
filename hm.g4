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

// Admet TYPEID a l'esquerra perque coses com 'Var' no es reconeixen com ID...
def : (ID | TYPEID | NUM | OPPAR) '::' tipus   #definicio
     ;

tipus: TYPEID       #tipusBase
     | <assoc=right> tipus '->' tipus #tipusFuncio
     ;

terme : ID       #paraula
      | NUM           #numero
      | '(' terme ')' #parentesi
      | terme terme   #termeAplicacio
      | '\\' ID '->' terme #termeAbstraccio
      | OPPAR #termeOperador
     ;

OP : ('+'|'-'|'*'|'/');
OPPAR: ('(+)'|'(-)'|'(*)'|'(/)') ;
NUM : [0-9]+ ;
WS  : [ \t\n\r]+ -> skip ;
TYPEID : ('A'..'Z') ('a'..'z'|'A'..'Z')* ; //Paraules que comencen per majúscula, només text
ID : ('a'..'z'|'A'..'Z') (NUM|'_'|PARAULA)* ; //Comencen per una lletra i poden contenir números i '_'
PARAULA : ('a'..'z'|'A'..'Z')+ ;