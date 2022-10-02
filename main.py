import sys
import time

import pygame                       #подключаем библиотеку pygame
from Player_class import Player     #подключаем класс Player (игрок)
from Enemy_class import Enemy       #подключаем класс Enemy (враг)
import Events                       #подключаем файл событий игры

def run():
    pygame.init()                                  #Инициализуем pygame

    screen = pygame.display.set_mode((1200, 900))  #Задаем размер игрового окна
    pygame.display.set_caption("Танчики")          #Задаем название игрового окна
    bg_color = (45, 45, 45)                        #Задаём цвет фона окна (серый)

    clock = pygame.time.Clock()                    #Создаём clock для ограничения FPS
    FPS = 500                                      #Максимальное допустимое FPS

    player = Player(screen)                        #Создаём игрока и передаём ему параметр screen
    enemy = Enemy(screen)                          #Создаём противника
    bombs = []                                     #Создаём массив снарядов

    while True:
        if player.health == 0 or enemy.health == 0: #Если у игрока или противка не осталось здоровья, то выходим из цикла
            break

        Events.events(screen, player, enemy, bombs)  #Вызываем функцию events в модуле Events
        player.update()                              #Обновляем модельку игрока
        enemy.update(player, bombs)                  #Обновляем модельку противка

        Events.update_bombs(bombs, player, enemy, screen)      #Обновляем модельки снарядов
        Events.update(screen, bg_color, player, enemy, bombs)  #Отрисосываем фон и модельки

        clock.tick(FPS)                                        #Задаём ограничение на FPS

    show_go_screen(player, enemy, screen)                      #Вызываем функцию конца игры

def show_go_screen(player, enemy, screen):                                       #Функция конца игры
    result_text = ""                                                             #создаем переменную с итоговым текстом
    if player.health == 0:                                                       #Если у игрока закончилось здоровье, то итоговый текст будет соответствующим
        result_text = "Вы проиграли. Нажмите Backspace чтобы начать заново."
    if enemy.health == 0:                                                        #Если у противника закончилось здоровье, то итоговый текст будет соответствующим
        result_text = "Вы победили. Нажмите Backspace чтобы начать заново."

    f1 = pygame.font.SysFont('couriernew', 30)                                   #Создаем шрифт для итоговой надписи
    text = f1.render(result_text, True, (255, 255, 255))                         #Задаем текс и цвет итоговой надписи

    screen.fill((0, 0, 0))                                                                   #Задаем цвет фона в окне с игрой
    screen.blit(text, (screen.get_rect().centerx - 450, screen.get_rect().centery - 40))     #Выводим итоговую надпись

    pygame.display.flip()                                                        #Обновляем игровое окно

    repeat = False                                                               #Переменная для запуска игры заново

    for i in range(30):                                                          #Заходим в цикл
        for event in pygame.event.get():                                         #Проходим циклом по событиям pygame
            if event.type == pygame.QUIT:                                        #В случае закрытия окна игры, выключаем программу полностью
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:  #Если была нажата кнопка для продолжения
                repeat = True
                break                                                             #То выходим из цикла
        if repeat:
            break
        time.sleep(0.3)                                                           #Ставим временную задержку в 0.3 секунды

    if repeat:                                                                    #Если была нажата кнопка продолжения, то перезапускаем программу
        run()

run()                              #первоначальный запуск программы