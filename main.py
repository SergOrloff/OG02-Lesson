import tkinter as tk
from tkinter import Button

def Hello():
# Необходимо считывать информацию из поля для ввода, которое называется entry.
# Для этого используем функцию get(). Это метод для получения значения из поля для ввода.
# Прописываем это так: # name = str(entry.get())
# name — переменная, внутри которой сохраняеся имя, entry — поле для ввода,
# .get — в переменную сохранится все содержимое поля для ввода сплошным элементом.
    fam, name = entry.get().split()

    label.config(text=f'Привет, {fam}чик {name}!', fg="green", font = ("Comic Sans MS", 20, "bold"), bg="yellow")

root = tk.Tk()
root.configure(bg='light grey')
root.geometry('650x150')
# Введем название программы:
root.title('Домашнее задание "Использование функции Tkinter"')
# Для того, чтобы сделать подпись, создаем переменную label, где пропишем необходимое действие:
label = tk.Label(root, text='Как звать тебя?', width=52, justify="center", fg="white", font=("Helvetica", 15), bg="red")
label.pack(pady=10, padx=100, anchor="w")
# Создаем поле для ввода с помощью переменной entry():
entry = tk.Entry(root, width=22, fg="white", font = (("Times New Roman"), 15), bg="green")
# Это виджет, который будет появляться в окне. Можно задать ему ширину ( width=),
# но сейчас это не так важно. Поле для ввода создано и необходимо его расположить в окне:
entry.pack()
# Создадим кнопку которая будет выводить приветствие. Для этого используем
# переменную button, которая будет создавать виджет кнопки для запуска приветствия.
button = tk.Button(root, text='Нажми кнопку после ввода ответа!', width=42, command=Hello, fg="white", font = (("Times New Roman"), 15), bg="brown")
button.pack()


button1 = tk.Button(root, text='Нажми кнопку после ввода ответа!', width=42, command=Hello1, fg="white", font = (("Times New Roman"), 15), bg="brown")
button.pack()

# Все закрепляем на экране
root.mainloop()