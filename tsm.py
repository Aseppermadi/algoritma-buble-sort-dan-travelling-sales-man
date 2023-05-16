import itertools


def calculate_distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


def calculate_total_distance(points, permutation):
    total_distance = 0
    for i in range(len(permutation) - 1):
        point1 = points[permutation[i]]
        point2 = points[permutation[i+1]]
        total_distance += calculate_distance(point1, point2)
    return total_distance


def tsp_brute_force(points):
    min_distance = float('inf')
    min_permutation = None
    all_permutations = itertools.permutations(range(len(points)))

    for permutation in all_permutations:
        distance = calculate_total_distance(points, permutation)
        if distance < min_distance:
            min_distance = distance
            min_permutation = permutation

    return min_permutation, min_distance


# Contoh penggunaan program
points = [(0, 0), (1, 5), (2, 3), (5, 2), (6, 8)]
min_permutation, min_distance = tsp_brute_force(points)
print("Rute terpendek:", min_permutation)
print("Jarak terpendek:", min_distance)
