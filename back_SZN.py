import pygame
import random

class Jatekos_SZN():
    def __init__(self, x, y):
        self.size = 30
        self.pozX = x
        self.pozY = y
        self.vSeb = 0
        self.fSeb = 0

    def setIrany(self, irany):
        self.vSeb = irany * 6

    def rajzol(self, root):
        pygame.draw.circle(root, ("darkgreen"), (self.pozX, self.pozY), self.size // 2)

    def mozgas(self, gravitacio, width, height):
        self.fSeb += gravitacio
        self.pozX += self.vSeb
        self.pozY += self.fSeb

        if self.pozX > width + self.size / 2:
            self.pozX = -self.size / 2
        if self.pozX < -self.size / 2:
            self.pozX = width + self.size / 2

    def utkozes(self):
        return self.pozY + self.size / 2

class Deszka():
    def __init__(self, x, y, width = 80, height = 12):
        self.pozX = x
        self.pozY = y
        self.width = width
        self.height = height

    def mozgas(self, y):
        self.pozY += y

    def rajzol(self, screen):
        pygame.draw.rect(screen, ("brown"), (self.pozX - self.width / 2, self.pozY - self.height / 2, self.width, self.height))

def DeszkaGeneralas(width, height, db):
    deszkak = []
    y = height - 40


    for _ in range(db):
        deszkaSzelesseg = random.choice([40, 70, 90])
        x = random.randint(deszkaSzelesseg // 2, width - deszkaSzelesseg // 2)

        minTav = 60
        maxTav = 120
        eltolas = random.randint(minTav, maxTav)

        deszkak.append(Deszka(x, y, deszkaSzelesseg))
        y -= eltolas

    return deszkak

def highscoreLoad(fajlnev):
    try:
        with open(fajlnev, "r", encoding="utf-8") as f:
            return int(f.read().strip())
    except:
        return 0

def highscoreSave(fajlnev, pont):
    try:
        with open(fajlnev, "w", encoding="utf-8") as f:
            f.write(str(int(pont)))
    except:
        pass