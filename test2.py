# Q2: get first place and second place
# def get_winner(names, points) -> tuple (str, str)

points = [100, 20, 60]
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
        second = points[1]
    else:
        first = points[1]
        second = points[0]

    for e in points:
        if first < e:
            second = first
            first = e
        elif second < e < first:
            second = e
    
    winners = names[points.index(first)], names[points.index(second)]

    return winners

get_first_and_second_place(points, names)