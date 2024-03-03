from sympy import diff


def function(x1_, x2_):
    string_function_f = 'x1**2 + 2*x2**2'
    func_ = eval(string_function_f, {'x1': x1_, 'x2': x2_})
    return func_


def composing_function_p_penalty_method(r_):
    string_function_f = 'x1**2 + 2*x2**2'
    string_function_g = '3*x1 + x2 - 2'
    string_function_p = string_function_f + " + " + str(r_ / 2) + "*(" + string_function_g + ")**2"
    return string_function_p


def composing_function_p_barrier_method(r_):
    string_function_f = 'x1**2 + 2*x2**2'
    string_function_g = '3*x1 + x2 - 2'
    string_function_p = string_function_f + " - " + str(r_) + "/(" + string_function_g + ")"
    return string_function_p


def count_function_p(string_function_p, x1_, x2_):
    func_p = eval(string_function_p, {'x1': x1_, 'x2': x2_})
    return func_p


def final_count_func_p_penalty_method(r_, x1_, x2_):
    string_function_g = '3*x1 + x2 - 2'
    string = f'{r_ / 2} * ({string_function_g})**2'
    answer = eval(string, {'x1': x1_, 'x2': x2_})
    return answer


def final_count_func_p_barrier_method(r_, x1_, x2_):
    string_function_g = '3*x1 + x2 - 2'
    string = f'{r_} / ({string_function_g})'
    answer = eval(string, {'x1': x1_, 'x2': x2_})
    return answer


def composing_function_grad_x1(string_function_p):
    string_grad_x1 = str(diff(string_function_p, 'x1'))
    return string_grad_x1


def composing_function_grad_x2(string_function_p):
    string_grad_x2 = str(diff(string_function_p, 'x2'))
    return string_grad_x2


def gradient_x1(string_grad_x1, x1_, x2_):
    grad_x1_ = eval(string_grad_x1, {'x1': x1_, 'x2': x2_})
    return grad_x1_


def gradient_x2(string_grad_x2, x1_, x2_):
    grad_x2_ = eval(string_grad_x2, {'x1': x1_, 'x2': x2_})
    return grad_x2_


def norm_of_vector(x1_, x2_):
    norm_x_ = (x1_ ** 2 + x2_ ** 2) ** (1 / 2)
    return norm_x_


