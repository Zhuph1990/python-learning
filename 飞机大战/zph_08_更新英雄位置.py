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

# 定义react记录飞机的初始位置
hero_reac = pygame.Rect(150, 300, 102, 126)
# 游戏循环   --> 意味着游戏正式开始

while True:
    
    # 设置屏幕刷新帧率
    clock.tick(60)

    # 修改飞机位置
    hero_reac.y -= 1

    # 调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_reac)

    # 调用update方法更新显示
    pygame.display.update()

    pass

pygame.quit()