homens([carlos,mario,jose,joao]).
mulheres([maria,ana,joana,helena]).
progenitores([(jose,joao),(maria,joao),(jose,ana),(maria,ana),(ana,helena),(ana,joana),(joao,mario),(helena,carlos),(mario,carlos)]).

pertence(X,[X|T]).
pertence(X,[H|T]):- pertence(X,T).

homem(X):-homens(L),pertence(X,L).
mulher(X):-mulheres(L),pertence(X,L).
progenitor(X,Y):-progenitores(L), pertence((X,Y),L).

irma(X,Y):-progenitor(A,X),progenitor(A,Y),X\==Y, mulher(X).
irmao(X,Y):-progenitor(A,X),progenitor(A,Y),X\==Y, homem(X).

descendente(X,Y):-progenitor(X,Y).
descendente(X,Y):-progenitor(X,A),descendente(A,Y).

avo(X,Y):-progenitor(X,A),progenitor(A,Y),homem(X).
avo_a(X,Y):-progenitor(X,A),progenitor(A,Y),mulher(X).

pai(X,Y):-progenitor(X,Y),homem(X).
mae(X,Y):-progenitor(X,Y),mulher(X).

tio(X,Y):-irmao(X,A),progenitor(A,Y).
tia(X,Y):-irma(X,A),progenitor(A,Y).

primo(X,Y):-irmao(A,B),progenitor(A,X),progenitor(B,Y),X\==Y.
prima(X,Y):-irma(A,B),progenitor(A,X),progenitor(B,Y),X\==Y.