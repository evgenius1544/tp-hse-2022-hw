import time
import app.main as m


def get_test_work_time(to_visual: bool = False) -> None:
    """
    get_test_work_time
        Gets work (real) time for each test.
    """

    elements_time = []

    for count in [i for i in range(0, 1000000 + 1, 10000)][1:]:
        time_start = time.time()
        m.main(f"./tests/test_el_{count}.txt")
        time_end = time.time()

        work_time = time_end - time_start

        elements_time.append((count, work_time))

        print(f"Time for {count} elements:", work_time)

    if to_visual:
        from matplotlib import pyplot as plt

        plt.plot(*zip(*elements_time))
        plt.xlabel("elements")
        plt.ylabel("time")
        plt.show()


if __name__ == "__main__":
    get_test_work_time(to_visual=True)
