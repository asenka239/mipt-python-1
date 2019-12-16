from random import randrange as rnd, choice
import tkinter as tk
import math
import time

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
a = 1  # ускорение свободного падения


class Ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса Ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 120

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки.
        То есть, обновляет значения self.x и self.y с учетом скоростей
        self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.live > 0:
            if self.y <= 500:
                self.vy -= a
                self.y -= self.vy
                self.x += self.vx
                self.vx *= 0.99
                self.set_coords()
            else:
                if self.vx ** 2 + self.vy**2 > 10:
                    self.vy = -self.vy / 2
                    self.vx = self.vx / 2
                    self.y = 499
                if self.live < 0:
                    balls.pop(balls.index(self))
                    canv.delete(self.id)
                else:
                    self.live -= 1
            if self.x > 780:
                self.vx = -self.vx / 2
                self.x = 779
                return False
        else:
            canv.delete(self.id)
            return True

    def hit_test(self, obj):
        """Функция проверяет сталкивалкивается ли
        данный обьект с целью, описываемой в объекте obj.

        Args:
            obj: Объект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели.
            В противном случае возвращает False.
        """
        if abs(obj.x - self.x) <= (self.r + obj.r)\
                and abs(obj.y - self.y) <= (self.r + obj.r):
            return True
        else:
            return False


"""
Класс gun описывает пушку.
"""


class Gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = -self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450, 20 + max(self.f2_power, 20) *
                    math.cos(self.an), 450 + max(self.f2_power, 20) *
                    math.sin(self.an))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


"""
Класс target описывает цель.
"""


class target():
    def __init__(self):
        self.points = 0
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.new_target()
        self.live = 1

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        self.vx = rnd(3, 10)
        self.vy = rnd(2, 8)
        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)

    def move(self):
        """Переместить цель по прошествии единицы времени.

        Метод описывает перемещение цели за один кадр перерисовки.
        То есть, обновляет значения self.x и self.y с учетом скоростей
        self.vx и self.vy, БЕЗ силы гравитации, действующей на цели,
        а стен по краям окна учитываются(размер окна 800х600).
        """
        canv.delete(self.id)
        self.x += self.vx
        self.y -= self.vy
        if self.x + self.r > 800 or self.x - self.r < 0:
            self.vx = -self.vx
        if self.y + self.r > 600 or self.y - self.r < 0:
            self.vy = -self.vy
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )


global t1
t1 = []
for x in range(2):
    t1.append(target())
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = Gun()
bullet = 0
balls = []


def new_game(event=''):
    global t1, screen1, balls, bullet
    for x in t1:
        x.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
    for x in t1:
        x.live = 1
    T1_LIVE = 0
    for x in t1:
        T1_LIVE += x.live
    while T1_LIVE > 0 or balls:
        for b in balls:
            if b.move():
                balls.remove(b)
            for x in t1:
                if b.hit_test(x) and x.live:
                    x.live = 0
                    x.hit()
                    T1_LIVE = 0
                    for x in t1:
                        T1_LIVE += x.live
                    if T1_LIVE == 0:
                        canv.itemconfig(screen1,
                                        text='Вы уничтожили цели за ' +
                                        str(bullet) + ' выстрелов')
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
        T1_LIVE = 0
        for x in t1:
            T1_LIVE += x.live
    canv.itemconfig(screen1, text='')
    root.after(750, new_game)


def update_targets():
    for t in t1:
        if t.live > 0:
            t.move()
        else:
            canv.delete(t.id)
    root.after(30, update_targets)


update_targets()
new_game()

root.mainloop()
