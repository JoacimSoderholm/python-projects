Inneh�ller installerade filer f�r program f�r att simulera Mitsubishin, b�r funka att k�ra direkt p� annan dator, annars f�r man s�ka upp programmet via internet.

Inneh�ller ocks� original-filen som h�mtades ut ur Mitsubishin samt den som idag k�rs 2016-2017 (...400_EO4_PLUS), notera att n�r pelletsmotorn k�rs �ppnas tv� rel�er, det andra anv�nds f�r att m�ta att s� sker, via tillkopplade Raspberry Pi och loggly.com.

�ndringen som gjorts f�r att f� det att funka h�sten 2017 var att �ndra Counter B61 till v�rde 400, av n�gon anledning hade det f�tt v�rde 0. Tester visar att det s�kert ocks� fungerar bra med ett v�rde 300 men l�gre �n det kan vara d�ligt.
Detta v�rde anv�nds f�r att m�ta mot flamvaktens v�rde. Flamvakten kan pendla mellan 0 och 550 men i totalt m�rker verkar den �nd� r�ra sig mellan 100-200.. 400 fungerar, original var det 550 men flamvakten var nog b�ttre.

En annan f�rb�ttring som kan g�ras �r att hitta varf�r den v�ntar s� l�nge fr�n det att den sett att v�rdet p� flamvakten �r �ver 400 till det att den b�rjar mata p� med pellets. Detta orsakar ett uppstartsbeteende som inte �r bra, den pendlar mellan av och p� i l�nga stunder innan den f�tt s� mycket pellets att den orkar h�lla flamman uppe s� l�nge att motorn hinner f� fram pellets innan flamman b�rjat bli svagare igen.

ppt inneh�ller resultat av unders�kning av de olika inputs och outputs som Mitsubishin har.


Uppdatering 2017-05-25:
�ndrade s� att tiden fr�n uppt�ckt eld till start av pelletsmatning = 3 sekunder.
�ndrade s� att tiden fr�n att eld inte l�ngre syns till nedst�ngning av pelletsmatning till 25 sekunder.
�ndrade gr�nsv�rdet f�r n�r eld anses angiven av flamvakt fr�n 400 till 350 (analogt v�rde).

P�verkade signaler i programmet: B33 (COUNTER to 3). B04 (OFF DELAY 25s). B61 (COUNTER (ACTUALLY CONSTANT) 350).