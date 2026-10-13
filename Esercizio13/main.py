from Contenuto.Video.video import Video
from Contenuto.Podcast.podcast import Podcast
from Contenuto.LibroDigitale.librodigitale import LibroDigitale

def main():
    # 1. Creare una piccola collezione di contenuti diversi
    collezione = [
        Video(titolo="Tutorial Python", autore="Mario Rossi", durata="10:00", frame_rate=60, qualità="1080p", like=150, dislike=2),
        Podcast(titolo="La storia dell'informatica", autore="Luigi Verdi", durata="45:00", ospite="Alan Turing"),
        LibroDigitale(titolo="Imparare Python", autore="Mario Rossi", durata="N/A", numero_pagine=300, codice_attivazione="PY-2024-ABC"),
        Video(titolo="Recensione Smartphone", autore="Giulia Bianchi", durata="15:30", frame_rate=30, qualità="4K", like=3000, dislike=50),
        Podcast(titolo="Chiacchiere tech", autore="Giulia Bianchi", durata="60:00", ospite="Bill Gates")
    ]

    # 2. Mostrare i dati di tutti gli elementi
    print("--- TUTTI I CONTENUTI ---")
    for contenuto in collezione:
        print(contenuto)

    # 3. Filtrare gli elementi secondo almeno un criterio scelto da te
    # Criterio: Filtrare per autore "Mario Rossi"
    autore_scelto = "Mario Rossi"
    print(f"\n--- CONTENUTI FILTRATI PER AUTORE: {autore_scelto} ---")
    contenuti_filtrati = [c for c in collezione if c.autore == autore_scelto]
    
    if contenuti_filtrati:
        for contenuto in contenuti_filtrati:
            print(contenuto)
    else:
        print("Nessun contenuto trovato per questo autore.")

    # Altro criterio: Filtrare solo i Podcast
    print(f"\n--- CONTENUTI FILTRATI PER TIPO: Podcast ---")
    podcast_filtrati = [c for c in collezione if isinstance(c, Podcast)]
    
    if podcast_filtrati:
        for podcast in podcast_filtrati:
            print(podcast)
    else:
        print("Nessun podcast trovato.")

if __name__ == "__main__":
    main()
