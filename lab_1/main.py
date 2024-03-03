from math import *
from tkinter import *
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


def function(x):
    func = ent_func.get()
    func_ = func.replace("^", "**").replace(",", ".").replace(" ", "").replace("y=", "") \
        .replace("f(x)=", "").replace("X", "x")
    y = eval(func_, {'x': x})
    return y


# ===============================================================================================================


def middle_of_the_segment(a, b):
    midpoint_ = 1 / 2 * (a + b)
    func = function(midpoint_)
    return midpoint_, func


def method_of_half_division(left_border, right_border, EPSILON):
    steps_counter = 1

    while True:
        midpoint_x = middle_of_the_segment(left_border, right_border)[0]
        midpoint_y = middle_of_the_segment(left_border, right_border)[1]

        if abs(midpoint_y) < EPSILON:
            return round(midpoint_x, rounding), round(function(midpoint_x), rounding)

        else:
            if function(midpoint_x) * function(left_border) < 0:
                steps_counter += 1
                right_border = midpoint_x

            if function(midpoint_x) * function(right_border) < 0:
                steps_counter += 1
                left_border = midpoint_x


# ===============================================================================================================


def calculation_y(a, b):
    y_ = a * (sqrt(5) - 1) / 2 + b * (3 - sqrt(5)) / 2
    return y_


def calculation_z(a, b):
    z_ = a * (3 - sqrt(5)) / 2 + b * (sqrt(5) - 1) / 2
    return z_


def golden_ratio_method(left_border, right_border, EPSILON):
    y = calculation_y(left_border, right_border)
    z = calculation_z(left_border, right_border)

    A = function(y)
    B = function(z)

    steps_counter = 0
    while True:
        steps_counter += 1

        if A < B:
            right_border = z

            if abs(right_border - left_border) < EPSILON:
                x = 1 / 2 * (left_border + right_border)
                break

            else:
                z = y
                B = A
                y = calculation_y(left_border, right_border)
                A = function(y)

        else:
            left_border = y

            if abs(right_border - left_border) < EPSILON:
                x = 1 / 2 * (left_border + right_border)
                break

            else:
                y = z
                A = B
                z = calculation_z(left_border, right_border)
                B = function(z)
    return round(x, rounding), round(function(x), rounding)


# ===============================================================================================================


def method_Fibonacci_numbers(left_border, right_border, EPSILON, acceptable_length_):
    nearest_fibonacci_number = abs(right_border - left_border) / acceptable_length_

    fibonacci_numbers = []
    fibonacci_numbers.insert(0, 1)
    fibonacci_numbers.insert(1, 1)

    number_of_calculations = 2

    value = fibonacci_numbers[number_of_calculations - 1] + fibonacci_numbers[number_of_calculations - 2]
    fibonacci_numbers.insert(number_of_calculations, value)

    while nearest_fibonacci_number >= fibonacci_numbers[number_of_calculations]:
        number_of_calculations += 1
        value = fibonacci_numbers[number_of_calculations - 1] + fibonacci_numbers[number_of_calculations - 2]
        fibonacci_numbers.insert(number_of_calculations, value)

    step_counter = 1

    localization_segment_length = abs(right_border - left_border) / fibonacci_numbers[number_of_calculations]
    x1 = left_border + localization_segment_length * fibonacci_numbers[number_of_calculations - 2]
    x2 = right_border - localization_segment_length * fibonacci_numbers[number_of_calculations - 2]

    while True:
        if function(x1) < function(x2):
            right_border = x2
            step_counter += 1

            if step_counter != number_of_calculations - 1:
                x2 = x1
                x1 = left_border + localization_segment_length * fibonacci_numbers[
                    number_of_calculations - 1 - step_counter]
            else:
                x2 = x1 + EPSILON

                if function(x1) < function(x2):
                    right_border = x1
                    x = (left_border + right_border) / 2
                    return round(x, rounding), round(function(x), rounding)
                else:
                    left_border = x1
                    x = (left_border + right_border) / 2
                    return round(x, rounding), round(function(x), rounding)

        else:
            left_border = x1
            step_counter += 1

            if step_counter != number_of_calculations - 1:
                x1 = x2
                x2 = right_border - localization_segment_length * fibonacci_numbers[
                    number_of_calculations - 1 - step_counter]
            else:
                x2 = x1 + EPSILON

                if function(x1) < function(x2):
                    right_border = x1
                    x = (left_border + right_border) / 2
                    return round(x, rounding), round(function(x), rounding)
                else:
                    left_border = x1
                    x = (left_border + right_border) / 2
                    return round(x, rounding), round(function(x), rounding)


