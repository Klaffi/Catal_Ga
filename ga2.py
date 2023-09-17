from tkinter import *
from tkinter import ttk, messagebox
import pygad
import numpy
from threading import *
import customtkinter

customtkinter.set_appearance_mode("Lite")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title('Genetic Algorithm')
root.geometry('1000x620')


root.update_idletasks()
s = root.geometry()
s = s.split('+')
s = s[0].split('x')

width_root = int(s[0])
height_root = int(s[1])

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w // 2
h = h // 2
w = w - width_root // 2
h = h - height_root // 2
root.geometry('+{}+{}'.format(w, h))

my_menu = Menu(root)
root.config(menu=my_menu)


def _open():
    top = customtkinter.CTkToplevel()
    top.resizable(width=False, height=False)
    top.title('Помощь')
    text_help = customtkinter.CTkTextbox(top, width=500, height=300, wrap=WORD)
    text_help.pack()
    text_help.insert(1.0, "Для расчетов используйте не менее 500 поколений.\nЗначение поколений должно быть целым "
                          "числом.\nЕсли уравнение имеет менее 30 переменных, то введие в пустые строки число 0.")


file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Помощь", menu=file_menu)
file_menu.add_command(label="Помощь", command=_open)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.quit)


def progressStart():
    my_progress.start(10)


def progressStop():
    my_progress.stop()


