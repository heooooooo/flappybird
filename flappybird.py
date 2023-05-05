import pygame,time,random # Gọi các thư viện cần thiết
pygame.init() # Khời tạo các module của pygame

window_x = 720 # Bề ngang cửa sổ
window_y = 480 # Bề dọc cửa sổ
g=10/60 # Gia tốc rơi tự do
pos=[50,250] # Vị trí người chơi
pillar_pos1=[250,random.randrange(200, 350)] # Tọa độ cột
pillar_pos2=[400,random.randrange(200, 350)]
pillar_pos3=[550,random.randrange(200, 350)]
pillar_pos4=[700,random.randrange(200, 350)]
new=True # Biến kiểm tra đã có chướng ngại vật hay chưa
run=True # Biến chạy vòng lặp chính
score=0 # Biến tính điểm

pygame.display.set_caption('Flappy bird') # Đặt tên cửa sổ là Flappy bird
game_window = pygame.display.set_mode((window_x, window_y)) # Tạo cửa sổ có độ lớn là window_x và window_y

def pillar_draw(x,y): # Hàm vẽ các cột
    pygame.draw.rect(game_window, green, pygame.Rect(x, y, 30, 300))
    pygame.draw.rect(game_window, green, pygame.Rect(x, (y-400), 30, 300))

def pillar_pass(x1, x2, score): # Cộng điểm khi người chơi vượt qua cột
    if x1>(x2+18):
        score+=10
    return score

def check(x1,y1,x2,y2): # Kiểm tra sự kiện người chơi va vào cột
    return ((x1 in range (x2,x2+20)) and (y1>=y2 or y1<=(y2-100))) or (y1>=480 or y1<=0)

def show_score(choice ,color, font, size): # Hàm tính điểm
    score_font = pygame.font.SysFont(font, size) # Phông chữ
    score_surface = score_font.render('Score : ' + str(score), True, color) # In ra điểm
    score_rect = score_surface.get_rect() 
    if choice == 1:
        score_rect.midtop = (window_x/10, 15)
    else:
        score_rect.midtop = (window_x/2, window_y/1.25)
    game_window.blit(score_surface, score_rect) # Tạo chỗ để in ra điểm

def game_over(): # Hàm khi thua game
    my_font = pygame.font.SysFont('times new roman', 50) # Phông chữ
    game_over_surface = my_font.render('BẠN ĐÃ THUA', True, red)  # tương tự như in điểm
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(3)

#Khời tạo các màu cơ bản
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Biến số khung hình trên giây
fps_controller = pygame.time.Clock()

while run: # Vòng lặp chính của game
    # Nhận sự kiện nhấn phím
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Sự kiện để dừng vòng lặp và tắt chương trình
            run = False
    keys = pygame.key.get_pressed() # Danh sách lưu trữ các phím đã nhấn
    if keys[pygame.K_ESCAPE]:
        pygame.event.post(pygame.event.Event(pygame.QUIT))
    if keys[pygame.K_UP]: # Nhấn phím mũi tên lên
        vely=0 # Đặt vận tốc rơi tự do về 0
        vely-=3.5 # Truyền cho vật vận tốc hướng lên
        new=False # Biến kiểm tra đã bắt đầu hay chưa
    

    if not new: # Nếu đã bắt đầu thì thực hiện các câu lệnh
        vely+=g # Tăng dần vận tốc rơi tự do theo gia tốc rơi tự do
        pillar_pos1[0]-=2 # Vị trí của các cột được di chuyển lại gần người chơi phương Ox
        pillar_pos2[0]-=2
        pillar_pos3[0]-=2
        pillar_pos4[0]-=2
        pos[1]+=vely # Vật rơi dần theo phương Oy với vận tốc vely

    if pillar_pos1[0]<30: # Kiểm tra xem người chơi đã vượt qua cột hay chưa
        # nếu rồi thì đặt lại vị trí ngẫu nhiên cho 2 cột
        pillar_pos1=[600,random.randrange(200, 350)]
    if pillar_pos2[0]<30:
        pillar_pos2=[600,random.randrange(200, 350)]
    if pillar_pos3[0]<30:
        pillar_pos3=[600,random.randrange(200, 350)]
    if pillar_pos4[0]<30:
        pillar_pos4=[600,random.randrange(200, 350)]

    if check(pos[0],pos[1],pillar_pos1[0],pillar_pos1[1]) or check(pos[0],pos[1],pillar_pos2[0],pillar_pos2[1]) or check(pos[0],pos[1],pillar_pos3[0],pillar_pos3[1]) or check(pos[0],pos[1],pillar_pos4[0],pillar_pos4[1]):
        # Kiểm tra điều kiện thua game nếu chạm trúng cột hoặc ra khỏi màn hình thì thua
        game_over() # gọi hàm thua game
        # Trả lại vị trí các cột
        pillar_pos1=[250,random.randrange(200, 350)]
        pillar_pos2=[400,random.randrange(200, 350)]
        pillar_pos3=[550,random.randrange(200, 350)]
        pillar_pos4=[700,random.randrange(200, 350)]
        score=0 # đặt lại điểm thành 0
        vely=0 # Đặt lại vận tốc rơi bằng 0
        new=True # Đưa game về trạng thái chưa bắt đầu
        pos[0],pos[1]=50,250 # Đặt lại vị trí người chơi

    score=pillar_pass(pos[0], pillar_pos1[0], score) # Cộng điểm
    score=pillar_pass(pos[0], pillar_pos2[0], score)
    score=pillar_pass(pos[0], pillar_pos3[0], score)
    score=pillar_pass(pos[0], pillar_pos4[0], score)

    game_window.fill(black) # Đặt màu nền của game là màu đen
    pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    # Vẽ người chơi
    pillar_draw(pillar_pos1[0], pillar_pos1[1])
    pillar_draw(pillar_pos2[0], pillar_pos2[1])
    pillar_draw(pillar_pos3[0], pillar_pos3[1])
    pillar_draw(pillar_pos4[0], pillar_pos4[1])
    show_score(1, white, 'consolas', 20)
    # Gọi hàm in ra điểm
    pygame.display.update() # Cập nhật lại màn hình mỗi lần hoàn thành vòng lặp
    fps_controller.tick(60) # Đặt khung hình mỗi giây là 60
