# Disease Spread Simulator
Created as a project at AGH UST

Jedna kratka to około 7.69m\
Czyli jej pole to około 60m2\
Na jedną kratkę drogi maksymalnie więc może znajdować się około 60 osób (założenie 1 osoba - 1m2)\
prędkość chodu = około 5 km/h = około 1.4 m/s\
7.69 / 1.4 = 5.5s - taki jest interwał czasowy symulacji\
przyjmuję, że godzina zajmuje 654 iteracje, wtedy:\
daje to 15696 iteracji na dzień\
1 iteracja - czas potrzebny na pokonanie jednej kratki


Godzina | Numer iteracji
--------:|--------------:
 0:00  |      0
 1:00  |    654
 2:00  |   1308
 3:00  |   1962
 4:00  |   2616
 5:00  |   3270
 6:00  |   3924
 7:00  |   4578
 8:00  |   5232
 9:00  |   5886
10:00  |   6540
11:00  |   7194
12:00  |   7848
13:00  |   8502
14:00  |   9156
15:00  |   9810
16:00  |  10464
17:00  |  11118
18:00  |  11772
19:00  |  12426
20:00  |  13080
21:00  |  13734
22:00  |  14388
23:00  |  15042
24:00  |  15696



22:00 - 2:00 - większe prawdopodobieństwo na imprezę\
8:00 - 18:00 - większe prawdopodobieństwo na naukę i sport\
22:00 - 4:00 - większe prawdopodobieństwo na sen\

impreza - timeout na 30min - 2h (losowane)\
nauka   - timeout na 1h 30min -  4h (losowane)\
sport - timeout na 1h30min - 2h30min (losowane)\
sen - timeout na 6h - 10h (losowane)

kwarantanna - quarantine probability
higiena - Student.hygiene

Scenariusz | parametr higieny |prawdopodobieństwo wykrycia choroby | parametr dobrego wykrycia | parametr błędnego wykrycia
---|---|---|---|---
brak kwarantanny, zła higiena | 0.8 | 0 | 1 | 0
brak kwarantanny, średnia higiena | 0.5 | 0 | 1 | 0
brak kwarantanny, dobra higiena | 0.1 | 0 | 1 | 0
kwarantanna z dobrym testem, średnia higiena | 0.5 | 5 | 0.1 | 0
kwarantanna z średnim testem, średnia higiena | 0.5 | 5 | 0.5 | 0
kwarantanna z złym testem, średnia higiena | 0.5 | 5 | 1 | 0
kwarantanna z średnim testem, średnia higiena z niewielkim błędnym wykryciem | 0.5 | 5 | 1 | 0.5
kwarantanna z średnim testem, średnia higiena z dużym błędnym wykryciem | 0.5 | 5 | 1 | 0.1