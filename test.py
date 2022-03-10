CapoluoghiRegioni = {'Abruzzo': 'LAquila', 'Basilicata': 'Potenza', 'Calabria': 'Catanzaro', 'Campania': 'Napoli', 'EmiliaRomagna': 'Bologna', 'Friuli': 'Trieste', 'Lazio': 'Roma', 'Liguria': 'Genova', 'Lombardia': 'Milano',
                     'Marche': 'Ancona', 'Molise': 'Campobasso', 'Piemonte': 'Torino', 'Puglia': 'Bari', 'Sardegna': 'Cagliari', 'Sicilia': 'Palermo', 'Toscana': 'Firenze', 'Trentino': 'Trento', 'Umbria': 'Perugia', 'ValledAosta': 'Aosta', 'Veneto': 'Venezia'}

regione = input()

for key, value in CapoluoghiRegioni.items():
       if regione == key:
           namcapoluogo = value
print(namcapoluogo)