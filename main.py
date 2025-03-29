import asyncio
import pygame
import random
import sys
async def main():
# 初始化 pygame
    pygame.init()

# 設定遊戲視窗大小
    WIDTH, HEIGHT = 500, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("躲避遊戲")

# 顏色設定
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

# 玩家設定
    player_size = 50
    player_x = WIDTH // 2 - player_size // 2
    player_y = HEIGHT - 70
    player_speed = 7

# 障礙物設定
    obstacle_size = 50
    obstacle_x = random.randint(0, WIDTH - obstacle_size)
    obstacle_y = -50
    obstacle_speed = 5

# 遊戲變數
    running = True
    score = 0
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

# 遊戲主迴圈
    while running:
        screen.fill(WHITE)
    
    # 事件監聽
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    # 玩家控制
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
            player_x += player_speed
    
    # 更新障礙物位置
        obstacle_y += obstacle_speed
        if obstacle_y > HEIGHT:
            obstacle_y = -50
            obstacle_x = random.randint(0, WIDTH - obstacle_size)
            score += 1
    
    # 碰撞檢測
        if (player_x < obstacle_x + obstacle_size and
            player_x + player_size > obstacle_x and
            player_y < obstacle_y + obstacle_size and
            player_y + player_size > obstacle_y):
            running = False  # 結束遊戲
    
    # 畫出玩家和障礙物
        pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
        pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, obstacle_size, obstacle_size))
    
    # 顯示分數
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
    
        pygame.display.flip()
        clock.tick(30)
        await pygame.sleep(0)
    pygame.quit()
    sys.exit()
asyncio.run(main())