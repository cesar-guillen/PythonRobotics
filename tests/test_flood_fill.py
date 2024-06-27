import numpy as np
import conftest
import math
import unittest
from collections import deque
from Mapping.lidar_to_grid_map.lidar_to_grid_map import flood_fill, init_flood_fill, calc_grid_map_config
from Mapping.lidar_to_grid_map.lidar_to_grid_map import branch_coverage
from Mapping.lidar_to_grid_map.branch_coverage import branch_coverage_2
from PathTracking.lqr_speed_steer_control.lqr_speed_steer_control import State, update, dt, L, max_steer

class TestMappingAndPathTracking(unittest.TestCase):

    def print_coverage_1():
        hit_branches = sum(branch_coverage.values())
        total_branches = len(branch_coverage)
        coverage_percentage = (hit_branches/total_branches) * 100
        for branch, hit in branch_coverage.items():
            if hit:
                print(f"{branch} was {'hit' if hit else 'not hit'}")
            print(f"Coverage: {coverage_percentage:.2f}%")

    def print_coverage_2():
        hit_branches = sum(branch_coverage_2.values())
        total_branches = len(branch_coverage_2)
        coverage_percentage = (hit_branches/total_branches) * 100
        for branch, hit in branch_coverage_2.items():
            if hit:
                print(f"{branch} was {'hit' if hit else 'not hit'}")
            print(f"Coverage: {coverage_percentage:.2f}%")

    def setUp(self):
            self.xy_resolution = 1.0
            self.ox = np.array([1, 2, 2, 3, 3, 4])
            self.oy = np.array([1, 1, 2, 2, 3, 3])
            self.min_x, self.min_y, self.max_x, self.max_y, self.xw, self.yw = calc_grid_map_config(self.ox, self.oy, self.xy_resolution)
            self.center_point = (int(round(-self.min_x / self.xy_resolution)), int(round(-self.min_y / self.xy_resolution)))
            self.occupancy_map = init_flood_fill(self.center_point, (self.ox, self.oy), (self.xw, self.yw), (self.min_x, self.min_y), self.xy_resolution)
    
    def test_flood_fill(self):
        result_map = self.occupancy_map.copy()
        flood_fill(self.center_point, result_map)

        expected_map = self.occupancy_map.copy()
        fringe = deque()
        fringe.appendleft(self.center_point)
        while fringe:
            n = fringe.pop()
            nx, ny = n
            if nx > 0 and expected_map[nx - 1, ny] == 0.5:
                expected_map[nx - 1, ny] = 0.0
                fringe.appendleft((nx - 1, ny))
            if nx < expected_map.shape[0] - 1 and expected_map[nx + 1, ny] == 0.5:
                expected_map[nx + 1, ny] = 0.0
                fringe.appendleft((nx + 1, ny))
            if ny > 0 and expected_map[nx, ny - 1] == 0.5:
                expected_map[nx, ny - 1] = 0.0
                fringe.appendleft((nx, ny - 1))
            if ny < expected_map.shape[1] - 1 and expected_map[nx, ny + 1] == 0.5:
                expected_map[nx, ny + 1] = 0.0
                fringe.appendleft((nx, ny + 1))

        np.testing.assert_array_almost_equal(result_map, expected_map, err_msg="Flood fill did not fill correctly.")

    def test_no_flood_fill_obstacle(self):
        self.occupancy_map[self.center_point[0], self.center_point[1]] = 1.0
        original_map = self.occupancy_map.copy()

        result_map = self.occupancy_map.copy()
        flood_fill(self.center_point, result_map)

        np.testing.assert_array_equal(result_map, original_map, "Flood fill should not alter map when starting point is an obstacle.")


    def test_update_delta_within_range_1(self):
        state = State(x=0.0, y=0.0, yaw=0.0, v=1.0)
        a = 0.1
        delta = 0.0
        new_state = update(state, a, delta)
        self.assertAlmostEqual(new_state.x, state.x + state.v * math.cos(state.yaw) * dt)
        self.assertAlmostEqual(new_state.y, state.y + state.v * math.sin(state.yaw) * dt)
        self.assertAlmostEqual(new_state.yaw, state.yaw + state.v / L * math.tan(delta) * dt)
        self.assertAlmostEqual(new_state.v, state.v + a * dt)
        self.print_coverage_2()

    def test_update_delta_within_range_2(self):
        state = State(x=0.0, y=0.0, yaw=0.0, v=1.0)
        a = 0.0
        delta = math.radians(30)
        new_state = update(state, a, delta)
        self.assertAlmostEqual(new_state.x, state.x + state.v * math.cos(state.yaw) * dt)
        self.assertAlmostEqual(new_state.y, state.y + state.v * math.sin(state.yaw) * dt)
        self.assertAlmostEqual(new_state.yaw, state.yaw + state.v / L * math.tan(delta) * dt)
        self.assertAlmostEqual(new_state.v, state.v + a * dt)
        self.print_coverage_2()

    def test_update_delta_exceeds_max_steer_1(self):
        state = State(x=0.0, y=0.0, yaw=0.0, v=1.0)
        a = 0.0
        delta = math.radians(60) 
        new_state = update(state, a, delta)
        self.assertAlmostEqual(new_state.x, state.x + state.v * math.cos(state.yaw) * dt)
        self.assertAlmostEqual(new_state.y, state.y + state.v * math.sin(state.yaw) * dt)
        self.assertAlmostEqual(new_state.yaw, state.yaw + state.v / L * math.tan(max_steer) * dt)
        self.assertAlmostEqual(new_state.v, state.v + a * dt)
        self.print_coverage_2()

    def test_update_delta_exceeds_max_steer_2(self):
        state = State(x=0.0, y=0.0, yaw=0.0, v=1.0)
        a = 0.0
        delta = math.radians(60) 
        new_state = update(state, a, delta)
        self.assertAlmostEqual(new_state.x, state.x + state.v * math.cos(state.yaw) * dt)
        self.assertAlmostEqual(new_state.y, state.y + state.v * math.sin(state.yaw) * dt)
        self.assertAlmostEqual(new_state.yaw, state.yaw + state.v / L * math.tan(max_steer) * dt)
        self.assertAlmostEqual(new_state.v, state.v + a * dt)
        self.print_coverage_2()

    def test_update_delta_negative_1(self):
        state = State(x=0.0, y=0.0, yaw=0.0, v=-1.0)
        a = -0.1
        delta = 0.0
        new_state = update(state, a, delta)
        self.assertAlmostEqual(new_state.x, state.x + state.v * math.cos(state.yaw) * dt)
        self.assertAlmostEqual(new_state.y, state.y + state.v * math.sin(state.yaw) * dt)
        self.assertAlmostEqual(new_state.yaw, state.yaw + state.v / L * math.tan(delta) * dt)
        self.assertAlmostEqual(new_state.v, state.v + a * dt)
        self.print_coverage_2()

    def test_update_delta_negative_2(self):
        state = State(x=0.0, y=0.0, yaw=0.0, v=-1.0)
        a = -0.1
        delta = 0.0
        new_state = update(state, a, delta)
        self.assertAlmostEqual(new_state.x, state.x + state.v * math.cos(state.yaw) * dt)
        self.assertAlmostEqual(new_state.y, state.y + state.v * math.sin(state.yaw) * dt)
        self.assertAlmostEqual(new_state.yaw, state.yaw + state.v / L * math.tan(delta) * dt)
        self.assertAlmostEqual(new_state.v, state.v + a * dt)
        self.print_coverage_2()

    # def test_print_coverage():
    #     print('')
    #     print_coverage_1()
    #     print_coverage_2()

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     conftest.run_this_test(__file__)
