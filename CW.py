# Задание 1.Необходимо написать проект, содержащий функционал работы с заметками. Программа должна уметь
#  создавать заметку, сохранять её,  читать список заметок, редактировать заметку, удалять заметку.

import tkinter as tk

# Создание основного окна
root = tk.Tk()
root.title("Простое приложение для заметок")
root.geometry("400x400")  


# Создание виджетов.Мы добавим текстовое поле для написания заметок и список для отображения созданных заметок.
notes_listbox = tk.Listbox(root)
notes_listbox.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

note_entry = tk.Entry(root, width=50)
note_entry.pack(pady=20, padx=20)


# Добавление функциональности.Добавим кнопки для создания новых заметок и удаления выбранной заметки из списка.
def add_note():
    note = note_entry.get()
    if note:
        notes_listbox.insert(tk.END, note)
        note_entry.delete(0, tk.END)

def delete_note():
    try:
        notes_listbox.delete(notes_listbox.curselection())
    except:
        pass

add_button = tk.Button(root, text="Добавить заметку", command=add_note)
add_button.pack(pady=10, padx=20)

delete_button = tk.Button(root, text="Удалить заметку", command=delete_note)
delete_button.pack(pady=10, padx=20)


# Запуск приложения
root.mainloop()