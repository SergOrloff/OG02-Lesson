<<<<<<< Updated upstream
import tkinter as tk

def Hello1():
# Необходимо считывать информацию из поля для ввода, которое называется entry.
# Для этого используем функцию get(). Это метод для получения значения из поля для ввода.
# Прописываем это так: # name = str(entry.get())
# name — переменная, внутри которой сохраняеся имя, entry — поле для ввода,
# .get — в переменную сохранится все содержимое поля для ввода сплошным элементом.
    fam, name = entry.get().split()
    label.config(text=f'Привет, {fam}ка {name}!', fg="green",
                 font = ("Comic Sans MS", 20, "bold"), bg="yellow")

