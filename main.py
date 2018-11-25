import time
import numpy as np
import matplotlib.pyplot as plt
import config
from algorithms import *
from sys import argv

if __name__ == '__main__':
    points = np.random.rand(config.N, 2)
    bf_results = []
    gw_results = []
    qh_results = []
    if '-v' in argv or '--visual' in argv:
        config.visual = True

    if config.visual:
        print("Running with visual mode\n")
        plt.xlabel('X')
        plt.ylabel('Y')
        config.timer = plt.text(0.9, 1, "")

        init_plot(points)
       
    if config.run_brute_force:
        print("Solving with Brute Force Algorithm")
        if config.visual:
            reset_plot('Brute Force')
        start_time = time.time()
        bf_results = brute_force(points, start_time)
        end_time = time.time() - start_time

        print("Solved in %.2f seconds\n" % end_time)

    if config.run_gift_wrap:
        print("Solving with Gift Wrapping Algorithm")
        if config.visual:
            reset_plot('Gift Wrapping')
        start_time = time.time()
        gw_results = gift_wrap(points, start_time)
        end_time = time.time() - start_time

        print("Solved in %.2f seconds\n" % end_time)

    if config.run_quickhull:
        print("Solving with Quickhull Algorithm")
        if config.visual:
            reset_plot('Quickhull')
        start_time = time.time()
        qh_results = quickhull(points, start_time)
        end_time = time.time() - start_time

        print("Solved in %.2f seconds\n" % end_time)


    # We don't have to do the below comparisons
    if config.run_brute_force and config.run_gift_wrap:
        print("Brute Force and Gift Wrapping comparision:")
        if all(i in bf_results for i in gw_results):
            print("\tResults match!")
        else:
            print("\tResults don't match!")

    if config.run_brute_force and config.run_quickhull:
        print("Brute Force and Quickhull comparision:")
        if all(i in bf_results for i in qh_results):
            print("\tResults match!")
        else:
            print("\tResults don't match!")

    if config.run_gift_wrap and config.run_quickhull:
        print("Gift Wrapping and Quickhull comparision:")
        if gw_results == qh_results:
            print("\tResults match!")
        else:
            print("\tResults don't match!")

    if config.visual:
        plt.show()
