import conftest
import numpy as np
from coverage import branch_coverage
from Mapping.normal_vector_estimation import normal_vector_estimation as m



def print_coverage():
    hits = 0
    for branch, hit in branch_coverage.items():
        hits += 1  # Increment hits for each branch iterated
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
    
    m.distance_to_plane(point, normal, origin)
    assert branch_coverage["normal_vector_esitmation_1"] == True

def test_point_off_plane():

    point = np.array([1, 2, 3])
    normal = np.array([1, 0, -1])
    origin = np.array([0, 0, 0])
    
    m.distance_to_plane(point, normal, origin)
    print_coverage()
    assert branch_coverage["normal_vector_esitmation_2"] == True

def coverage():
    print_coverage()

if __name__ == '__main__':
    conftest.run_this_test(__file__)
    print_coverage()
