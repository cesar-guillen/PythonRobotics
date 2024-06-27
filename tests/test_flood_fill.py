import numpy as np
import conftest
from collections import deque
from Mapping.lidar_to_grid_map.lidar_to_grid_map import init_flood_fill, flood_fill, bresenham
from Mapping.lidar_to_grid_map import branch_coverage

def print_coverage():
    hit_branches = sum(branch_coverage.values())
    total_branches = len(branch_coverage)
    coverage_percentage = (hit_branches/total_branches) * 100
    for branch, hit in branch_coverage.items():
        if hit:
            print(f"{branch} was {'hit' if hit else 'not hit'}")
        print(f"Coverage: {coverage_percentage:.2f}%")


def test_init_flood_fill():
    # Define parameters for the test
    center_point = (5, 5)
    obstacle_points = (np.array([8, 8, 8, 5, 2, 2, 2, 5]), np.array([2, 5, 8, 8, 8, 5, 2, 2]))
    xy_points = (10, 10)
    min_coord = (0, 0)
    xy_resolution = 1

    # Expected occupancy map
    expected_map = np.ones((10, 10)) * 0.5
    for (x, y) in zip(obstacle_points[0], obstacle_points[1]):
        ix = int(round((x - min_coord[0]) / xy_resolution))
        iy = int(round((y - min_coord[1]) / xy_resolution))
        free_area = bresenham((4, 5), (ix, iy))
        for fa in free_area:
            expected_map[fa[0]][fa[1]] = 0.0
        expected_map[ix][iy] = 0.5

    # Run the function
    occupancy_map = init_flood_fill(center_point, obstacle_points, xy_points, min_coord, xy_resolution)

    # Print actual occupancy map for debugging
    print("Actual Occupancy Map After init_flood_fill:")
    print(occupancy_map)

    # Check the result
    assert np.array_equal(occupancy_map, expected_map), "init_flood_fill did not produce the expected result."

def test_flood_fill():
    # Define parameters for the test
    center_point = (5, 5)
    occupancy_map = np.ones((10, 10)) * 0.5
    occupancy_map[5, 5] = 0.0

    # Expected occupancy map after flood fill
    expected_map = np.ones((10, 10)) * 0.5
    for i in range(10):
        for j in range(10):
            expected_map[i, j] = 0.0
    expected_map[0, 0] = 0.5

    # Run the function
    flood_fill(center_point, occupancy_map)

    # Print actual occupancy map for debugging
    print("Actual Occupancy Map After flood_fill:")
    print(occupancy_map)

    # Expected occupancy map after flood fill
    expected_map = np.ones((10, 10)) * 0.0  # Assuming flood_fill sets all connected 0.5 cells to 0.0
    expected_map[0, 0] = 0.5  # Since (0, 0) was set to 0.5 and should not change

    # Check the result
    assert np.array_equal(occupancy_map, expected_map), "flood_fill did not produce the expected result."

def test_print_coverage():
    print('')
    print_coverage()

if __name__ == '__main__':
    conftest.run_this_test(__file__)
