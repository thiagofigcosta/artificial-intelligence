%nome(tweety,passaro).
%nome(goldie,peixe).
%nome(squilly,minhoca).

gosta(passaro,minhoca).
gosta(gato,peixe).
gosta(gato,passaro).
gosta(eu,gato).
gosta(gato,eu).

gato_come(X):-gosta(gato,X). 
