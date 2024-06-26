import conftest
import numpy as np
from coverage_tracker import branch_coverage, branch_coverage_2
from Mapping.normal_vector_estimation import normal_vector_estimation as m
from PathPlanning.HybridAStar import dynamic_programming_heuristic as n



def print_coverage_1():
    hits = 0
    for branch, hit in branch_coverage.items():
        if hit:
            hits += 1  
        print(f"{branch} was {'hit' if hit else 'not hit'}")
    
    if len(branch_coverage) > 0:
        coverage_percentage = hits / len(branch_coverage) * 100
    else:
        coverage_percentage = 0.0
    print(f"Total function coverage: {coverage_percentage:.2f}%")

def print_coverage_2():
    hits = 0
    for branch, hit in branch_coverage_2.items():
        if hit:
            hits += 1  
        print(f"{branch} was {'hit' if hit else 'not hit'}")
    
    if len(branch_coverage) > 0:
        coverage_percentage = hits / len(branch_coverage_2) * 100
    else:
        coverage_percentage = 0.0
    print(f"Total function coverage: {coverage_percentage:.2f}%")

def test_distance_to_plane_point_on_plane():
    point = np.array([0, 0, 0])
    normal = np.array([0, 0, 0])
    origin = np.array([0, 0, 0])
    result = m.distance_to_plane(point, normal, origin)
    assert result == 0

def test_distance_to_plane_point_on_plane_2():
    point = np.array([2, 1, 3])
    normal = np.array([1, 1, 1])
    origin = np.array([3, 1, 2])
    result = m.distance_to_plane(point, normal, origin)
    assert result == 0

def test_distance_to_plane_point_off_plane():
    point = np.array([1, 2, 3])
    normal = np.array([1, 0, -1])
    origin = np.array([0, 0, 0])
    result = m.distance_to_plane(point, normal, origin)
    assert result > 0

def test_distance_to_plane_point_off_plane_2():
    point = np.array([0, 1, 0])
    normal = np.array([1, 1, 1])
    origin = np.array([0, 0, 0])
    result = m.distance_to_plane(point, normal, origin)
    assert result > 0  

def test_verify_node_within_bounds_no_obstacle():
    node = n.Node(5, 5, 0, -1)
    obstacle_map = [[False]*10 for _ in range(10)]
    assert n.verify_node(node, obstacle_map, 0, 0, 10, 10) == True

def test_verify_node_out_of_bounds_negative_coordinates():
    node = n.Node(-1, 5, 0, -1)
    obstacle_map = [[False]*10 for _ in range(10)]
    assert n.verify_node(node, obstacle_map, 0, 0, 10, 10) == False

def test_verify_node_out_of_bounds_x_large():
    node = n.Node(11, 5, 0, -1)
    obstacle_map = [[False]*10 for _ in range(10)]
    assert n.verify_node(node, obstacle_map, 0, 0, 10, 10) == False

def test_verify_node_within_bounds_on_obstacle():
    node = n.Node(3, 3, 0, -1)
    obstacle_map = [[False]*10 for _ in range(10)]
    obstacle_map[3][3] = True
    assert n.verify_node(node, obstacle_map, 0, 0, 10, 10) == False

def test_verify_out_of_bounds_y_small():
    node = n.Node(0, -2, 0, -1)
    obstacle_map = [[False]*10 for _ in range(10)]
    assert n.verify_node(node, obstacle_map, 0, 0, 10, 10) == False
    

def test_verify_out_of_bounds_y_large():
    node = n.Node(0, 10, 0, -1)
    obstacle_map = [[False]*10 for _ in range(10)]
    assert n.verify_node(node, obstacle_map, 0, 0, 10, 10) == False

def test_print_coverages():
    print('')
    print_coverage_1()
    print_coverage_2()


if __name__ == '__main__':
    conftest.run_this_test(__file__)

