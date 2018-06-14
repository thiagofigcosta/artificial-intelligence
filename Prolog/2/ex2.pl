mente(leao,1).
mente(leao,2).
mente(leao,3).

mente(unicornio,4).
mente(unicornio,5).
mente(unicornio,6).

dia('domingo',0).
dia('segunda',1).
dia('terça',2).
dia('quarta',3).
dia('quinta',4).
dia('sexta',5).
dia('sabado',6).

ontem(0,1).
ontem(1,2).
ontem(2,3).
ontem(3,4).
ontem(4,5).
ontem(5,6).
ontem(6,0).

quediaehoje(D):- ontem(Y,X)	,(mente(leao,X),not(mente(leao,Y));mente(leao,Y),not(mente(leao,X)))
							,(mente(unicornio,X),not(mente(unicornio,Y));mente(unicornio,Y),not(mente(unicornio,X)))
							,dia(D,X).