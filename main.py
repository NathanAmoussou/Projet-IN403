# Partie 1 : Structure de données

class Sommet():
    def __init__(self, entrant: list, sortant: list):
        self.entrant = entrant
        self.sortant = sortant

class Arc():
    def __init__(self, nom: str, nature: str, duree: float=0):
        self.nature = nature
        self.nom = nom
        self.duree = duree

# Exemple :

arcs = {
    # Remontées
    "CHANROSSA": Arc("CHANROSSA", "télésiège"),
    "ROC MERLET": Arc("ROC MERLET", "télésiège"),
    "ROC MUGNIER": Arc("ROC MUGNIER", "télésiège"),
    "PYRAMIDE": Arc("PYRAMIDE", "téléski"),
    # Pistes
    "Chanrossa": Arc("Chanrossa", "piste noire"),
    "Jean Pachod": Arc("Jean Pachod", "piste rouge"),
    "Roc Merlet": Arc("Roc Merlet", "piste rouge"),
    "Creux": Arc("Creux", "piste rouge"),
    "Roc Mugnier": Arc("Roc Mugnier", "piste rouge"),
    "Plan Mugnier": Arc("Plan Mugnier", "piste bleue"),
    "Mont Russes": Arc("Mont Russes", "piste bleue"),
    "Pyramide": Arc("Pyramide", "piste bleue"),
}

sommets = [
    Sommet(
        [arcs["CHANROSSA"], arcs["ROC MERLET"]],
        [arcs["Chanrossa"], arcs["Jean Pachod"], arcs["Roc Merlet"]]
    ),
    Sommet(
        [arcs["Creux"], arcs["Jean Pachod"], arcs["Chanrossa"]],
        [arcs["CHANROSSA"]]
    ),
    Sommet(
        [arcs["Roc Mugnier"], arcs["Creux"]],
        [arcs["ROC MUGNIER"]]
    ),
    Sommet(
        [arcs["ROC MUGNIER"], arcs["Pyramide"], arcs["Mont Russes"], arcs["Plan Mugnier"]],
        [arcs["Roc Mugnier"], arcs["PYRAMIDE"]]
    ),
    Sommet(
        [arcs["PYRAMIDE"], arcs["Roc Merlet"]],
        [arcs["Plan Mugnier"], arcs["Mont Russes"], arcs["Pyramide"], arcs["ROC MERLET"]]
    )
]

localisation = input("Où vous trouvez-vous ? ")
localisation = localisation.split(" ")
i_tmp = localisation.index("de")
str_tmp = " ".join(localisation[i_tmp+1:])
sommet_tmp = ""
print(str_tmp)
if "haut" in localisation:
    i = 0
    while sommet_tmp == "":
        print(i)
        if arcs[str_tmp] in sommets[i].sortant:
            sommet_tmp = sommets[i]
        print(sommets[i].sortant)
        i += 1

    for arcs in sommet_tmp.sortant:
        print(arcs.nom)
