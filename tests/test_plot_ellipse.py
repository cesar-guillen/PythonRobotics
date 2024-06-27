import unittest
import numpy as np
import matplotlib.pyplot as plt
from utils.plot import plot_ellipse, coverage_tracker

class TestPlotEllipse(unittest.TestCase):
    def test_plot_ellipse(self):
        fig, ax = plt.subplots()
        plot_ellipse(0, 0, 1, 0.5, np.pi/4, ax=ax)
        plt.close(fig)

    def test_plot_ellipse_with_different_params(self):
        fig, ax = plt.subplots()
        plot_ellipse(1, 1, 2, 1, np.pi/6, color='-b', ax=ax)
        plt.close(fig)

    def test_plot_ellipse_no_ax(self):
        plot_ellipse(0, 0, 1, 0.5, np.pi/4)

    def test_plot_ellipse_different_params_no_ax(self):
        plot_ellipse(1, 1, 2, 1, np.pi/6, color='-b')

    def test_coverage_tracker(self):
        plot_ellipse(0, 0, 1, 0.5, np.pi/4)
        plot_ellipse(1, 1, 2, 1, np.pi/6)
        self.assertTrue('plot_ellipse_entered' in coverage_tracker)
        self.assertTrue('plot_ellipse_no_ax' in coverage_tracker or 'plot_ellipse_with_ax' in coverage_tracker)

if __name__ == '__main__':
    unittest.main()
