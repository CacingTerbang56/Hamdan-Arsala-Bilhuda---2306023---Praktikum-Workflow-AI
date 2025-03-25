anakIbu(andi).
anakIbu(budi).
anakIbu(cika).
anakIbu(dani).
anakIbu(emil).
not(anakIbu(fadil)).

sukaPermen(andi).
sukaPermen(budi).
sukaPermen(cika).
not(sukaPermen(dani)).
not(sukaPermen(emil)).

anak_ibu(X):- anakIbu(X).
dapatPermen(X):-sukaPermen(X).
dapatUang(X):-not(sukaPermen(X)).
nothing(X):-not(anakIbu(X)).

