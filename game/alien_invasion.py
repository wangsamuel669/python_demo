import sys
import pygame

from settings import Settings


def run_game():

    # 初始化游戏，并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # 返回一个1200 * 800 的屏幕
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    # 设置屏幕的标题
    pygame.display.set_caption("Alien Invasion")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 每次循环都重新绘制屏幕
        screen.fill(ai_settings.bg_color)
        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
