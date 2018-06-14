pai(carlos,madalena).
mae(madalena,manoel).
pai(manoel,felipe).
pais(X,Y) :- pai(X,Y).
pais(X,Y) :- mae(X,Y).
descendente(X,Y):- pais(Y,X). % caso base da recursao
descendente(X,Y):- pais(Z,X), descendente(Z,Y). % passo recursivo 
