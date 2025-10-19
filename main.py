import random
import pygame


# ------------------- BUTTON CLASS -------------------
class Button:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def clicked(self, pos):
        return self.rect.collidepoint(pos)


# ------------------- MAIN GAME CLASS -------------------
class RpsGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((960, 640))
        pygame.display.set_caption("RPS Smasher")

        # Load images
        self.bg = pygame.image.load("background.jpg").convert()
        self.r_btn = pygame.image.load("r_button.png").convert_alpha()
        self.p_btn = pygame.image.load("p_button.png").convert_alpha()
        self.s_btn = pygame.image.load("s_button.png").convert_alpha()

        self.choose_rock = pygame.image.load("rock.png").convert_alpha()
        self.choose_paper = pygame.image.load("paper.png").convert_alpha()
        self.choose_scissors = pygame.image.load("scissors.png").convert_alpha()

        # Buttons for Rock, Paper, Scissors
        self.rock_btn = Button(20, 500, 300, 100)
        self.paper_btn = Button(330, 500, 300, 100)
        self.scissors_btn = Button(640, 500, 300, 100)

        # Game variables
        self.font = pygame.font.Font('Splatch.ttf', 80)
        self.text = self.font.render("", True, (255, 255, 255))
        self.pl_score = 0
        self.pc_score = 0
        self.p_option = None
        self.pc_random_choice = None

    # ------------------- PLAYER CHOICE -------------------
    def player_choice(self, pos):
        if self.rock_btn.clicked(pos):
            self.p_option = "rock"
            self.screen.blit(self.choose_rock, (120, 200))
        elif self.paper_btn.clicked(pos):
            self.p_option = "paper"
            self.screen.blit(self.choose_paper, (120, 200))
        elif self.scissors_btn.clicked(pos):
            self.p_option = "scissors"
            self.screen.blit(self.choose_scissors, (120, 200))
        return self.p_option

    # ------------------- COMPUTER CHOICE -------------------
    def computer_choice(self):
        options = ["rock", "paper", "scissors"]
        self.pc_random_choice = random.choice(options)

        if self.pc_random_choice == "rock":
            choice_img = self.choose_rock
        elif self.pc_random_choice == "paper":
            choice_img = self.choose_paper
        else:
            choice_img = self.choose_scissors

        self.screen.blit(choice_img, (600, 200))
        return self.pc_random_choice

    # ------------------- SCORE CALCULATION -------------------
    def calculate_scores(self):
        pl = self.p_option
        pc = self.pc_random_choice

        if not pl or not pc:
            return

        if pl == pc:
            return  # Draw
        elif (pl == "rock" and pc == "scissors") or \
             (pl == "paper" and pc == "rock") or \
             (pl == "scissors" and pc == "paper"):
            self.pl_score += 1
        else:
            self.pc_score += 1

    # ------------------- RESET IMAGES -------------------
    def reset_screen(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.r_btn, (20, 500))
        self.screen.blit(self.p_btn, (330, 500))
        self.screen.blit(self.s_btn, (640, 500))
        self.text = self.font.render(f"{self.pl_score} : {self.pc_score}", True, (255, 255, 255))
        self.screen.blit(self.text, (400, 20))
        pygame.display.flip()

    # ------------------- MAIN GAME LOOP -------------------
    def game_loop(self):
        clock = pygame.time.Clock()
        run = True

        while run:
            self.reset_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.rock_btn.clicked(pos) or self.paper_btn.clicked(pos) or self.scissors_btn.clicked(pos):
                        self.reset_screen()
                        self.player_choice(pos)
                        self.computer_choice()
                        self.calculate_scores()
                        pygame.display.flip()
                        pygame.time.wait(1000)  # Pause briefly to show result

            clock.tick(30)
        pygame.quit()


# ------------------- RUN GAME -------------------
if __name__ == "__main__":
    game = RpsGame()
    game.game_loop()
