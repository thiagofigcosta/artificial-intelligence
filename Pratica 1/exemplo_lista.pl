pertence(X, [ X | _ ] ).
pertence(X, [ _ | L ] ) :- pertence(X, L).

concatena( [], L, L).
concatena( [ X | L1 ], L2, [ X | L3 ]) :- concatena(L1, L2, L3).

igual([],[]).
igual([ X | L1], [X | L2] ) :- igual(L1, L2).

remove(X, [X | L], L).
remove(X, [ Y | L1 ], [ Y | L2 ] ) :- remove(X, L1, L2).

primeiro([P | _], P).
ultimo([U], U).
ultimo([_ | R], U) :- ultimo(R, U). 