def method_gradient_descent_constant_step(string_function_p, x1_, x2_, t_):
    set_value_m_ = 10
    eps1_ = 0.15
    eps2_ = 0.2
    k_ = 0
    flag_ = 0
    print(f'    |       | M = {set_value_m_}, eps1 = {eps1_}, eps2 = {eps2_}, x = ({round(x1_, 4)};{round(x2_, 4)})')
    print('    |       |', '-' * 64)
    while True:
        count_t = 0
        print('    |       | k =', k_, '; x1 =', round(x1_, 5), ', x2 =', round(x2_, 5))

        print('    |       |', '=' * 64)
        if flag_ == 2:
            print('    |       |   X(k) и X(k-1) подходят')
            print('    |       |   Ответ: x1 =', round(x1_, 5), '; x2 =', round(x2_, 5), '; func = ',
                  round(count_function_p(string_function_p, x1_, x2_), 5))
            break
        else:
            string_grad_x1 = composing_function_grad_x1(string_function_p)
            string_grad_x2 = composing_function_grad_x2(string_function_p)
            grad_x1 = gradient_x1(string_grad_x1, x1_, x2_)
            grad_x2 = gradient_x2(string_grad_x2, x1_, x2_)
            norma_vectors = norm_of_vector(grad_x1, grad_x2)
            print('    |       |   gradient = (', round(grad_x1, 5), ':', round(grad_x2, 5), ')  ; norm_vector =',
                  round(norma_vectors, 5))
            if norma_vectors < eps1_:
                print('    |       |   norm_vector < eps1')
                print()
                print('    |       | ', '-' * 64)
                print('    |       |   Ответ: x1 =', round(x1_, 5), '; x2 =', round(x2_, 5), '; func = ',
                      round(count_function_p(string_function_p, x1_, x2_), 5))
                break
            else:
                if k_ >= set_value_m_:
                    print('    |       | k >= M')
                    print('    |       |   Ответ: x1 =', round(x1_, 5), '; x2 =', round(x2_, 5), '; func = ',
                          round(count_function_p(string_function_p, x1_, x2_), 5))
                    break
                else:
                    while True:
                        count_t += 1
                        print('    |       |     ', count_t, '. t =', t_)
                        x1_next = x1_ - t_ * grad_x1
                        x2_next = x2_ - t_ * grad_x2

                        print('    |       |       X(k+1) = (', round(x1_next, 5), ':', round(x2_next, 5), ')')
                        print('    |       |       f(X(k+1)) = ', round(count_function_p(string_function_p,
                                                                                         x1_next, x2_next), 5))
                        print('    |       |       f(x) =', round(count_function_p(string_function_p, x1_, x2_), 5))
                        if count_function_p(string_function_p, x1_next, x2_next) - count_function_p(string_function_p,
                                                                                                    x1_, x2_) < 0:
                            print('    |       |     f(X(k+1)) - f(X) < 0')
                            break
                        else:
                            print('    |       |       f(X(k+1) - f(X) > 0')
                            t_ = t_ / 2
                            print('    |       |    ', '*' * 33)

                    for_norm_vector_x1 = x1_next - x1_
                    for_norm_vector_x2 = x2_next - x2_
                    if abs(count_function_p(string_function_p, x1_next, x2_next) - count_function_p(string_function_p,
                                                                                                    x1_, x2_)) < eps2_ \
                            and norm_of_vector(for_norm_vector_x1, for_norm_vector_x2) < eps2_:
                        print('    |       |   ||X(k+1) -X(k)|| < eps2 and f(X(k+1) - f(X) < eps2')
                        flag_ += 1
                        print('    |       |   flag = ', flag_)
                    else:
                        print('    |       |   ||X(k+1) -X(k)|| > eps2 or f(X(k+1) - f(X) > eps2')
                        flag_ = 0
                        print('    |       |   flag = ', flag_)
                    k_ += 1
                    x1_ = x1_next
                    x2_ = x2_next
                    print('    |       |', '=' * 64)
                    print('    |       |')
    return x1_, x2_, t_


def penalty_method(eps, r0, step_changing_r):
    r = r0
    x1 = 0.5
    x2 = 0
    k = 0
    t = 0.25
    print(f'\n    | Начальные условия: {r = }, C = {step_changing_r}, {eps = }, x0 = ({x1};{x2})')
    while True:
        print('    | ' + '~' * 64, f'\n    | {k = }, {r = }, x = ({round(x1, 4)};{round(x2, 4)})')

        string_function_p = composing_function_p_penalty_method(r)
        print('    | F(x;r0) =', string_function_p)

        print('    | ' + '+_' * 32 + '\n    | Поиск минимума методом градиентного спуска с постоянным шагом')
        print('    | ')
        list_answer_x = method_gradient_descent_constant_step(string_function_p, x1, x2, t)
        x1_new = list_answer_x[0]
        x2_new = list_answer_x[1]
        t = list_answer_x[2]

        print('    | ' + '-' * 64 + '\n' + f'    | x* = ({round(x1_new, 4)};{round(x2_new, 4)})')
        value_func_p = final_count_func_p_penalty_method(r, x1_new, x2_new)
        print('    | P(x(r), r) =', round(value_func_p, 4))
        print('    | ')

        if value_func_p <= eps:
            print(f'    | {round(value_func_p, 5)} < {eps} => конец процесса поиска')

            print('    | ' + '=' * 64 + f'\n'
                                        f'    | Ответ'
                                        f'\n'
                                        f'    | x = ({round(x1_new, 4)};{round(x2_new, 4)})'
                                        f'\n'
                                        f'    | f(x) = {round(function(x1_new, x2_new), 4)}\n' + '    | ' + '=' * 64,
                  '\n')
            break
        else:
            r *= step_changing_r
            k += 1
            x1 = x1_new
            x2 = x2_new
            print(f'    | {round(value_func_p, 2)} > {eps} => r = r*C = {r}, x=({round(x1_new, 4)};{round(x2_new, 4)})')
            print('    | ')
    return 0


