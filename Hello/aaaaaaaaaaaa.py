rom tkinter import *
import time
import random

score = 1
speed = score//150*2+1
rainbow_colors = ['#fff200', '#effd5f', '#fee12b', '#fffdd0', '#7c5295', 'gold',
                  'yellow', '#d5a6e6', '#d0f0c0', '#39ff14', '#7ef9ff', '#3fe0d0']


class SATURNV:
    def __init__(self, canvas, x, y):
        self.canvas = canvas

        # Rocket

        # Flames
        self.flame1 = self.canvas.create_arc(12, 272, 16, 297, start=180,
                                             extent=359, fill='#ff781f', outline='#ff8b3d')
        self.flame2 = self.canvas.create_arc(24, 272, 28, 297, start=180,
                                             extent=359, fill='#ff781f', outline='#ff8b3d')
        self.flame3 = self.canvas.create_arc(18, 272, 22, 297, start=180,
                                             extent=359, fill='#ff781f', outline='#ff8b3d')
        self.flames = [self.flame1, self.flame2, self.flame3]

        # Nozzles
        self.nozzle3 = self.canvas.create_arc(17, 269, 23, 287, start=0, extent=180, fill='#808080', outline='')
        self.nozzle1 = self.canvas.create_arc(12, 269, 16, 288, start=0, extent=180, fill='#989898', outline='#989898')
        self.nozzle2 = self.canvas.create_arc(24, 269, 28, 288, start=0, extent=180, fill='#989898', outline='#989898')

        # Wings
        self.bottomwing_1 = self.canvas.create_polygon(10, 270, 0, 270, 0, 258, 10, 220,
                                                       fill='#1f2f2f', outline='#1f2f2f')
        self.bottomwing_2 = self.canvas.create_polygon(30, 270, 40, 270, 40, 258, 30, 220,
                                                       fill='#1f2f2f', outline='#1f2f2f')

        # Stage 1
        self.stage1_bottom = self.canvas.create_rectangle(10, 220, 30, 270, fill='black', outline='black')
        self.stage1_usa_bg = self.canvas.create_rectangle(16, 230, 24, 270, fill='white', outline='white')
        self.stage1_usa = self.canvas.create_text(21, 249, text='U\nS\nA', font=('Helvetica', 10, 'bold'),
                                                  justify='center', fill='black')
        self.stage1_top = self.canvas.create_rectangle(10, 160, 30, 220, fill='white', outline='white')
        self.unitedstates = self.canvas.create_text(17, 190, text='U\nN\nI\nT\nE\nD\n\nS\nT\nA\nT\nE\nS',
                                                    font=('Helvetica', 3, 'bold'), justify='center', fill='red')

        # Stage 2
        self.stage2_bottom = self.canvas.create_rectangle(10, 140, 30, 160, fill='black', outline='black')
        self.stage2_center = self.canvas.create_rectangle(10, 90, 30, 140, fill='white', outline='white')
        self.saturnV = self.canvas.create_text(21, 137, text='SATURN V', font=('Helvetica', 3),
                                               justify='center', fill='red')
        self.flag_blue = self.canvas.create_rectangle(18, 127, 22, 129, fill='blue', outline='')
        self.flag_red = self.canvas.create_text(22, 128, text='______________\n______________\n______________',
                                                font=('Helvetica', 2), fill='red')
        self.stage2_topline = self.canvas.create_rectangle(10, 88, 30, 90, fill='black', outline='black')
        self.stage2_top = self.canvas.create_rectangle(10, 80, 30, 88, fill='white', outline='white')

        # Stage 3
        self.stage2_3 = self.canvas.create_polygon(10, 80, 30, 80, 26, 67, 14, 67, fill='black', outline='black')
        self.stage3_bottom = self.canvas.create_polygon(14, 67, 26, 67, 24, 44, 16, 44, fill='white', outline='white')
        self.stage3_line = self.canvas.create_line(24, 44, 16, 44, fill='#dcdcdc')
        self.stage3_top = self.canvas.create_polygon(23, 43, 17, 43, 18, 30, 22, 30, fill='white', outline='white')

        # Top
        self.cargo = self.canvas.create_rectangle(18, 25, 22, 30, fill='#ebecf0', outline='#ebecf0')
        self.cargo_top = self.canvas.create_polygon(18, 25, 22, 25, 20, 18, fill='#ebecf0', outline='#ebecf0')
        self.top = self.canvas.create_rectangle(20, 0, 20, 18, fill='white', outline='')

        # Rocket list
        self.rocket = [self.bottomwing_1, self.bottomwing_2, self.flame1, self.flame2, self.flame3,
                       self.nozzle1, self.nozzle2, self.nozzle3, self.stage1_bottom, self.stage1_usa_bg,
                       self.stage1_usa, self.stage1_top, self.unitedstates, self.stage2_bottom,
                       self.stage2_center, self.saturnV, self.flag_red, self.flag_blue, self.stage2_topline,
                       self.stage2_top, self.stage2_3, self.stage3_bottom, self.stage3_line, self.stage3_top,
                       self.cargo, self.cargo_top, self.top]
        # Color dictionary
        self.color_dict = {self.bottomwing_1: '#1f2f2f', self.bottomwing_2: '#1f2f2f', self.flame1: '#ff781f',
                           self.flame2: '#ff781f', self.flame3: '#ff781f', self.nozzle1: '#808080',
                           self.nozzle2: '#808080', self.nozzle3: '#808080', self.stage1_bottom: 'black',
                           self.stage1_usa_bg: 'white', self.stage1_usa: 'black', self.stage1_top: 'white',
                           self.unitedstates: 'red', self.stage2_bottom: 'black', self.stage2_center: 'white',
                           self.saturnV: 'red', self.flag_red: 'red', self.flag_blue: 'blue',
                           self.stage2_topline: 'black', self.stage2_top: 'white', self.stage2_3: 'black',
                           self.stage3_bottom: 'white', self.stage3_line: '#dcdcdc', self.stage3_top: 'white',
                           self.cargo: '#ebecf0', self.cargo_top: '#ebecf0', self.top: 'white'}

        # __init__
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        for i in self.rocket:
            self.canvas.move(i, x, y)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<space>', self.straight)

    def draw(self):
        for i in self.rocket:
            self.canvas.move(i, self.x, 0)
        pos1 = self.canvas.coords(self.bottomwing_1)
        pos2 = self.canvas.coords(self.bottomwing_2)
        if pos1[0] <= 0:
            self.x = 0
            for i in self.rocket:
                self.canvas.move(i, 1, 0)
        if pos2[2] >= self.canvas_width:
            self.x = 0
            for i in self.rocket:
                self.canvas.move(i, -1, 0)

    def turn_left(self, evt):
        if boost:
            self.x = -speed//2-6
        else:
            self.x = -speed//2-2

    def turn_right(self, evt):
        if boost:
            self.x = speed // 2 + 7
        else:
            self.x = speed // 2 + 3


    def straight(self, evt):
        self.x = 0

    def get_pos(self):
        rocket_pos = []
        for i in self.rocket:
            position = self.canvas.coords(i)
            rocket_pos.append(position)
        print(rocket_pos)


