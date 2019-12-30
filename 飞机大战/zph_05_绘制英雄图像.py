import pygame

pygame.init()

# 1.0 创建游戏主窗口

screen = pygame.display.set_mode((480, 700))

# 2.0 绘制背景图像

# 1> 加载图像  加载到内存
bg = pygame.image.load("./images/background.png")

# 2> 绘制在屏幕
screen.blit(bg, (0, 0))

# 3> 更新显示
pygame.display.update()


# 3.0 绘制英雄图像

# 1> 加载图像
hero = pygame.image.load("./images/me1.png")

# 2> 绘制在屏幕
screen.blit(hero, (200, 500))

# 3> 更新显示
pygame.display.update()


# 游戏循环
while True:
    pass

pygame.quit()