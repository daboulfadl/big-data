from collections import defaultdict

bestSongInTheWorld = """
Au début des années 80, je me souviens des soirées
Où l'ambiance était chaude et les mecs rentraient
Stan Smith aux pieds le regard froid
Ils scrutaient la salle le trois-quart en cuir roulé autour du bras
Ray Ban sur la tête survêtement Tacchini

Pour les plus classes les mocassins Nébuloni
Dès qu'ils passaient Cameo Midnight Star
SOS Band Delegation ou Shalamar
Tout le monde se levait des cercles se formaient
Des concours de danse un peu partout s'improvisaient
Je te propose un voyage dans le temps, via planète Marseille

Je danse le MIA
Hey DJ met nous donc du Funk, que je danse le MIA
Je danse le MIA
Fait pousser le Pioneer à fond qu'on danse le MIA
Je danse le MIA
Ce soir les bagues brilleront on danse le MIA 

Je danse le MIA
Hey DJ met nous donc du Funk, je danse le MIA

Je danse le MIA jusqu'à ce que la soirée vacille
Une bagarre au fond et tout le monde s'éparpille
On râlait que c'était nul que ça craignait
Le samedi d'après on revenait tellement qu'on s'emmerdait
J'entends encore le rire des filles
Qui assistaient au ballet des Renault 12 sur le parking
A l'intérieur, pour elles c'était moins rose
Oh cousine, tu danses ou je t'explose?
Voilà comment tout s'aggravait en un quart-d'heure
Le frère rappliquait : oh comment tu parles à ma soeur
Viens avec moi, on va se filer
Tête à tête je vais te fumer derrière les cyprès
Et tout s'arrangeait ou se réglait à la danse
L'un disait fils t'y as aucune chance
Eh les filles, mes chaussures brillent, hop un tour je vrille
Je te bousille tu te rhabilles et moi je danse le MIA
Comme les voitures c'était le défi
KUX 73 JM 120 mon petit
Du grand voyou à la plus grosse mauviette
La main sur le volant avec la moquette
Pare-soleil Pioneer sur le pare-brise arrière
Dédé et Valérie écrit en gros: sur mon père!
La bonne époque où on sortait la douze sur magic touch
On lui collait la bande rouge à la Starsky et Hutch
J'avais la nuque longue Eric aussi Malek coco
La coupe à la Marley Pascal était rasta des affros
Sur François et Joe déjà à la danse à côté d'eux
Personne ne touchait une bille
On dansait le MIA

Je danse le MIA
Hey DJ met nous donc du Funk, que je danse le MIA
Je danse le MIA
Fait pousser le Pioneer à fond qu'on danse le MIA
Je danse le MIA
Ce soir les bagues brilleront on danse le MIA
Je danse le MIA
Hey DJ met nous donc du Funk, je danse le MIA

En direct sur Radio Chacal, en duplex live avec le Starflash
Laserline Hatchin club c'est tout de suite 3, 2, 1, Dj :
Merci à toutes et à tous d'être encore avec nous ce soir
Au New starflash Lazerline Hatchin Club
Nous sommes ensemble ce soir pour une soirée de bonheur musical
Avec un grand concours de danse
De nombreux super cadeaux pour les heureux gagnants
Il y aura les T-shirt Marlboro, les autocollants Pioneer
Les caleçons JB, les peluches
à la technique c'est Michel, le light jockey c'est Momo
On monte sur les tables, on lève les bras bien haut
Allez c'est parti...

Je danse le mia
Je danse le mia

Je danse le MIA, pas de pacotille
Chemise ouverte, chaîne en or qui brille
Des gestes lents ils prenaient leur temps pour enchaîner
Les passes qu'ils avaient élaborées dans leur quartier
C'était vraiment trop beau
Un mec assurait tout le monde criait : ah oui minot
La piste s'enflammait et tous les yeux convergeaient
Les différents s'effaçaient et les rires éclataient
Beaucoup disaient que nos soirées étaient sauvages
Et qu'il fallait rentrer avec une batte ou une hache
Foutaises, c'étaient les ragots des jaloux
Et quoi qu'on en dise, nous on s'amusait beaucoup
Aujourd'hui, encore on peut entendre des filles dire
"Hayya, IAM, ils dansent le MIA"

Je danse le MIA
Hey DJ met nous donc du Funk, que je danse le MIA
Je danse le MIA
Fait pousser le Pioneer à fond qu'on danse le MIA
Je danse le MIA
Ce soir les bagues brilleront on danse le MIA
Je danse le MIA
Hey DJ met nous donc du Funk, je danse le MIA

Je danse le MIA...
"""

def wordCount(text):
    counts=defaultdict(int)
    for word in text.split():
        counts[word.lower()] +=1
    return counts

print(wordCount(bestSongInTheWorld))