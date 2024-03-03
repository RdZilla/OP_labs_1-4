from colorama import Fore, Style


def function(x1_, x2_):
    func_ = 2 * x1_ ** 2 + 0.1 * x1_ * x2_ + 2 * x2_ ** 2
    return func_


def gradient_x1(x1_, x2_):
    grad_x1_ = 4 * x1_ + 0.1 * x2_
    return grad_x1_


def gradient_x2(x1_, x2_):
    grad_x2_ = 0.1 * x1_ + 4 * x2_
    return grad_x2_


def norm_of_vector(x1_, x2_):
    norm_x_ = (x1_ ** 2 + x2_ ** 2) ** (1 / 2)
    return norm_x_


def method_newton(M_, x1_, x2_, eps1_, eps2_, k_, flag_):
    while True:
        print('k =', k_, '; x1 =', round(x1_, 5), ', x2 =', round(x2_, 5))

        print('=' * 64)
        if flag_ == 2:
            print('  X(k) и X(k-1) подходят')
            print()
            print(Fore.RED + '-' * 64 + Style.RESET_ALL)
            print(Fore.RED + '  Ответ: ' + Style.RESET_ALL + 'x1 =', round(x1_, 5), '; x2 =',
                  round(x2_, 5), '; func = ', round(function(x1_, x2_), 5))
            break
        else:
            grad_x1 = gradient_x1(x1_, x2_)
            grad_x2 = gradient_x2(x1_, x2_)
            norma_vectora = norm_of_vector(grad_x1, grad_x2)
            print('  gradient = (' + str(round(grad_x1, 5)) + ';' + str(round(grad_x2, 5)) + ')')
            print('  norm_vector =', round(norma_vectora, 5))
            if norma_vectora < eps1_:
                print('  norm_vector < eps1' + Fore.RED + ' < ' + str(eps1_) + Style.RESET_ALL)
                print()
                print(Fore.RED + '-' * 64 + Style.RESET_ALL)
                print(Fore.RED + '  Ответ: ' + Style.RESET_ALL + 'x1 =', round(x1_, 5), '; x2 =',
                      round(x2_, 5), '; func = ', round(function(x1_, x2_), 5))
                break
            else:
                print('  norm_vector >= eps1' + Fore.RED + ' >= ' + str(eps1) + Style.RESET_ALL)
                if k_ >= M_:
                    print('k >= M')
                    print()
                    print(Fore.RED + '-' * 64 + Style.RESET_ALL)
                    print(Fore.RED + '  Ответ: ' + Style.RESET_ALL + 'x1 =', round(x1_, 5), '; x2 =',
                          round(x2_, 5), '; func = ', round(function(x1_, x2_), 5))
                    break
                else:
                    matrix_h_main_diagonal = 0.25
                    matrix_h_secondary_diagonal = -0.006

                    matrix_h_delta_1 = matrix_h_main_diagonal
                    matrix_h_delta_2 = matrix_h_main_diagonal ** 2 - matrix_h_secondary_diagonal ** 2
                    print('  determinant 1 =', matrix_h_delta_1)
                    print('  determinant 2 =', matrix_h_delta_2)
                    print()

                    if matrix_h_delta_1 > 0 and matrix_h_delta_2 > 0:
                        print('  del1 > 0 and del2 > 0')
                        d1 = (matrix_h_main_diagonal * gradient_x1(x1_, x2_) + matrix_h_secondary_diagonal *
                              gradient_x2(x1_, x2_)) * -1
                        d2 = (matrix_h_secondary_diagonal * gradient_x1(x1_, x2_) + matrix_h_main_diagonal *
                              gradient_x2(x1_, x2_)) * -1
                        print('    d1 =', d1)
                        print('    d2= ', d2)
                        x1_next = x1_ + d1
                        x2_next = x2_ + d2
                        print('    x1_next =', round(x1_next, 4))
                        print('    x2_next =', round(x2_next, 4))
                    else:
                        left_border = 0
                        right_border = 0
                        eps_t = 0.15

                        # delta = abs(right_border - left_border)

                        while True:
                            y = left_border + (right_border - left_border) * (3 - 5 ** 0.5) / 2
                            z = left_border + right_border - y

                            if function(y) > function(z):
                                left_border = y
                                y = z
                                z = left_border + right_border - y
                            else:
                                right_border = z
                                z = y
                                y = left_border + right_border - z
                            delta = abs(right_border - left_border)

                            if delta <= eps_t:
                                t = (left_border + right_border) / 2
                                break
                        print('t =', t)
                        x1_next = x1_ - t * gradient_x1(x1_, x2_)
                        x2_next = x2_ - t * gradient_x2(x1_, x2_)
                        print('x1_next =', x1_next)
                        print('x2_next =', x2_next)

                    for_norm_vector_x1 = x1_next - x1_
                    for_norm_vector_x2 = x2_next - x2_

                    if abs(function(x1_next, x2_next) - function(x1_, x2_)) < eps2_ and \
                            norm_of_vector(for_norm_vector_x1, for_norm_vector_x2) < eps2_:
                        print('  ||X(k+1) -X(k)|| < eps2 ' + Fore.RED + 'and' + Style.RESET_ALL
                              + ' f(X(k+1) - f(X) < eps2' + Fore.RED + ' < ' + str(eps2_) + Style.RESET_ALL)

                        flag_ += 1
                        print('  flag =', flag_)
                    else:
                        print('  ||X(k+1) -X(k)|| > eps2 ' + Fore.RED + 'or' + Style.RESET_ALL
                              + ' f(X(k+1) - f(X) > eps2' + Fore.RED + ' > ' + str(eps2_) + Style.RESET_ALL)

                        flag_ = 0
                        print('  flag = ', flag_)
                    k_ += 1
                    x1_ = x1_next
                    x2_ = x2_next
                    print(Fore.YELLOW + '=' * 64 + Style.RESET_ALL)
                    print()


if __name__ == '__main__':
    x1 = 1.5
    x2 = 0.5

    eps1 = 0.15
    eps2 = 0.2

    M = 10

    k = 0
    flag = 0
    print()
    print(Fore.CYAN + Style.BRIGHT + ' ' * 24 + 'Newton\'s method' + Style.RESET_ALL)
    print('\n')
    method_newton(M, x1, x2, eps1, eps2, k, flag)
