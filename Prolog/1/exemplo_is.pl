fatorial(0, 1).
fatorial(X, Y) :- X1 is X-1, fatorial(X1, Y1), Y is X*Y1.

mdc(X,X,X).
mdc(X,Y,Z):- X > Y, W is X-Y, mdc(W,Y,Z).
mdc(X,Y,Z):- Y > X, W is Y-X, mdc(X,W,Z).

densidade(X,Y) :- populacao(X,P), area(X,A), Y is P/A.

soma ([],0).
soma ([X | L], S) :- soma (L, S1), S is S1+X. 
