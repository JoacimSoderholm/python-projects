Innehåller installerade filer för program för att simulera Mitsubishin, bör funka att köra direkt på annan dator, annars får man söka upp programmet via internet.

Innehåller också original-filen som hämtades ut ur Mitsubishin samt den som idag körs 2016-2017 (...400_EO4_PLUS), notera att när pelletsmotorn körs öppnas två reläer, det andra används för att mäta att så sker, via tillkopplade Raspberry Pi och loggly.com.

Ändringen som gjorts för att få det att funka hösten 2017 var att ändra Counter B61 till värde 400, av någon anledning hade det fått värde 0. Tester visar att det säkert också fungerar bra med ett värde 300 men lägre än det kan vara dåligt.
Detta värde används för att mäta mot flamvaktens värde. Flamvakten kan pendla mellan 0 och 550 men i totalt mörker verkar den ändå röra sig mellan 100-200.. 400 fungerar, original var det 550 men flamvakten var nog bättre.

En annan förbättring som kan göras är att hitta varför den väntar så länge från det att den sett att värdet på flamvakten är över 400 till det att den börjar mata på med pellets. Detta orsakar ett uppstartsbeteende som inte är bra, den pendlar mellan av och på i långa stunder innan den fått så mycket pellets att den orkar hålla flamman uppe så länge att motorn hinner få fram pellets innan flamman börjat bli svagare igen.

ppt innehåller resultat av undersökning av de olika inputs och outputs som Mitsubishin har.


Uppdatering 2017-05-25:
Ändrade så att tiden från upptäckt eld till start av pelletsmatning = 3 sekunder.
Ändrade så att tiden från att eld inte längre syns till nedstängning av pelletsmatning till 25 sekunder.
Ändrade gränsvärdet för när eld anses angiven av flamvakt från 400 till 350 (analogt värde).

Påverkade signaler i programmet: B33 (COUNTER to 3). B04 (OFF DELAY 25s). B61 (COUNTER (ACTUALLY CONSTANT) 350).