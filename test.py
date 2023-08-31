# Talent Competition - SE in charge of recording scores used 2 DS to record:
# - A Python list of names [‘Pablo’, ‘Jessica’, ‘Elise’]
# - Another list for scores [100, 80, 50]
# - Index from names matches index from scores

# Q1: Write a function that takes both names and scores and returns the name of the person with the highest score.

# Q2: … returns the name of the person in first place and the name of the person in second place.

# names: ["Pablo", "Jessica", "Chris"]
# points: [12, 60, 50]
# 10:43
# def get_winner(names, points) -> str
# 10:44
# Q1:  name of the person who won the talent contest

# Questions:
    # What if there is a tie for the highest score? Return both names, or assume no ties?
    # Can I assume all participants have a score?

points = [10, 500, 60]
names = ["Pablo", "Jessica", "Chris"]

# Steps:
# Iterate through points list and find index of max points
# Return names[index] from index of points

def get_winner(points, names):
    winner = points[0]
    index = 0
    for i, e in enumerate(points):
        if winner < e:
            winner = e
            index = i
    print(names[index])
    
get_winner(points, names)

# Example:
# points = [50, 30, 45]
# names = ['Pablo', 'Jessica', 'Chris']

# candidate = 50
# 50 < 30 ? false, so 50 remains candidate
# 50 < 45 ? false, so 50 remains candidate
# position of points.index(50) = 0
# return names[0] = 'Pablo'
# Pablo is the winner!