def barrier_function_method(eps, r0, step_changing_r):
    r = r0
    x1 = 0.5
    x2 = 0
    k = 0
    t = 0.25
    print(f'\n    | Начальные условия: {r = }, C = {step_changing_r}, {eps = }, x0 = ({x1};{x2})')
    while True:
        print('    | ' + '~' * 64, f'\n    | {k = }, {r = }, x = ({round(x1, 4)};{round(x2, 4)})')

        string_function_p = composing_function_p_barrier_method(r)
        print('    | F(x;r0) =', string_function_p)

        print('    | ' + '+_' * 32, '\n    | Поиск минимума методом градиентного спуска с постоянным шагом')
        print('    | ')
        list_answer_x = method_gradient_descent_constant_step(string_function_p, x1, x2, t)
        x1_new = list_answer_x[0]
        x2_new = list_answer_x[1]
        t = list_answer_x[2]

        print('    | ' + '-' * 64 + '\n' + f'    | x* = ({round(x1_new, 4)};{round(x2_new, 4)})')
        value_func_p = final_count_func_p_barrier_method(r, x1_new, x2_new)
        print('    | P(x(r), r) =', round(value_func_p, 4))

        if abs(value_func_p) <= eps:
            print(f'    | |{round(value_func_p, 5)}| < {eps} => Ответ')
            value_func_q = eval('3*x1 + x2 - 2', {'x1': x1_new, 'x2': x2_new})
            print('    | ' + '=' * 64, f'\n    | Ответ\n'
                                       f'    | x* = ({round(x1_new, 4)};{round(x2_new, 4)})\n'
                                       f'    | f(x*) = {round(function(x1_new, x2_new), 4)}\n'
                                       f'    | q(x*) = {round(value_func_q, 4)} < 0\n' + '    | ' + '=' * 64, '\n')
            break
        else:
            x1 = x1_new
            x2 = x2_new
            r /= step_changing_r
            k += 1
            print(f'    | |{round(value_func_p, 2)}| > {eps} => r = r/C = {r}, '
                  f'x=({round(x1_new, 4)};{round(x2_new, 4)})')
            print('    | ')
    return 0


def start():
    while True:
        try:
            choice = input("\nВведите цифру, соответствующую желаемой функции:\n"
                           "1 - Метод штрафов\n"
                           "2 - Метод барьерных функций\n" +
                           "-" * 28 + "\nexit (или ex) - Выход\n"
                                      ">>> ")
        except KeyboardInterrupt:
            print()
            print('|| ERROR: Программа была остановлена ||')
            print('||  Исполнение программы завершено  ||')
            return

        if choice == '1':
            print('\n\n' + '-_' * 32, '\nМетод штрафов')
            penalty_method(0.05, 1, 5)
        elif choice == '2':
            print('\n\n' + '-_' * 32, '\nМетод барьерных функций')
            barrier_function_method(0.05, 1, 5)
        elif choice == 'exit' or choice == 'ex':
            print('|| Исполнение программы завершено ||')
            return
        else:
            print('|| ERROR: Введите цифру из предложенных, соответствующую желаемой функции ||')


if __name__ == "__main__":
    print("\nМетоды условной оптимизации. Поиск локального минимума функции.\n\n"
          "f(x) = x1**2 + 2*x2**2\n"
          "g(x) = 3*x1 + x2 - 2\n"
          "eps=0.05, r=1, C=5")
    start()
