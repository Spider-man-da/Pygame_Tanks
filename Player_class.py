import pygame

class Player():

    def __init__(self, screen):                                    #Инициализируем класс игрока
        self.screen = screen                                       #Записываем переменную экрана
        self.image = pygame.image.load('images/Player_up.png')     #Загружаем модельку танка игрока

        #Задаем размеры прямоугольников модельки и экрана
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Задаем начальную позицию модельки игрока
        self.rect.centerx = self.screen_rect.centerx + 450
        self.rect.centery = self.screen_rect.centery + 300

        #Задаем координаты центра модельки
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        #Задаем текущее направление, куда смотрит моделька игрока (u = up = вверх)
        self.direction_now = "u"

        #Движение
        self.direction = [False] * 4  #Задаем массив направлений в котором 0 элемент- Вверх, 1 - вниз, 2 - влево, 3 - вправо
        self.speed = 1.2222222        #Скорость модельки

        # Здоровье
        self.health = 40

    def output(self): #Функция отрисовки модельки игрока в игровом окне
        self.screen.blit(self.image, self.rect)

    def rotation(self, direction):  #Функция поворота модельки игрока
        if direction == "u":                                          #Если текущее направление - вверх, то загружаем соответствующую модельку
            self.image = pygame.image.load('images/Player_up.png')
        if direction == "d":                                          #И так по аналогии с каждым направлением
            self.image = pygame.image.load('images/Player_down.png')
        if direction == "l":
            self.image = pygame.image.load('images/Player_left.png')
        if direction == "r":
            self.image = pygame.image.load('images/Player_right.png')

    def update(self): #Функция обновления модельки игрока
        if self.direction[0] and self.rect.top > 0:          #Если игрок нажал кнопку "вверх" и моделька игрока не дошла до пределов экрана
            self.direction_now = "u"                         #То задаем текущее направление движения игрока как "вверх"
            self.rotation(self.direction_now)                #Вызываем функцию поворота модельки
            self.centery -= self.speed                       #И перемещаем модельку вверх на единицу, равную скорости модельки

        # И так по аналогии с каждым направлением
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

        #Задаем центр модельки равным новым координатам
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery