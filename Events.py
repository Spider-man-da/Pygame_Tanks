import math, pygame, sys
from Bomb_class import Bomb

def events(screen, player, enemy, bombs):              #функция обработки событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:            #Если какая-то кнопка была нажата
            if event.key == pygame.K_UP:              #И эта кнопка 'стрелка вверх'
                player.direction[0] = True            #То задаем направление игрока вверх равное True

            elif event.key == pygame.K_DOWN:          #Если эта кнопка 'стрелка вниз'
                player.direction[1] = True            #То задаем направление игрока вниз равное True

            elif event.key == pygame.K_LEFT:          #По аналогии
                player.direction[2] = True

            elif event.key == pygame.K_RIGHT:         #По аналогии
                player.direction[3] = True

            elif event.key == pygame.K_SPACE:                   #Если был нажат пробел
                new_bomb = Bomb(screen, True, player, enemy)    #То создаем объект класса Bomb
                bombs.append(new_bomb)                          #И добавляем в массив снарядов

        elif event.type == pygame.KEYUP:              #Если какая-то кнопка была отжата
            if event.key == pygame.K_UP:              #И эта кнопка 'стрелка вверх'
                player.direction[0] = False           #То направление игрока вверх считаем не действительным как False

            elif event.key == pygame.K_DOWN:          #По аналогии
                player.direction[1] = False

            elif event.key == pygame.K_LEFT:          #По аналогии
                player.direction[2] = False

            elif event.key == pygame.K_RIGHT:         #По аналогии
                player.direction[3] = False

def update(screen, bg_color, player, enemy, bombs):
    screen.fill(bg_color)                                                             #Задаем цвет фона игрового окна (серым цветом)

    f1 = pygame.font.SysFont('couriernew', 36)                                        #Создаем шрифт для надписи о здоровье игрока
    text = f1.render("Здоровье: " + str(player.health), True, (255, 255, 255))        #Задаем текс и цвет надписи о здоровье
    screen.blit(text, (10, 10))                                                       #Выводим на экран

    text = f1.render("Здоровье врага: " + str(enemy.health), True, (255, 255, 255))   #По аналогии задаем параметры надписи о здоровье противника
    screen.blit(text, (10, 50))

    for bomb in bombs:            #Отрисовываем все снаряды из массива снарядов
        bomb.output()

    player.output()               #Отрисовываем модельку игрока
    enemy.output()                #Отрисовываем модельку противника

    pygame.display.flip()         #Обновляем игровой экран

def hit(bomb, player, enemy):         #Функция для определения - попал снаряд или нет
    if bomb.is_player_fire:           #Если бомба выпущена игроком, то координатами цели будут координаты противника
        target_x = enemy.centerx
        target_y = enemy.centery
    else:
        target_x = player.centerx     #Если бомба выпущена противников, то координатами цели будут координаты игрока
        target_y = player.centery

    distance = math.sqrt(pow((bomb.x - target_x), 2) + pow((bomb.y - target_y), 2))  #Вычисляем расстояние между снарядом и целью
    radius_porajenia = 50                                                            #Задаем радиус допустимого попадения

    if distance <= radius_porajenia:         #Если дистанция меньше или равна радиусу допустимого попадения
        if bomb.is_player_fire:              #И выпустил снаряд игрок
            enemy.health -= 1                #То противнику отнимаем одно очко здоровья
        else:
            player.health -= 1               #Если снаряд выпустил противник, то отнимаем одно очко здоровья у игрока
        return True

    return False

def update_bombs(bombs, player, enemy, screen):     #функция для обновления снарядов
    for bomb in bombs:
        if (bomb.rect.bottom < 0) or (bomb.rect.right < 0) or (bomb.rect.left > screen.get_rect().right) or (bomb.rect.top > screen.get_rect().bottom) or hit(bomb, player, enemy):
            #Если снаряд выходит за пределы окна, то удаляем его из массива снарядов
            bombs.remove(bomb)
        else:
            #А если снаряд находится в пределах игрового окна, то обновляем его модельку
            bomb.update()