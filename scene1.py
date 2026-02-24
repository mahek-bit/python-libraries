import numpy as np

ratings = np.array([
[5, 4, 0],
[3, 0, 5],
[0, 4, 4]
])

# Average rating per movie
avg = np.mean(ratings, axis=0)

print("Average Movie Rating:")
print(avg)