def zxc():
    if x1_entry.get() and x2_entry.get() and x3_entry.get() and x4_entry.get() and x5_entry.get() and x6_entry.get() \
            and x7_entry.get() and x8_entry.get() and x9_entry.get() and x10_entry.get() and x11_entry.get() and\
            x12_entry.get() and x13_entry.get() and x14_entry.get() and x15_entry.get() and x16_entry.get()\
            and x17_entry.get() and x18_entry.get() and x19_entry.get() and x20_entry.get() and x21_entry.get() \
            and x22_entry.get() and x23_entry.get() and x24_entry.get() and x25_entry.get() and x26_entry.get() \
            and x27_entry.get() and x28_entry.get() and x29_entry.get() and x30_entry.get() and y_entry.get():

        _Y = float(y_entry.get())
        x1 = float(x1_entry.get())
        x2 = float(x2_entry.get())
        x3 = float(x3_entry.get())
        x4 = float(x4_entry.get())
        x5 = float(x5_entry.get())
        x6 = float(x6_entry.get())
        x7 = float(x7_entry.get())
        x8 = float(x8_entry.get())
        x9 = float(x9_entry.get())
        x10 = float(x10_entry.get())
        x11 = float(x11_entry.get())
        x12 = float(x12_entry.get())
        x13 = float(x13_entry.get())
        x14 = float(x14_entry.get())
        x15 = float(x15_entry.get())
        x16 = float(x16_entry.get())
        x17 = float(x17_entry.get())
        x18 = float(x18_entry.get())
        x19 = float(x19_entry.get())
        x20 = float(x20_entry.get())
        x21 = float(x21_entry.get())
        x22 = float(x22_entry.get())
        x23 = float(x23_entry.get())
        x24 = float(x24_entry.get())
        x25 = float(x25_entry.get())
        x26 = float(x26_entry.get())
        x27 = float(x27_entry.get())
        x28 = float(x28_entry.get())
        x29 = float(x29_entry.get())
        x30 = float(x30_entry.get())
        function_inputs = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20,
                           x21, x22, x23, x24, x25, x26, x27, x28, x29, x30]
        desired_output = _Y
        if x2 == 0:
            function_inputs.pop(1)
        if x3 == 0:
            function_inputs.pop(2)
        if x4 == 0:
            function_inputs.pop(3)
        if x5 == 0:
            function_inputs.pop(4)
        if x6 == 0:
            function_inputs.pop(5)
        if x7 == 0:
            function_inputs.pop(-24)
        if x8 == 0:
            function_inputs.pop(-23)
        if x9 == 0:
            function_inputs.pop(-22)
        if x10 == 0:
            function_inputs.pop(-21)
        if x11 == 0:
            function_inputs.pop(-20)
        if x12 == 0:
            function_inputs.pop(-19)
        if x13 == 0:
            function_inputs.pop(-18)
        if x14 == 0:
            function_inputs.pop(-17)
        if x15 == 0:
            function_inputs.pop(-16)
        if x16 == 0:
            function_inputs.pop(-15)
        if x17 == 0:
            function_inputs.pop(-14)
        if x18 == 0:
            function_inputs.pop(-13)
        if x19 == 0:
            function_inputs.pop(-12)
        if x20 == 0:
            function_inputs.pop(-11)
        if x21 == 0:
            function_inputs.pop(-10)
        if x22 == 0:
            function_inputs.pop(-9)
        if x23 == 0:
            function_inputs.pop(-8)
        if x24 == 0:
            function_inputs.pop(-7)
        if x25 == 0:
            function_inputs.pop(-6)
        if x26 == 0:
            function_inputs.pop(-5)
        if x27 == 0:
            function_inputs.pop(-4)
        if x28 == 0:
            function_inputs.pop(-3)
        if x29 == 0:
            function_inputs.pop(-2)
        if x30 == 0:
            function_inputs.pop(-1)

        def fitness_func(_solution, _solution_idx):
            output = numpy.sum(_solution * function_inputs)
            fitness = 1.0 / numpy.abs(output - desired_output)
            return fitness

        fitness_function = fitness_func

        num_generations = int(gen_entry.get())
        num_parents_mating = 20

        sol_per_pop = 50
        num_genes = len(function_inputs)

        init_range_low = -2
        init_range_high = 5

        parent_selection_type = "sss"
        keep_parents = 1

        crossover_type = "single_point"

        mutation_type = "random"
        mutation_percent_genes = 20
        ga_instance = pygad.GA(num_generations=num_generations,
                               num_parents_mating=num_parents_mating,
                               fitness_func=fitness_function,
                               sol_per_pop=sol_per_pop,
                               num_genes=num_genes,
                               init_range_low=init_range_low,
                               init_range_high=init_range_high,
                               parent_selection_type=parent_selection_type,
                               keep_parents=keep_parents,
                               crossover_type=crossover_type,
                               mutation_type=mutation_type,
                               mutation_percent_genes=mutation_percent_genes)
        ga_instance.run()
        progressStop()
        # ga_instance.plot_fitness()
        solution, solution_fitness, _solution_idx = ga_instance.best_solution()
        prediction = numpy.sum(numpy.array(function_inputs) * solution)
        text.insert(1.0, "\nПараметры наилучшего поколения : {solution}".format(
            solution=list(solution)) + "\nРезультаты наилучших вариантов : {prediction}".format(
            prediction=prediction) + "\n----------------------------")


    else:
        text.insert(1.0, "\nВведите данные в поля, либо впишите ноль" + "\n----------------------------")
        progressStop()


my_label_frame = LabelFrame(root,
                            text=u"Генетический алгоритм для линейного уравнения типа Y("
                                 u"X)=K\u2081X\u2081+K\u2082X\u2082+...+K\u2081\u2080X\u2083\u2080")
my_label_frame.pack(pady=5)

my_frame = Frame(my_label_frame)
my_frame.pack(pady=5)

y_label = customtkinter.CTkLabel(my_frame, text="Значение Y: ")
y_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

gen_label = customtkinter.CTkLabel(my_frame, text="Количество поколений: ")
gen_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x1_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2081: ")
x1_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x2_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2082: ")
x2_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x3_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2083: ")
x3_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x4_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2084: ")
x4_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x5_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2085: ")
x5_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x6_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2086: ")
x6_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x7_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2087: ")
x7_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x8_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2088: ")
x8_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x9_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2089: ")
x9_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x10_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2081\u2080: ")
x10_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x11_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2081\u2081: ")
x11_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x12_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2081\u2082: ")
x12_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x13_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2081\u2083: ")
x13_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x14_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2081\u2084: ")
x14_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x15_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2081\u2085: ")
x15_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x16_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2081\u2086: ")
x16_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x17_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2081\u2087: ")
x17_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x18_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2081\u2088: ")
x18_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x19_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2081\u2089: ")
x19_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x20_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2082\u2080: ")
x20_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x21_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2082\u2081: ")
x21_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x22_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2082\u2082: ")
x22_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x23_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2082\u2083: ")
x23_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x24_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2082\u2084: ")
x24_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x25_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2082\u2085: ")
x25_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x26_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2082\u2086: ")
x26_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x27_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2082\u2087: ")
x27_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x28_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2082\u2088: ")
x28_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x29_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2082\u2089: ")
x29_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

