import conftest
import numpy as np
from coverage_tracker import branch_coverage
from Mapping.normal_vector_estimation import normal_vector_estimation as m
from Mapping.grid_map_lib import grid_map_lib as n



def print_coverage():
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

def test_point_on_plane():
    point = np.array([0, 0, 0])
    normal = np.array([0, 0, 0])
    origin = np.array([0, 0, 0])
    result = m.distance_to_plane(point, normal, origin)
    assert result == 0
    assert branch_coverage["normal_vector_esitmation_1"] == True

def test_point_on_plane_2():
    point = np.array([2, 1, 3])
    normal = np.array([1, 1, 1])
    origin = np.array([3, 1, 2])
    result = m.distance_to_plane(point, normal, origin)
    assert result == 0
    assert branch_coverage["normal_vector_esitmation_1"] == True

def test_point_off_plane():
    point = np.array([1, 2, 3])
    normal = np.array([1, 0, -1])
    origin = np.array([0, 0, 0])
    result = m.distance_to_plane(point, normal, origin)
    assert result > 0
    assert branch_coverage["normal_vector_esitmation_2"] == True

def test_point_off_plane_2():
    point = np.array([0, 1, 0])
    normal = np.array([1, 1, 1])
    origin = np.array([0, 0, 0])
    result = m.distance_to_plane(point, normal, origin)
    assert result > 0
    assert branch_coverage["normal_vector_esitmation_2"] == True

def test_occupied():
     # Create a GridMap instance with FloatGrid(0.0) as initial values
    grid_map = n.GridMap(10, 10, 1.0, 5.0, 5.0, n.FloatGrid(0.0))
    occupied_val = n.FloatGrid(1.0)
    grid_map.set_value_from_xy_index(2, 2, n.FloatGrid(1.0))
    result = grid_map.check_occupied_from_xy_index(2, 2, occupied_val)
    assert result == True 
    assert branch_coverage["check_occupied_from_xy_index_1"] == True

def test_occupied_2():
    grid_map = n.GridMap(10, 10, 1.0, 5.0, 5.0, n.FloatGrid(0.0))
    occupied_val = n.FloatGrid(2.0)
    grid_map.set_value_from_xy_index(3, 3, n.FloatGrid(2.0))
    result = grid_map.check_occupied_from_xy_index(3, 3, occupied_val)
    assert result == True 

def test_not_occupied():
    n.grid_map = n.GridMap(10, 10, 1.0, 5.0, 5.0, n.FloatGrid(0.0))
    occupied_val = n.FloatGrid(1.0)
    n.grid_map.set_value_from_xy_index(5, 5, n.FloatGrid(0.1))
    result = n.grid_map.check_occupied_from_xy_index(5, 5, occupied_val)
    assert result == False
    assert branch_coverage["check_occupied_from_xy_index_2"] == True


def test_not_occupied_2():
    n.grid_map = n.GridMap(10, 10, 1.0, 5.0, 5.0, n.FloatGrid(0.0))
    occupied_val = n.FloatGrid(1.0)
    n.grid_map.set_value_from_xy_index(5, 5, n.FloatGrid(0.9))
    result = n.grid_map.check_occupied_from_xy_index(5, 5, occupied_val)
    assert result == False
    print_coverage()


def reset():
    for key in branch_coverage:
        branch_coverage[key] = False

if __name__ == '__main__':
    conftest.run_this_test(__file__)
    print_coverage()
    reset()
