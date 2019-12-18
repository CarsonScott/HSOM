
from som import SelfOrganizingMap

learning_rate = 0.1
boost_factor = 2
node_count = 5
input_size = 6
weight_range = (0.01, 0.03)

# Create a self-organizing map with 5 nodes and 6 inputs
self_organizing_map = SelfOrganizingMap(
    learning_rate=learning_rate, 
    boost_factor=boost_factor,
    node_count=node_count, 
    input_size=input_size, 
    weight_range=weight_range)

inputs = [
  [1,1,0,0,0,0],
  [0,1,1,0,0,0],
  [0,0,1,1,0,0],
  [0,0,0,1,1,0],
  [0,0,0,0,1,1]]

for i in range(200):
    self_organizing_map.train(inputs)

outputs = self_organizing_map.test(inputs)

for i in range(len(outputs)):
  print(outputs[i])

# TEST RESULTS
#
# [0, 0, 0, 0, 1]
# [0, 0, 1, 0, 0]
# [0, 1, 0, 0, 0]
# [1, 0, 0, 0, 0]
# [0, 0, 0, 1, 0]
