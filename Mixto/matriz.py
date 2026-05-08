import numpy as np
costs = np.column_stack(([3, 2, 1, 3], [7, 6, 6, 5], [3, 5, 1, 6]))
print("MATRIZ COLUMN STACK")
print(costs)
mean_costs = np.mean(costs[:3, 1])
print("MATRIZ MEAN")
print(mean_costs)