x30_label = customtkinter.CTkLabel(my_frame, text="Переменная X\u2083\u2080: ")
x30_entry = customtkinter.CTkEntry(my_frame, font=("Helvetica", 10))

y_label.grid(row=0, column=0)
y_entry.grid(row=0, column=1)

gen_label.grid(row=1, column=0)
gen_entry.grid(row=1, column=1)

x1_label.grid(row=2, column=0)
x1_entry.grid(row=2, column=1)

x2_label.grid(row=3, column=0)
x2_entry.grid(row=3, column=1)

x3_label.grid(row=4, column=0)
x3_entry.grid(row=4, column=1)

x4_label.grid(row=5, column=0)
x4_entry.grid(row=5, column=1)

x5_label.grid(row=6, column=0)
x5_entry.grid(row=6, column=1)

x6_label.grid(row=7, column=0)
x6_entry.grid(row=7, column=1)

x7_label.grid(row=8, column=0)
x7_entry.grid(row=8, column=1)

x8_label.grid(row=9, column=0)
x8_entry.grid(row=9, column=1)

x9_label.grid(row=10, column=0)
x9_entry.grid(row=10, column=1)

x10_label.grid(row=11, column=0)
x10_entry.grid(row=11, column=1)

x11_label.grid(row=2, column=2)
x11_entry.grid(row=2, column=3)

x12_label.grid(row=3, column=2)
x12_entry.grid(row=3, column=3)

x13_label.grid(row=4, column=2)
x13_entry.grid(row=4, column=3)

x14_label.grid(row=5, column=2)
x14_entry.grid(row=5, column=3)

x15_label.grid(row=6, column=2)
x15_entry.grid(row=6, column=3)

x16_label.grid(row=7, column=2)
x16_entry.grid(row=7, column=3)

x17_label.grid(row=8, column=2)
x17_entry.grid(row=8, column=3)

x18_label.grid(row=9, column=2)
x18_entry.grid(row=9, column=3)

x19_label.grid(row=10, column=2)
x19_entry.grid(row=10, column=3)

x20_label.grid(row=11, column=2)
x20_entry.grid(row=11, column=3)

x21_label.grid(row=2, column=4)
x21_entry.grid(row=2, column=5)

x22_label.grid(row=3, column=4)
x22_entry.grid(row=3, column=5)

x23_label.grid(row=4, column=4)
x23_entry.grid(row=4, column=5)

x24_label.grid(row=5, column=4)
x24_entry.grid(row=5, column=5)

x25_label.grid(row=6, column=4)
x25_entry.grid(row=6, column=5)

x26_label.grid(row=7, column=4)
x26_entry.grid(row=7, column=5)

x27_label.grid(row=8, column=4)
x27_entry.grid(row=8, column=5)

x28_label.grid(row=9, column=4)
x28_entry.grid(row=9, column=5)

x29_label.grid(row=10, column=4)
x29_entry.grid(row=10, column=5)

x30_label.grid(row=11, column=4)
x30_entry.grid(row=11, column=5)


def popup():
    messagebox.showinfo('zxctyl', 'Для того, чтобы программа начала считать, нажмите "OK"')
    Thread(target=(lambda: [progressStart(), zxc()])).start()


my_button = customtkinter.CTkButton(my_label_frame, text="Провести расчеты", command=lambda: [popup()])
my_button.pack(pady=5)

my_progress = ttk.Progressbar(root, orient=HORIZONTAL, length=461, mode='indeterminate')
my_progress.pack()

text = Text(width=57, height=13, wrap=WORD)
text.pack(pady=5)

root.mainloop()
