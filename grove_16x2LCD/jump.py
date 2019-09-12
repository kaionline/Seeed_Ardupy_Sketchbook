from grove import grove_16x2_lcd
from grove import grove_button
from random import randint
import board
import time

# KEEP THOSE DEFINE
RUN1, RUN2, JUMP, J_UPPER, J_LOWER = 1, 2, 3, 46, 4
STEMPTY, STSOLID, STSOLID_RIGHT, STSOLID_LEFT = 32, 5, 6, 7
WIDTH, EMPTY, LOW_BLOCK, UPP_BLOCK, HOR_POS = 16, 0, 1, 2, 1
POS_OFF, R_LOW_1, R_LOW_2, J_1, J_2, J_3, J_4, J_5, J_6, J_7, J_8, R_UPP_1, R_UPP_2 = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

lcd = grove_16x2_lcd()
lcd.initialize_graphics()
btn = grove_button(board.D0)

def rand(max):
    return randint(0, max)

def advance_terrain(terrain, new_terrain):
    i = 0
    while i < WIDTH:
        current = terrain[i]
        next = new_terrain if i == WIDTH-1 else terrain[i+1]
        if current == STEMPTY:
            terrain[i] = STSOLID_RIGHT if next == STSOLID else STEMPTY
        elif current == STSOLID:
            terrain[i] = STSOLID_LEFT if next == STEMPTY else STSOLID
        elif current == STSOLID_RIGHT:
            terrain[i] = STSOLID
        elif current == STSOLID_LEFT:
            terrain[i] = STEMPTY
        i = i + 1

def loop(sta):
    sta.button_pushed = btn.value
    if not sta.playing:
        pos = POS_OFF if sta.blink else sta.hero_pos
        lcd.draw_hero(pos, sta.distance >> 3)
        lcd.set_cursor(0, 0)
        lcd.print("Press Start")
        time.sleep(0.25)
        sta.blink = not sta.blink
        if sta.button_pushed:
            lcd.initialize_graphics()
            sta.hero_pos = R_LOW_1
            sta.playing = True
            sta.button_pushed = False
            sta.distance = 0
        return
    advance_terrain(lcd.terrain_lower, STSOLID if sta.new_terrain_type == LOW_BLOCK else STEMPTY)
    advance_terrain(lcd.terrain_upper, STSOLID if sta.new_terrain_type == UPP_BLOCK else STEMPTY)
    sta.new_terrain_duration = sta.new_terrain_duration - 1
    if sta.new_terrain_duration == 0:
        if sta.new_terrain_type == EMPTY:
            sta.new_terrain_type = UPP_BLOCK if rand(3) == 0 else LOW_BLOCK
            sta.new_terrain_duration = 2 + rand(10)
        else:
            sta.new_terrain_type = EMPTY
            sta.new_terrain_duration = 10 + rand(10)
    if sta.button_pushed:
        if sta.hero_pos <= R_LOW_2:
            sta.hero_pos = J_1
        sta.button_pushed = False
    if lcd.draw_hero(sta.hero_pos, sta.distance >> 3):
        sta.playing = False
    else:
        if sta.hero_pos == R_LOW_2 or sta.hero_pos == J_8:
            sta.hero_pos = R_LOW_1
        elif sta.hero_pos >= J_3 and sta.hero_pos <= J_5 and lcd.terrain_lower[HOR_POS] != STEMPTY:
            sta.hero_pos = R_UPP_1
        elif sta.hero_pos >= R_UPP_1 and lcd.terrain_lower[HOR_POS] == STEMPTY:
            sta.hero_pos = J_5
        elif sta.hero_pos == R_UPP_2:
            sta.hero_pos = R_UPP_1
        else:
            sta.hero_pos = sta.hero_pos + 1
        sta.distance = sta.distance + 1
    time.sleep(0.05)

class state:
    def __init__(self):
        self.new_terrain_type, self.new_terrain_duration = EMPTY, 1
        self.hero_pos, self.playing, self.blink = R_LOW_1, False, False
        self.distance, self.button_pushed = 0, False

sta = state()
while True:
    loop(sta)