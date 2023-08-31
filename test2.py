# Q2: get first place and second place
# def get_winner(names, points) -> tuple (str, str)

points = [75, 80, 100]
names = ["Pablo", "Jessica", "Chris"]

# Expected to return ('Pablo', 'Chris') because they have the two highest scores, 100 and 60.

# Steps:
# Iterate through points list and find index of max score, then index of next highest score
# Consider removing first score from list before iterating again
# Return names[index] from index of points as tuple (str, str)

# What if first item is largest item? Need to check if first and second item are larger, then initialize variables correctly

def get_first_and_second_place(points, names):
    if points[0] > points[1]:
        first = points[0]
        index_first = 0
        second = points[1]
        index_second = 1
    else:
        first = points[1]
        index_first = 1
        second = points[0]
        index_second = 0

    for i, e in enumerate(points):
        if first < e:
            second = first
            index_second = index_first
            first = e
            index_first = i
        elif second < e < first:
            second = e
            index_second = i
    return (names[index_first], names[index_second])


get_first_and_second_place(points, names)