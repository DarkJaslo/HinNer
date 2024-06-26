# HinNer-LP-2024

Pràctica de llenguatges de programació, primavera 2024. El nom ve de Hindley-Milner.

Analitzador d'expressions tipus Haskell amb inferència de tipus senzilla.

Per executar, cal primer processar la gramàtica:
```.sh
antlr4 -Dlanguage=Python3 -no-listener -visitor hm.g4
```

I després executar amb:

```.sh
streamlit run hm.py
```

Això donarà a la terminal un enllaç a localhost per fer servir la pàgina de Streamlit.

### Funcionalitats

L'analitzador té les funcionalitats descrites als 6 punts de l'enunciat de la pràctica. 

- Els operadors matemàtics reconeguts són +, -, * i /, per simplicitat. Es poden definir funcions amb noms de variable.
- Els identificadors de variables són paraules que comencen per minúscula i poden contenir més endavant '_' o números.
- Els identificadors de tipus són paraules que comencen per majúscula i només admeten lletres.

Com a restricció, totes les funcions han d'estar ben definides. No admet això:

```haskell
func :: a -> b -> c
```
I per tant no fa inferència de tipus sobre funcions. Això sí funciona:
```haskell
func :: A -> B -> C
```

S'assumirà que tots els identificadors de tipus són tipus concrets (A, N, Natural, Bool, QualsevolCosa). 

Un exemple que funciona:

```haskell
2 :: Natural
(*) :: Natural -> Natural -> Natural
\x -> (*) 2 x

var :: Natural
\x -> (*) var x
```

### Informació sobre la implementació

La part d'inferència de tipus es fa purament amb l'arbre generat pel visitador, alguns diccionaris i tractament de _strings_. Això últim no era el que es pretenia, però no se'ns va donar info i em feia més gràcia això que perdre el temps buscant, encara més amb totes les altres entregues que hi havia.

Pel que fa a la resta, es poden veure els comentaris.

S'ha fet servir _autopep8_ pel format del codi.