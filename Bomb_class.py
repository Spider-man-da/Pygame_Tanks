import pygame

class Bomb():

    def __init__(self, screen, is_player_fire, player, enemy):      #Инициализируем класс снаряда (сделан по аналогии с классами игрока и противника)
        self.screen = screen
        self.is_player_fire = is_player_fire

        self.image = pygame.image.load('images/bullet.png')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        if self.is_player_fire:                              #Если данный снаряд выпустил игрок
            self.rect.centerx = player.rect.centerx          #То задаем центр снаряда равным центру игрока по х
            self.direction = player.direction_now            #направление движения снаряда задаем как направление движения игрока в момент выстрела

            if self.direction == "u":                        #Если это направление - вверх, то верхнюю часть снаряда привязываем к верхней части игрока
                self.rect.top = player.rect.top
            if self.direction == "d":
                self.rect.bottom = player.rect.bottom
            if self.direction == "l":
                self.rect.midleft = player.rect.midleft
            if self.direction == "r":
                self.rect.midright = player.rect.midright  #И так далее по аналогии
        else:
            self.rect.centerx = enemy.rect.centerx
            self.direction = enemy.direction_now

            if self.direction == "u":
                self.rect.top = enemy.rect.top
            if self.direction == "d":
                self.rect.bottom = enemy.rect.bottom
            if self.direction == "l":
                self.rect.midleft = enemy.rect.midleft
            if self.direction == "r":
                self.rect.midright = enemy.rect.midright

        #Координаты снаряда
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.speed = 2 #Скорость снаряда

    def update(self):            #Перемещение пули
        if self.direction == "u":            #Вверх
            self.y -= self.speed
        elif self.direction == "d":          #Вниз
            self.y += self.speed
        elif self.direction == "l":          #Влево
            self.x -= self.speed
        elif self.direction == "r":          #Вправо
            self.x += self.speed

        self.rect.x = self.x
        self.rect.y = self.y

    def output(self):
        self.screen.blit(self.image, self.rect)