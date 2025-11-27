
import pygame
import random
import back_SZN

pygame.init()

width = 400
height = 600
gravitacio = 0.4
gyorsulas = 11

highscoreFile = "highscore.txt"
highscore = back_SZN.highscoreLoad(highscoreFile)

root = pygame.display.set_mode((width, height))
root.fill(('lightblue'))
pygame.display.set_caption('app')
clock = pygame.time.Clock()

fontStart = pygame.font.SysFont('comicsans', 30)
fontScore = pygame.font.SysFont('arial', 24)

startText = fontStart.render("START", True, (0, 0, 0))
startRect = startText.get_rect(center=(width // 2, height // 2))

kiemelesMeret = 1.0
kiemelesSeb = 0.01
kiemelesIrany = 1
kiemeles = False

def reset():
    deszkak = back_SZN.deszkaGeneralas(width, height, 8)
    elsoDeszka = deszkak[0]
    jatekos = back_SZN.Jatekos_SZN(elsoDeszka.pozX, elsoDeszka.pozY - 40)
    return jatekos, deszkak, 0, True

startButton = True
jatekos = None
deszkak = []
score = 0
running = False

def scoreHozzaadas_SZN(value):
    global score
    score += int(value * 0.2)
    if score <= 0:
        score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if startButton:
                if startRect.collidepoint(event.pos):
                    jatekos, deszkak, score, running = reset()
                    startButton = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jatekos.setIrany(-1)
            if event.key == pygame.K_RIGHT:
                jatekos.setIrany(1)
            if not running and event.key == pygame.K_SPACE:
                jatekos, deszkak, score, running = reset()

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                jatekos.setIrany(0)

    root.fill(('lightblue'))

    egerPoz = pygame.mouse.get_pos()
    kiemeles = startRect.collidepoint(egerPoz)
    if kiemeles:
        kiemelesMeret += kiemelesSeb * kiemelesIrany
        if kiemelesMeret > 1.2:
            kiemelesIrany = -1
        elif kiemelesMeret < 1.0:
            kiemelesIrany = 1
    else:
        kiemelesMeret = 1.0

    if startButton:
        scaledFont = pygame.font.SysFont('comicsans', int(30 * kiemelesMeret))
        startText = scaledFont.render("START", True, (0, 0, 0))
        startRect = startText.get_rect(center=(width // 2, 200))
        root.blit(startText, startRect)

        iranyitasText = fontStart.render("Iranyitás", True, (255, 255, 255))
        iranyitasBalraText = fontScore.render("Balra    ←", True, (255, 255, 255))
        iranyitasJobbraText = fontScore.render("Jobbra  →", True, (255, 255, 255))
        root.blit(iranyitasText, (130, 350))
        root.blit(iranyitasBalraText, (150, 400))
        root.blit(iranyitasJobbraText, (150, 430))

        pygame.display.update()
        clock.tick(60)
        continue

    if running:
        elozoPozY = jatekos.pozY
        jatekos.mozgas(gravitacio, width, height)

        if jatekos.fSeb > 0:
            for deszka in deszkak:
                if elozoPozY + jatekos.size / 2 <= deszka.pozY <= jatekos.utkozes():
                    if deszka.pozX - deszka.width /2 <= jatekos.pozX <= deszka.pozX + deszka.width / 2:
                        jatekos.fSeb = -gyorsulas
                        break

        if jatekos.pozY < height / 2:
            y = height / 2 - jatekos.pozY
            jatekos.pozY = height / 2

            for deszka in deszkak:
                deszka.mozgas(y)

            scoreHozzaadas_SZN(y)

        lista = []
        for deszka in deszkak:
            if deszka.pozY - deszka.height / 2 > height:
                deszkaSzelesseg = random.choice([40, 70, 90])
                x = random.randint(deszkaSzelesseg // 2, width - deszkaSzelesseg // 2)
                random.randrange(-120, -40)
                lista.append(back_SZN.Deszka(x, y, deszkaSzelesseg))
                scoreHozzaadas_SZN(2)
            else:
                lista.append(deszka)

        deszkak = lista

        if jatekos.pozY - jatekos.size / 2 > height:
            running = False
            if score > highscore:
                highscore = score
                back_SZN.highscoreSave(highscoreFile, highscore)

    for deszka in deszkak:
        deszka.rajzol(root)

    jatekos.rajzol(root)

    textScore = fontScore.render(f"Score: {score}", True, (0, 0, 0))
    root.blit(textScore, (10, 10))

    textHighscore = fontScore.render(f"High Score: {highscore}", True, (0, 0, 0))
    root.blit(textHighscore, (width - textHighscore.get_width() - 10, 10))

    if not running:
        vegeText1 = fontStart.render("Vesztettél!", True, (0, 0, 0))
        vegeText2 = fontStart.render("Space: új játék", True, (0, 0, 0))
        root.blit(vegeText2, (90, height / 2))
        root.blit(vegeText1, (125, height / 2 - vegeText1.get_height()))

    pygame.display.update()
    clock.tick(60)

