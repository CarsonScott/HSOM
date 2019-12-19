from hsom import SelfOrganizingNetwork
from random import sample 

input_size = 100
layer_sizes = [20, 15, 10, 5, 2, 1]
input_percents = [0.2, 0.2, 0.2, 0.2, 0.75, 1.0]
learning_rate = 0.05
boost_factor = 2
node_count = 5
winner_count = 1
initial_range = (-0.5, 0.5)

# Create hierarchical layers of size 20, 15, 10, 5, 2, and 1
self_organizing_network = SelfOrganizingNetwork(
  input_size=input_size,
  layer_sizes=layer_sizes,
  input_percents=input_percents,
  learning_rates=learning_rate,
  boost_factors=boost_factor,
  node_counts=node_count,
  winner_counts=winner_count,
  initial_ranges=initial_range)
  
# Create a set of sparse samples
samples=[]
for i in range(node_count):
  X = [0 for j in range(input_size)]
  I = [j for j in range(input_size)]
  for j in sample(I, int(input_size*0.2)):
    X[j] = 1
  samples.append(X)
    
for i in range(200):
  self_organizing_network.train(samples)
  
outputs=self_organizing_network.test(samples)

for i in range(len(outputs)):
  print(outputs[i])

# TEST RESULTS
#
# [0, 0, 0, 1, 0]
# [0, 1, 0, 0, 0]
# [0, 0, 0, 0, 1]
# [0, 0, 1, 0, 0]
# [1, 0, 0, 0, 0]
