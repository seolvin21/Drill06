from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

hand = load_image('hand_arrow.png')
TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def character_move():
    global arrive
    global hand_pos
    global x, y, i
    global character_left, character_right

    if arrive:
        return

    if len(hand_pos) > 0:
        if hand_pos[0][0] < x:
            character_left = True
            character_right = False
        elif hand_pos[0][0] > x:
            character_left = False
            character_right = True

        t = i / 100 / 100
        x = (1 - t) * x + t * hand_pos[0][0]
        y = (1 - t) * y + t * hand_pos[0][1]

    if i > 300:
        i = 0
        arrive = True
    else:
        i = i + 1


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



running, arrive = True, False
character_left, character_right = False, True
hand_x, hand_y = 0, 0
hand_pos = []
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
i = 0
frame = 0

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    if arrive and len(hand_pos) > 0:
        i = 0
        arrive = False
        hand_pos.pop(0)

    character_move()

    for hand_x, hand_y in hand_pos:
        hand.clip_draw(0, 0, 50, 52, hand_x, hand_y)

    if character_left:
        character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, y, 100, 100)
    elif character_right:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    frame = (frame + 1) % 8

    handle_events()
    update_canvas()

    delay(0.01)


close_canvas()