class Meteorite:
    def __init__(self, canv):
        self.canvas = canv
        s = random.randint(1, 10)
        type1 = (22 - random.randint(-2, s), 15,
                 27 + s, 9 - s, 40 + s, 10 - s,
                 45 + random.randint(0, s) + s, 25 + s,
                 38 + random.randint(1, 2) * s, 39 + s,
                 30 + s, 43 + random.randint(1, 2) * s, 20 + s, 34 + s)
        self.y = 0
        self.id = self.canvas.create_polygon(type1, fill=random.choice(['#ac9d8e', 'grey']))
        self.canvas.move(self.id, random.randint(0, canvas.winfo_width()), random.randint(-10000, -100))


# Create root & canvas
tk = Tk()
tk.title('Apollo13')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=1250, height=650, bg='#1f182d', bd=0, highlightthickness=0)
canvas.pack()
tk.update()

# Start settings
play = True
apollo13 = SATURNV(canvas, canvas.winfo_width()/2-50, 335)
z = 10-len(str(score))
score_txtlab = canvas.create_text(90, 30, text=z*'0'+str(round(score)),
                                  font=('Courier', 25), justify='center', fill='white')
apollo13_txt = canvas.create_text(canvas.winfo_width()-90, 30, text='APOLLO 13',
                                  font=('Courier', 25), justify='center', fill='white')
