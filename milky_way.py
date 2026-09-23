import tkinter as tk
import random
import math

root = tk.Tk()
root.title("Milky Way")
root.geometry("800x600")

canvas = tk.Canvas(root, width=800, height=600, bg="#030414")
canvas.pack()

stars = []

for _ in range(250):
    stars.append([
        random.uniform(0, 6.28),
        random.uniform(50, 350),
        random.randint(1, 3)
    ])


angle = 0
def animate():
    global angle
    angle += 0.002

    canvas.delete("all")

    canvas.create_rectangle(
        0, 0, 800, 600,
        fill="#030414",
    )

    for a, radius, size in stars:
        x = 400 + math.cos(a + angle) * radius
        y = 300 + math.sin(a + angle) * radius * 0.45

        canvas.create_oval(
            x-size, y-size,
            x+size, y+size,
            fill="white",
            outline=""
        )
    root.after(30, animate)

animate()
root.mainloop()