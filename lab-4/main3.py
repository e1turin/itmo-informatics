import main as MAIN
import main2 as MAIN2
import main1 as MAIN1


def benchmark(iters: int = 1):
    """ Decorator for benchmarking functions with some iterations """
    def actual_decorator(func: 'function') -> 'function':
        import time

        def wrapper(*args, **kwargs):
            total = 0
            return_value = None
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total += end - start

            print("function: ", func.__name__)
            print('[*] Среднее ремя выполнения за {} итераций: {:.5} секунд x10.'.format(iters, total / iters * 10))
            return return_value

        return wrapper

    return actual_decorator


@benchmark(iters=100)
def benchfunc(func):
    func()


def main():
    print()
    print("Тестируем реализацию 0:")
    benchfunc(MAIN.main)

    print()
    print("Тестируем реализацию 2:")
    benchfunc(MAIN2.main)

    print('\n------------------------\n')
    print("Тестируем реализацию 1:")
    benchfunc(MAIN1.main)


if __name__ == "__main__":
    main()
