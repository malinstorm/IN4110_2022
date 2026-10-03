Dette prosjektet inneholder en enkel, hjemmesnekret array-klasse inspirert av grunnleggende funksjonalitet i NumPy.

array_class.py inneholder Array-klassen og implementerer støtte for enkle 1D- og 2D-arrays. Klassen støtter blant annet addisjon, subtraksjon og multiplikasjon mellom arrays, samt de samme operasjonene mellom et array og en skalar. Den inneholder også funksjonalitet for sammenligning av arrays, elementvis sammenligning, indeksering, minste verdi og gjennomsnittsverdi.

test_array.py inneholder tester av funksjonaliteten i Array-klassen. Testene dekker både heltall og flyttall, skalaroperasjoner, sammenligning av arrays og enkle operasjoner på 1D- og 2D-arrays.

Testing

Testene kjøres fra test_array.py.

Filen bruker variablene shape1 og shape2, som begge har verdien (4,). Disse er allerede definert i test_array.py.

Koden er testet både manuelt og med pytest.

Hvis pytest ikke er installert, installer det først med:

py -m pip install pytest

Kjør deretter testene med:

py -m pytest test_array.py -q

Testfilen kan også kjøres manuelt med:

py test_array.py

Alle 12 testene skal passere.