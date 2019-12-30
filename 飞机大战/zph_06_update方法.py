import pygame

pygame.init()

# 1.0 创建游戏主窗口

screen = pygame.display.set_mode((480, 700))

# 2.0 绘制背景图像

bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))

hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))

# 3.0 更新显示
pygame.display.update()

# 游戏循环
while True:
    pass

pygame.quit()