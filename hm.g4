grammar hm;
root : terme             // l'etiqueta ja és root
     | def
     ;

def : (ID | NUM | OPPAR) '::' tipus   #definicio
     ;

tipus: TYPEID       #tipusBase
     | '(' tipus '->' tipus ')' #tipusCompost
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
ID : ('a'..'z') (NUM|'_'|PARAULA)* ; //Comencen per una lletra minúscula i poden contenir números i '_'
PARAULA : ('a'..'z'|'A'..'Z')+ ;