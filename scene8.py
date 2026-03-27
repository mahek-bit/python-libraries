import numpy as np

# Step 1: Define traffic flow matrix (2×2)
# Rows = Incoming roads
# Columns = Outgoing roads

traffic_flow = np.array([[40, 25],
                         [35, 30]])

print("Original Traffic Flow Matrix:")
print(traffic_flow)


# Step 2: Define transformation matrix
# Simulates signal timing change

transformation = np.array([[1.2, 0],
                           [0, 0.8]])

print("\nTransformation Matrix:")
print(transformation)


# Step 3: Apply transformation

new_flow = np.dot(transformation, traffic_flow)

print("\nNew Traffic Flow Matrix:")
print(new_flow)


# Step 4: Compare total traffic

print("\nTotal Before:", np.sum(traffic_flow))
print("Total After:", np.sum(new_flow))