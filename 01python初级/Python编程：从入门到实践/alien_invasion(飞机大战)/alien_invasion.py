# sys实现退出游戏功能
import sys
# pygame包含开发游戏所需的功能
import pygame
# 导入Settings
from settings import Settings
# 导入ship
from ship import Ship
# 导入game_functions
import game_functions as gf
# 将子弹存储到编组中
from pygame.sprite import Group
# 导入统计信息
from game_stats import GameStats
# 导入按钮
from button import Button
# 导入记分牌
from scoreboard import Scoreboard



def run_game():
    # 初始化pygame,设置和屏幕对象
    pygame.init()# 初始化背景设置
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    # 设置游戏名称(标题)
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")


    #
    #  创建一个名为screen的游戏显示(display)窗口,设置样式(set_mode)为宽1200像素,高800像素
    #  实参是一个Tuple
    #  screen = pygame.display.set_mode((1200,800))
    #  pygame.display.set_caption("Alien Invasion")
    #  设置背景色
    #  在pygame中,颜色是以RGB值指定的
    #  bg_color = (230, 230, 230)
    #

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建记分牌
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船,创建一个用于存储子弹的编组, 创建一个alien编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建alien群
    gf.create_fleet(ai_settings, screen, ship, aliens)




    while True:
        # 监听事件并响应
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            # 更新飞船位置
            ship.update()
            # 更新子弹位置
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # 更新外星人位置
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
            # 更新屏幕显示
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)



    #
    # # 开始游戏的主循环
    # while True:
    #     # 监视键盘和鼠标
    #     # 事件循环-->侦听事件
    #     # pygame.event.get(): 访问侦听到的事件
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             sys.exit()
    #
    #
    #     screen.fill(ai_settings.bg_color)
    #     ship.blitme()
    #
    #     # 每次循环都重绘屏幕
    #     # screen.fill(color): 用背景色填充屏幕
    #     # 这个方法只接收一个实参-->一种颜色
    #     # screen.fill(bg_color)
    #
    #     # 让最近绘制的屏幕可见
    #     # flip: 快速翻转
    #     # 不断更新并显示屏幕, 显示元素的新位置, 并在原来的位置隐藏元素
    #     pygame.display.flip()
    #

run_game()