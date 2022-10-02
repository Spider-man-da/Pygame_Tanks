import random, pygame
from Bomb_class import Bomb

class Enemy():  #класс противника реализован по аналогии с классом игрока, за исключением некоторых моментов
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/Enemy_down.png')

        #Задаем размеры
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Начальная позиция
        self.rect.centerx = self.screen_rect.centerx - 450
        self.rect.centery = self.screen_rect.centery - 300

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.direction_now = "d"

        #Движение
        self.direction = [False] * 4  # Вверх, вниз, влево, вправо
        self.speed = 0.3
        self.health = 15

    def output(self): #отрисовка
        self.screen.blit(self.image, self.rect)

    def rotation(self, direction):
        if direction == "u":
            self.image = pygame.image.load('images/Enemy_up.png')
        if direction == "d":
            self.image = pygame.image.load('images/Enemy_down.png')
        if direction == "l":
            self.image = pygame.image.load('images/Enemy_left.png')
        if direction == "r":
            self.image = pygame.image.load('images/Enemy_right.png')

    def fire(self, player, bombs):
        new_bomb = Bomb(self.screen, False, player, self)
        bombs.append(new_bomb)

    def Intelligence(self, player, bombs):
        difference_x = player.centerx - self.centerx  #Функция находит разницу по х и у между игроком и противником
        difference_y = player.centery - self.centery

        pogreshost = 1                  #погрешность в определении прямой линии меж противником и игроком
        self.direction = [False] * 4    #Обнулям все направления движения на данный момент

        if abs(difference_x) <= pogreshost or abs(difference_y) <= pogreshost:   #Если модуль разности одной из осей меньше или равна подгрешности
            if abs(difference_x) > abs(difference_y):                #И модуль разности по х больше модуля разности по у
                if difference_x < 0:  # Лево                      #И разность по х отрицательна, то моделька должна повернуть влево
                    self.direction_now = "l"
                    self.rotation(self.direction_now)
                if difference_x > 0:
                    self.direction_now = "r"
                    self.rotation(self.direction_now)
            else:
                if difference_y > 0:  # вниз                      #И так по аналогии
                    self.direction_now = "d"
                    self.rotation(self.direction_now)
                if difference_y < 0:
                    self.direction_now = "u"
                    self.rotation(self.direction_now)
            if random.randint(0, 150) == 0:
                self.fire(player, bombs)

        elif abs(difference_x) < abs(difference_y):              #Если же противник не близок к игроку хотя бы по одной оси
            if difference_x < 0:  # Лево
                self.direction[2] = True                         #То он должен ехать влево, если ещё его разность по x меньше 0
            if difference_x > 0:
                self.direction[3] = True                         #И так по аналогии
        else:
            if difference_y > 0:  # вниз
                self.direction[1] = True
            if difference_y < 0:
                self.direction[0] = True

    def update(self, player, bombs):
        self.Intelligence(player, bombs)  #Вызываем функцию "Интеллекта" противника

        if self.direction[0] and self.rect.top > 0:
            self.direction_now = "u"
            self.rotation(self.direction_now)
            self.centery -= self.speed

        elif self.direction[1] and self.rect.bottom < self.screen_rect.bottom:
            self.direction_now = "d"
            self.rotation(self.direction_now)
            self.centery += self.speed

        elif self.direction[2] and self.rect.left > 0:
            self.direction_now = "l"
            self.rotation(self.direction_now)
            self.centerx -= self.speed

        elif self.direction[3] and self.rect.right < self.screen_rect.right:
            self.direction_now = "r"
            self.rotation(self.direction_now)
            self.centerx += self.speed

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery