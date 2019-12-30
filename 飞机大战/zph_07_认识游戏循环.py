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

# 4.0 创建游戏时钟对象
clock = pygame.time.Clock()

# 游戏循环   --> 意味着游戏正式开始
i = 0
while True:

    # 设置屏幕刷新帧率
    clock.tick(60)
    print(i)

    i += 1
    pass

pygame.quit()