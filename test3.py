# Publish results from competition in this format:
# Chris 100
# Pablo 75
# Jessica 60
# All participants names and scores in descending order

# The current way the data is store doesn't allow us to do this easily.
# However, we have all the information to build an intermediate structure that can be sorted, and then printed sequentially.
# Hint: python would sort complex data, say tuples, but you need to tell it which field to sort. 
# For that take a look at the sorted()  function that uses the lambda  trick to sort data more complex that just numbers.

# Steps
# Combine names and points into tuples
# Sort tuples by score from highest to lowest
# Print tuples in correct format 

points = [100, 75, 40, 80]
names = ["Pablo", "Jessica", "Chris", "Elise"]

scores_list = list(zip(names, points))

scores_list.sort(key=lambda x:x[1], reverse=True)

for name, score in scores_list:
    print(name, score)