# ===============================================================================================================

def _clear():
    for item in canvas.get_tk_widget().find_all():
        canvas.get_tk_widget().delete(item)


def plot(left_border, right_border):
    global canvas, plot1
    fig = Figure(figsize=(4.96, 4.96), dpi=100)

    index = 0
    list_x = []
    list_y = []

    x = left_border
    while x < right_border:
        func = function(x)
        list_x.insert(index, x)
        list_y.insert(index, func)
        index += 1
        x += 0.1

    plot1 = fig.add_subplot(111)

    plot1.plot(list_x, list_y, color='r')
    if left_border <= 0:
        plot1.vlines(0, min(list_y), max(list_y))
    plot1.hlines(0, left_border, right_border)

    canvas = FigureCanvasTkAgg(fig, master=graph_frame_)
    canvas.draw()

    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, graph_frame_)
    toolbar.update()
    canvas.get_tk_widget().pack()


def start_calculation():
    global rounding, acceptable_length, graph_frame_
    ent_answer_x.delete(0, END)
    ent_answer_func.delete(0, END)

    graph_frame_ = Frame(common_frame, width=496, height=496, relief=GROOVE, borderwidth=2)
    graph_frame_.place(x=2, y=102)

    fig = Figure(figsize=(4.96, 4.96), dpi=100)
    canvas = FigureCanvasTkAgg(fig, master=graph_frame_)
    canvas.draw()
    canvas.get_tk_widget().place(x=0, y=0)

    try:
        left_border = float((ent_left_border.get()).replace(",", ".").replace(" ", ""))
        function(left_border)
        right_border = float((ent_right_border.get()).replace(",", ".").replace(" ", ""))
        EPSILON = float((ent_epsilon.get()).replace(",", ".").replace(" ", ""))
        acceptable_length = float((ent_length.get()).replace(",", ".").replace(" ", ""))
        rounding = int((ent_rounding.get()).replace(" ", ""))

    except SyntaxError:
        messagebox.showerror("Ошибка!", "Проверьте введённую функцию!")
    except ValueError:
        messagebox.showerror("Ошибка!", "Проверьте введённые значения!")
    else:
        plot(left_border, right_border)
        if r_var.get() == 0:
            ent_answer_x.insert(0, method_of_half_division(left_border, right_border, EPSILON)[0])
            ent_answer_func.insert(0, method_of_half_division(left_border, right_border, EPSILON)[1])
        if r_var.get() == 1:
            ent_answer_x.insert(0, golden_ratio_method(left_border, right_border, EPSILON)[0])
            ent_answer_func.insert(0, golden_ratio_method(left_border, right_border, EPSILON)[1])
        if r_var.get() == 2:
            ent_answer_x.insert(0, method_Fibonacci_numbers(left_border, right_border, EPSILON, acceptable_length)[0])
            ent_answer_func.insert(0, method_Fibonacci_numbers(left_border, right_border, EPSILON,
                                                               acceptable_length)[1])
        return 0


