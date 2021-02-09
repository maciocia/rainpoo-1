from p5 import core
from p5.POO.Agario import creep
from p5.POO.Agario.bille import Bille
from p5.POO.Agario.creep import Creep
from p5.POO.Agario.player import Player
"variable globals initialisation "

playeur1 = None
creep = []
bille1 = None


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]

    global playeur1, creep1
    playeur1 = Player()

    for i in range(0, 100):
        creep.append(Creep())


    print("Setup END-----------")


def run():
    for c in creep:
        c.afficher(core)
    print("run")
    playeur1.afficher(core)
    if core.getMouseLeftClick() is not None:
        playeur1.deplacer(core.getMouseLeftClick())
    "on donne une valeur a playeur1"



if __name__ == "__main__":
    nom_joueur = Player()
    creep1 = Creep()
    bille1 = Bille()

core.main(setup, run)
