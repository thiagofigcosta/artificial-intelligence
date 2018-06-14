filho().%preencher com os dados
filha().%preencher com os dados
pai(X,Y):-filho(Y,X),filha(Y,X).
mãe(X,Y):-filho(Y,X),filha(Y,X).
tio(X,Y):-pai(F,Y),mae(F,Y),filho(X,F).
tia(X,Y):-pai(F,Y),mae(F,Y),filha(X,F).
primo(X,Y):-pai(F,Y),mae(F,Y),filho(R,F),filha(R,F),filho(X,R),filha(X,R).
avo(X,Y):-mae(R,Y),mae(X,R).
avo(X,Y):-pai(R,Y),pai(X,R).
cunhada(X,Y):-pai(X,Y),mae(X,Y),. 