def work_window():
    global r_var, ent_func, ent_left_border, ent_right_border, ent_epsilon, ent_answer_x, \
           ent_answer_func, ent_length, ent_rounding, graph_frame, canvas, common_frame, graph_frame
    window = Tk()
    window.title("Поиск минимума функции")
    window.iconbitmap("ico/ico_func.ico")

    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - 400
    h = h - 300
    window.geometry('800x600+{}+{}'.format(w, h))
    window.resizable(False, False)

    common_frame = Frame(window, width=800, height=600)
    common_frame.place(relx=0, rely=0)

    top_frame = Frame(common_frame, width=800, height=100)
    top_frame.place(x=0, y=0)

    func_frame = Frame(top_frame, width=330, height=94, relief=GROOVE, borderwidth=2)
    func_frame.place(x=20, y=3)

    lbl_func = Label(func_frame, text="Введите функцию", font=("Century Gothic", 18), width=0, height=0)
    lbl_func.place(x=52, y=5)

    ent_func = Entry(func_frame, font=("Century Gothic", 15))
    ent_func.place(x=20, y=55, width=290, height=30)
    ent_func.insert(0, 'x^3 - 3*x^2 + 2.5')

    border_frame = Frame(top_frame, width=290, height=94, relief=GROOVE, borderwidth=2)
    border_frame.place(x=370, y=3)

    lbl_border = Label(border_frame, text="левая;правая границы", font=("Century Gothic", 18), width=0, height=0)
    lbl_border.place(x=5, y=5)

    ent_left_border = Entry(border_frame, font=("Century Gothic", 15))
    ent_left_border.place(x=65, y=55, width=80, height=30)
    ent_left_border.insert(0, '1')

    lbl_between_border = Label(border_frame, text=";", font=("Century Gothic", 25), width=0, height=0)
    lbl_between_border.place(x=130, y=41)

    ent_right_border = Entry(border_frame, font=("Century Gothic", 15))
    ent_right_border.place(x=145, y=55, width=80, height=30)
    ent_right_border.insert(0, '3')

    epsilon_frame = Frame(top_frame, width=100, height=94, relief=GROOVE, borderwidth=2)
    epsilon_frame.place(x=680, y=3)

    lbl_epsilon = Label(epsilon_frame, text="ε", font=("Century Gothic", 21), width=0, height=0)
    lbl_epsilon.place(x=42, y=0)

    ent_epsilon = Entry(epsilon_frame, font=("Century Gothic", 15))
    ent_epsilon.place(x=7, y=55, width=80, height=30)
    ent_epsilon.insert(0, '0.2')

    control_frame = Frame(common_frame, width=296, height=496, relief=GROOVE, borderwidth=2)
    control_frame.place(x=502, y=102)

    r_var = IntVar()
    r_var.set(0)
    r_half_division = Radiobutton(control_frame, text="Метод половинного\nделения", font=("Century Gothic", 15),
                                  variable=r_var, value=0)
    r_golden_ratio = Radiobutton(control_frame, text="Метод \"золотого\" \ncечения", font=("Century Gothic", 15),
                                 variable=r_var, value=1)
    r_fibonacci_numbers = Radiobutton(control_frame, text="Метод чисел Фибоначчи", font=("Century Gothic", 15),
                                      variable=r_var, value=2)

    r_half_division.place(x=10, y=40)
    r_golden_ratio.place(x=10, y=110)
    r_fibonacci_numbers.place(x=10, y=180)

    lbl_length = Label(control_frame, text="Конечный интервал\nнеопределённости", font=("Century Gothic", 13))
    lbl_length.place(x=45, y=205)

    ent_length = Entry(control_frame, font=("Century Gothic", 15))
    ent_length.place(x=220, y=216, width=60, height=30)
    ent_length.insert(0, '0.1')

    btn_start = Button(control_frame, text="Вычислить", font=("Century Gothic", 15), command=start_calculation)
    btn_start.place(x=85, y=285)

    answer_frame = Frame(control_frame, width=280, height=150, relief=GROOVE, borderwidth=2, )
    answer_frame.place(x=6, y=338)

    lbl_answer = Label(answer_frame, text="Ответ округлить до", font=("Century Gothic", 17), width=0, height=0)
    lbl_answer.place(x=0, y=0)

    ent_rounding = Entry(answer_frame, font=("Century Gothic", 18))
    ent_rounding.place(x=230, y=3, width=30, height=30)
    ent_rounding.insert(0, '4')

    lbl_answer_x = Label(answer_frame, text="x =", font=("Century Gothic", 18), width=0, height=0)
    lbl_answer_x.place(x=20, y=45)

    ent_answer_x = Entry(answer_frame, font=("Century Gothic", 15))
    ent_answer_x.place(x=80, y=45, width=180, height=35)

    lbl_answer_func = Label(answer_frame, text="f(x) =", font=("Century Gothic", 18), width=0, height=0)
    lbl_answer_func.place(x=10, y=95)

    ent_answer_func = Entry(answer_frame, font=("Century Gothic", 15))
    ent_answer_func.place(x=80, y=95, width=180, height=35)

    window.mainloop()


work_window()
