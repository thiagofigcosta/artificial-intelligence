estrela(sol).
estrela(sirius).
orbita(venus, sol).
orbita(terra, sol).
orbita(marte, sol).
orbita(lua, terra).
orbita(phobos, marte).
orbita(deimos, marte).

planeta(B) :- orbita(B, sol).
satélite(B) :- orbita(B, P), planeta(P).

gosta(maria, peixe).
gosta(pedro, vinho).
gosta(maria, vinho).
gosta(pedro, maria).