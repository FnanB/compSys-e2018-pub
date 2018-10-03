# Exercises for 1/10-2018

Opgaver fra 26/9 såfremt I ikke allerede har løst dem.

Bemærk fejl i opgave 3, hvor programmet et sted i løkken 
skal indeholde linien "n++;"

Referencer til slides, er til slides fra 26/9 og 24/9


## Opgave 1

Antag at multiplexorne nederst til venstre på figuren over
A2's mikroarkitektur er implementeret efter samme princip
som illustreret ved slide 13 fra 26/9.

Hvor mange styre-ledninger skal der trækkes til hver mux?


## Opgave 2

Der er ingen direkte signalvej fra output-siden af registrene
til input-siden af samme. Så når MOVQ operationerne skal have
kopieret et register til et andet, så må værdien flyde igennem
comput-unit, der er ingen anden vej.

Foreslå hvordan man kan bruge compute-unit til at føre en værdi
igennem uændret


## Opgave 3

Compute-unit modtager 3 64-bit operander. (se evt slide med
compute unit i slide-set fra 24/9). To af de tre operander
kommer fra registre, det sidste fra dekoderen.

Hvis du betragter ordre-indkodningen (slides fra 24/9 eller
encoding.txt udleveret sammen med A2) kan du se at instruktionerne
udpeger registre ved hjælp af bits benævnt "dddd", "ssss" og "zzzz"

Opstil en tabel som for hver instruktion angiver hvilket
register der skal udlæses fra registrene og gives videre som
hver af de to register-operander til compute-unit.


## Opgave 4

Compute-unit modtager en 64-bit værdi fra afkodningen af instruktionen.
Men konstanterne indlejret i instruktionen er kun 32-bit.

Gennemgå de til A2 udleverede ".h" filer og find ud af hvordan du
kan forvandle en 32-bit værdi til en 64-bit værdi.


## Opgave 5

Konstanter indlejret i instruktioner kan være placeret forskellige
steder i forhold til starten af instruktionen.

Skitser et kredsløb som kan "udtage" en indlejret konstant fra det
rette sted (hint: det er noget med en mux)

Er der brug for ET eller TO sådanne kredsløb i mikroarkitekturen?
Begrund svaret.

