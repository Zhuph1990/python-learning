import pygame

pygame.init()

# 创建游戏主窗口

screen = pygame.display.set_mode((480, 700))

# 绘制背景图像

# 1> 加载图像  加载到内存
bg = pygame.image.load("./images/background.png")

# 2> 绘制在屏幕
screen.blit(bg, (0, 0))

# 3> 更新显示
pygame.display.update()

# 游戏循环
while True:
    pass

pygame.quit()