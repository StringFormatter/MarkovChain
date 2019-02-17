import pygame

def main():

    pygame.init()
    icon = pygame.image.load("AAMarkovicon.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Markov Dataset Creator")

    screen = pygame.display.set_mode((1920,1080))

    running = True

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()
