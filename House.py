import tkinter as tk
import random

def toggle_light():
    global light_on
    light_on = not light_on

    if light_on:

        canvas.config(bg="midnightblue")
        canvas.itemconfig(window, fill="yellow")
        button.config(text="Выключить свет")
    else:
        canvas.config(bg="lightblue")
        canvas.itemconfig(window, fill="black")
        button.config(text="Включить свет")

# Создаем окно
root = tk.Tk()
root.title("home")

# Холст для рисования
canvas = tk.Canvas(root, width=400, height=400, bg="orange")
canvas.pack()

# Рисуем home
canvas.create_polygon(100, 150, 300, 150, 200, 50, fill="white",outline="black")
canvas.create_rectangle(120, 150, 280, 300, fill="white", outline="black")
window = canvas.create_rectangle(180, 180, 220, 220, fill="black")
# Кнопка для переключения
light_on = False
button = tk.Button(root, text="Включить свет", command=toggle_light)
button.pack(pady=10)

root.mainloop()