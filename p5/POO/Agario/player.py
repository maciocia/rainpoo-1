import pygame
from pygame.math import Vector3, Vector2

from p5 import core


class Player() :
    def __init__(self):
        self.size = 10
        self.shape = "rond"

        self.couleur = Vector3(255,0,0)
        self.direction = Vector2(0,0)
        self.position = Vector2(0,0)

    def manger (self) :
        pass
    def mourir (self) :
        pass
    def deplacer (self, position) :
        self.position.x = position[0]
        self.position.y = position[1]
        pass
    def afficher (self,core) :

        if self.shape == "rond":
            pygame.draw.circle(core.screen, (int(self.couleur.x), int(self.couleur.y), int(self.couleur.z)), (int(self.position.x), int(self.position.y)),self.size)
