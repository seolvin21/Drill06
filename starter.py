from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

hand = load_image('hand_arrow.png')
TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running
    global hand_x, hand_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type==SDL_MOUSEBUTTONDOWN:
            hand_x, hand_y = event.x, TUK_HEIGHT - 1 - event.y
            hand_pos.append((hand_x, hand_y))
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass



running = True
hand_x, hand_y = 0, 0
hand_pos = []
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    for hand_x, hand_y in hand_pos:
        hand.clip_draw(0, 0, 50, 52, hand_x, hand_y)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    frame = (frame + 1) % 8

    handle_events()
    update_canvas()

close_canvas()




