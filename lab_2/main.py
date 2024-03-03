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


def method_gradient_descent_constant_step(M_, x1_, x2_, eps1_, eps2_, k_, flag_, t_):
    print('Gradient descent with a constant step')
    while True:
        count_t = 0
        print('k =', k_, '; x1 =', round(x1_, 5), ', x2 =', round(x2_, 5))

        print('===================================================================', )
        if flag_ == 2:
            print('  X(k) и X(k-1) подходят')
            print('  Ответ: x1 =', round(x1_, 5), '; x2 =', round(x2_, 5), '; func = ', round(function(x1_, x2_), 5))
            break
        else:
            grad_x1 = gradient_x1(x1_, x2_)
            grad_x2 = gradient_x2(x1_, x2_)
            norma_vectora = norm_of_vector(grad_x1, grad_x2)
            print('  gradient = (', round(grad_x1, 5), ':', round(grad_x2, 5), ')  ; norm_vector =',
                  round(norma_vectora, 5))
            if norma_vectora < eps1_:
                print('  norm_vector < eps1')
                print()
                print('-' * 64)
                print('  Ответ: x1 =', round(x1_, 5), '; x2 =', round(x2_, 5), '; func = ',
                      round(function(x1_, x2_), 5))
                break
            else:
                if k_ >= M_:
                    'k >= M'
                    print('  Ответ: x1 =', round(x1_, 5), '; x2 =', round(x2_, 5), '; func = ',
                          round(function(x1_, x2_), 5))
                    break
                else:
                    while True:
                        count_t += 1
                        print('    ', count_t, '. t =', t_)
                        x1_next = x1_ - t_ * grad_x1
                        x2_next = x2_ - t_ * grad_x2

                        print('      X(k+1) = (', round(x1_next, 5), ':', round(x2_next, 5), ')')
                        print('      f(X(k+1)) = ', round(function(x1_next, x2_next), 5))
                        print('      f(x) =', round(function(x1_, x2_), 5))
                        if function(x1_next, x2_next) - function(x1_, x2_) < 0:
                            print('    f(X(k+1)) - f(X) < 0')
                            break
                        else:
                            print('      f(X(k+1) - f(X) > 0')
                            t_ = t_ / 2
                            print('    ', '*' * 10)

                    for_norm_vector_x1 = x1_next - x1_
                    for_norm_vector_x2 = x2_next - x2_
                    if abs(function(x1_next, x2_next) - function(x1_, x2_)) < eps2_ and \
                            norm_of_vector(for_norm_vector_x1, for_norm_vector_x2) < eps2_:
                        print('  ||X(k+1) -X(k)|| < eps2 and f(X(k+1) - f(X) < eps2')
                        flag_ += 1
                        print('  flag = ', flag_)
                    else:
                        print('  ||X(k+1) -X(k)|| > eps2 or f(X(k+1) - f(X) > eps2')
                        flag_ = 0
                        print('  flag = ', flag_)
                    k_ += 1
                    x1_ = x1_next
                    x2_ = x2_next
                    print('=' * 64)
                    print()


if __name__ == '__main__':
    x1 = 0
    x2 = 0.5

    eps1 = 0.15
    eps2 = 0.2

    M = 10

    k = 0
    flag = 0
    t = 1

    method_gradient_descent_constant_step(M, x1, x2, eps1, eps2, k, flag, t)
