with open("Game of Thrones.txt","r",encoding="utf-8") as f:
    testo=f.readlines()
    print(f"Il libro contiene {len(testo)} righe")

    righeEffettive=[el for el in testo if el!='\n']
    print(f"Il numero effettivo di righe del libro è: {len(righeEffettive)}")

    print(f"Nel libro ci sono {len([el for el in testo if el.isupper()])} capitoli")

    conteggio_capitoli = {}
    for capitolo in [el for el in testo if el.isupper()]:
        if capitolo in conteggio_capitoli:
            conteggio_capitoli[capitolo] += 1
        else:
            conteggio_capitoli[capitolo] = 1
    print(conteggio_capitoli)

with open('Jon_Snow_lines.txt', 'w') as file:
    for i, riga in enumerate(righeEffettive):
        if 'Jon Snow' in riga:
            file.write(f"{i + 1} \"{riga}\"\n")
