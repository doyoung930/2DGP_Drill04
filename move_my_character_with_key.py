from pico2d import *
from PIL import Image

TUK_WIDTH, TUK_HEIGHT = 1280, 720
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('character2.png')
mouse = load_image('hand_arrow.png')
im = Image.open('character2.png')
width, height = im.size
print (width, height)

running = True
frame = 0

def handle_events():
    global running, dir
    global x, y
    global c_x, c_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                dir = 1
            elif event.key == SDLK_RIGHT:
                dir = 2
            elif event.key == SDLK_UP:
                dir = 3
            elif event.key == SDLK_DOWN:
                dir = 4

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                dir = 0
            elif event.key == SDLK_RIGHT:
                dir = 0
            elif event.key == SDLK_DOWN:
                dir = 0
            elif event.key == SDLK_UP:
                dir = 0


x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
c_x, c_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
hide_cursor()
dir = 0
while running:
    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    mouse.draw(x, y)
    if dir == 0:
        character.clip_draw(frame * 64, 192, 64, 64, c_x, c_y)
    elif dir == 1:
        c_x -= 10
        if c_x < 0:  # 화면 왼쪽으로 나가는 경우
            c_x = 0
        character.clip_draw(frame * 64, 128, 64, 64, c_x, c_y)
    elif dir == 2:
        c_x += 10
        if c_x > TUK_WIDTH:  # 화면 오른쪽으로 나가는 경우
            c_x = TUK_WIDTH
        character.clip_draw(frame * 64, 64, 64, 64, c_x, c_y)
    elif dir == 3:
        c_y += 10
        if c_y > TUK_HEIGHT:  # 화면 위로 나가는 경우
            c_y = TUK_HEIGHT
        character.clip_draw(frame * 64, 0, 64, 64, c_x, c_y)
    elif dir == 4:
        c_y -= 10
        if c_y < 0:  # 화면 아래로 나가는 경우
            c_y = 0
        character.clip_draw(frame * 64, 192, 64, 64, c_x, c_y)

    update_canvas()
    handle_events()

    if dir !=0:
        frame = (frame + 1) % 4

    delay(0.1)

close_canvas()
