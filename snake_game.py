import pygame
import random

# inisialiasi pgame
pygame.init()

# ukuran layar
lebar = 600
tinggi = 400
layar = pygame.display.set_mode((lebar, tinggi))
pygame.display.set_caption("snack game sederhana")

# warna
putih = (255, 255, 255)
hitam  = (0, 0,0)
merah = (255, 0, 0)
hijau = (0, 255, 0)

#ukuran blok ular
blok = 10
clok = pygame.time.Clock()
kecepatan = 10

#font
font = pygame.font.SysFont(None, 30)

def tampil_score(score):
    teks = font.render(f"score: {score}", True, hitam)
    layar.blit(teks, [10, 10])

def game_loop():
    game_over = False
    game_close = False

    # posisi awal ular
    x = lebar // 2
    y = tinggi // 2

    # arah awal ular
    x_change = blok
    y_change = 0

    snake = []
    panjang_snake = 1

    # makanan
    food_x = round(random.randrange(0, lebar - blok) / 10.0) * 10.0
    food_y = round(random.randrange(0, tinggi - blok) / 10.0) * 10.0

    while not game_over:
        while game_close:
            layar.fill(putih)
            teks = font.render(" kamu kalah! tekan Q untuk keluar atau C untuk main lagi", True, merah)
            layar.blit(teks, [20,tinggi / 2])
            pygame.display.update()

            pygame.event.pump()
            for event in pygame.event.get():
                if event .type == pygame. KEYDOWN:
                    if event.key == pygame.k_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.k_c:
                        game_loop()
    
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x_change = -blok
            y_change = 0
        elif keys[pygame.K_RIGHT]:
            x_change = blok
            y_change = 0
        elif keys[pygame.K_UP]:
            y_change = -blok
            x_change = 0
        elif keys[pygame.K_DOWN]:
            y_change = blok
            x_change = 0

        # cek tarak dinding
        if x >= lebar or x < 0 or y >= tinggi or y < 0:
            game_close = True
        x += x_change
        y += y_change
        layar.fill(putih)

        # gambar makanan
        pygame.draw.rect(layar, hijau, (int(food_x), int(food_y), blok, blok))

        #ular
        kepala = []
        kepala.append(x)
        kepala.append(y)
        snake.append(kepala)
        if len(snake) > panjang_snake:
            del snake[0]            
        
        # cek tabrak diri sendiri
        for bagian in snake[:-1]:
            if bagian == kepala:
                game_close = True

        for bagian in snake:
            pygame.draw.rect(layar, hitam, [bagian[0], bagian[1], blok, blok])
        tampil_score(panjang_snake - 1)
        pygame.display.update()

        # cek makan
        if abs(x - food_x) < blok and abs(y - food_y) < blok:
            food_x = round(random.randrange(0, lebar - blok) / 10.0) * 10.0
            food_y = round(random.randrange(0, tinggi - blok) / 10.0) * 10.0
            panjang_snake += 1

        clok.tick(kecepatan)

    pygame.quit()
    quit()

game_loop()