game_over_txt = canvas.create_text(canvas.winfo_width()/2, 300, text='GAME OVER',
                                   font=('Courier', 155), justify='center', state='hidden')
go_score_txt = canvas.create_text(canvas.winfo_width()/2, 200, text='Score: '+str(score),
                                  font=('Courier', 125), justify='center', state='hidden')


# Stars
stars = []
for i in range(0, 200):
    stars.append(canvas.create_text(random.randint(0, canvas.winfo_width()),
                                    random.randint(-1000, canvas.winfo_height()), text=".",
                                    font=('Helvetica', 14), fill='white'))


# Meteorites
meteorites = []

for i in range(0, 40):
    m = Meteorite(canvas)
    meteorites.append(m.id)


# Boost

boost = False


def set_boost(evt):
    global boost
    boost = True


def quit_boost(evt):
    global boost
    boost = False


canvas.bind_all('<KeyPress-Up>', set_boost)
canvas.bind_all('<KeyPress-Down>', quit_boost)


# Mainloop
while 1:

    # Set speed
    if boost:
        if score < 1000:
            speed = score//1000*2+9
        if score > 1000:
            speed = score//1000*2+7
    else:
        if score < 1000:
            speed = score//1000*2+1
        if score > 1000:
            speed = score//1000*2

    # Bring rocket to front
    for i in apollo13.rocket:
        canvas.tag_raise(i)

    # Get rocket coords
    rocket_pos = []
    for i in apollo13.rocket:
        pos = apollo13.canvas.coords(i)
        rocket_pos.append(pos)
    wing_rect = []
    wing_rect.append((rocket_pos[0][2], rocket_pos[0][3]))
    wing_rect.append((rocket_pos[1][4], rocket_pos[1][5]))
    rocket_body = []
    rocket_body.append((rocket_pos[20][6] - 2, rocket_pos[20][7]))
    rocket_body.append((rocket_pos[8][2], rocket_pos[8][3]))
    top_rect = []
    top_rect.append((rocket_pos[-1][0]-1, rocket_pos[-1][1]))
    top_rect.append((rocket_pos[-1][0]+1, rocket_pos[20][1]))
    top_triangle = []
    top_triangle.append((rocket_pos[-1][0]-3, rocket_pos[-1][1]))
    top_triangle.append((rocket_pos[-1][0]+3, rocket_pos[-1][1]+15))

    # Fly rocket
    if play:
        if boost:
            for i in apollo13.rocket:
                canvas.itemconfig(i, fill=random.choice(rainbow_colors))
            for i in apollo13.flames:
                canvas.itemconfig(i, fill=random.choice(['white', 'red']))
        else:
            for i in apollo13.rocket:
                canvas.itemconfig(i, fill=apollo13.color_dict[i])
        if score % 30 == 0:
            for i in range(0, 1):
                m = Meteorite(canvas)
                meteorites.append(m.id)
        # Stars
        for i in stars:
            if boost:
                canvas.move(i, 0, speed+31)
            else:
                canvas.move(i, 0, speed + 4)
            star_pos = canvas.coords(i)
            if star_pos[1] > 700:
                canvas.move(i, 0, -1000)
        # Meteorites

        if score > 20:
            for i in meteorites:
                if boost:
                    canvas.move(i, 0, speed+35)
                else:
                    canvas.move(i, 0, speed + 8)
                met_pos = canvas.coords(i)
                if met_pos[1] > 800:
                    canvas.move(i, random.randint(-100, 100), -10000)
                met_pos2 = canvas.coords(i)
                if met_pos2[0] or met_pos2[12] <= 0:
                    canvas.move(i, 175, 0)
                if met_pos2[6] or met_pos2[8] >= canvas.winfo_width():
                    canvas.move(i, -175, 0)
                for x in range(1, 14, 2):
                    if wing_rect[0][1] >= met_pos2[x] >= wing_rect[1][1]:
                        if wing_rect[1][0] >= met_pos2[x - 1] >= wing_rect[0][0]:
                            play = False
                    if rocket_body[0][1] <= met_pos2[x] <= rocket_body[1][1]:
                        if rocket_body[1][0] >= met_pos2[x - 1] >= rocket_body[0][0]:
                            play = False
                    if top_rect[0][1] <= met_pos2[x] <= top_rect[1][1]:
                        if top_rect[1][0] >= met_pos2[x - 1] >= top_rect[0][0]:
                            play = False
                    if top_triangle[0][1] <= met_pos2[x] <= top_triangle[1][1]:
                        if top_triangle[1][0] >= met_pos2[x - 1] >= top_triangle[0][0]:
                            play = False
        if boost:
            score += 8
        else:
            score += 2
        z = 10 - len(str(round(score)))
        canvas.itemconfig(score_txtlab, text=z * '0' + str(round(score)))

    # Stop rocket
    if not play:

        # Top score
        score_list = open('Space Rocket: Scorelist', 'r')
        scores = score_list.readlines()
        scores_lists = []
        score_int = []
        for i in scores:
            scores_lists.append(i.split())
            score_int.append(int(scores_lists[-1][0]))
        top_score = max(score_int)
        score_list.close()
        if score >= top_score:
            score_list = open('Space Rocket: Scorelist', 'a')
            score_list.write(str(round(score)) + '\n')
            score_list.close()
            top_score = round(score)

        # Stop engines, fall rocket
        for i in apollo13.flames:
            canvas.move(i, 0, 300)
        for i in range(0, 70):
            tk.update()
            time.sleep(0.0001)
            if boost:
                if i % 2 == 0:
                    for x in apollo13.rocket:
                        canvas.itemconfig(x, state='hidden')
                else:
                    for x in apollo13.rocket:
                        canvas.itemconfig(x, state='normal', fill='red')
            else:
                if i % 2 == 0:
                    for x in apollo13.rocket:
                        canvas.itemconfig(x, state='hidden')
                else:
                    for x in apollo13.rocket:
                        canvas.itemconfig(x, state='normal')

            apollo13.x = apollo13.x//2
            apollo13.draw()

            # Stars (up)
            for x in stars:
                canvas.move(x, 0, -1)
                star_pos = canvas.coords(x)
                if star_pos[1] < 0:
                    canvas.move(x, 0, 1000)

            # Meteorites (up)
            for x in meteorites:
                canvas.move(x, 0, -2)
                met_pos = canvas.coords(x)
                if met_pos[1] > 800:
                    canvas.move(x, 0, 10000)

        # Reset colors
        for i in apollo13.rocket:
            canvas.itemconfig(i, fill=apollo13.color_dict[i])

        # Score, best score & Game Over
        for i in range(10, 170, 2):
            canvas.tag_lower(game_over_txt)
            canvas.tag_raise(go_score_txt)
            canvas.itemconfig(game_over_txt, font=('Courier', i), state='normal')
            tk.update()
            time.sleep(0.005)
        canvas.itemconfig(go_score_txt, text='Score: '+str(round(score))+' - Best: '+str(top_score),
                          font=('Courier', 30), state='normal')
        tk.update()
        time.sleep(2)

        # Reset window
        boost = False
        score = 1
        canvas.itemconfig(game_over_txt, state='hidden')
        canvas.itemconfig(go_score_txt, state='hidden')
        for i in meteorites:
            canvas.move(i, 0, random.randint(-2000, -1500))
        for i in apollo13.rocket:
            canvas.move(i, -50, 0)
        for i in apollo13.flames:
            canvas.move(i, 0, -300)

    # Burning flames
    f = random.choice(apollo13.flames)
    if boost:
        dx = random.randint(-5, 4)
        dy = random.randint(-20, 20)
    else:
        dx = random.randint(-1, 0)
        dy = random.randint(-7, 7)
    apollo13.canvas.move(f, dx, dy)

    apollo13.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.0001)

    apollo13.canvas.move(f, -dx, -dy)
    play = True