from som import SelfOrganizingMemory
from random import sample 

input_size = 100
node_count = 5
learning_rate = 0.05
boost_factor = 2
initial_range = (-0.5, 0.5)
layer_sizes = [20, 15, 10, 5, 2, 1]
link_percentages = [0.2, 0.2, 0.2, 0.2, 0.75, 1.0]
winner_counts = [1, 1, 1, 1, 1, 1]

# Create hierarchical layers of size 20, 15, 10, 5, 2, and 1
self_organizing_memory = SelfOrganizingMemory(
  learning_rate=learning_rate,
  boost_factor=boost_factor, 
  node_count=node_count, 
  input_size=input_size, 
  initial_range=initial_range, 
  layer_sizes=layer_sizes, 
  link_percentages=link_percentages,
  winner_counts=winner_counts)
  
# Create a set of sparse samples
samples=[]
for i in range(node_count):
  X = [0 for j in range(input_size)]
  I = [j for j in range(input_size)]
  for j in sample(I, int(input_size*0.2)):
    X[j] = 1
  samples.append(X)
    
for i in range(200):
  self_organizing_memory.train(samples)
  
outputs=self_organizing_memory.test(samples)

for i in range(len(outputs)):
  print(outputs[i])

# TEST RESULTS
#
# [0, 0, 0, 1, 0]
# [0, 1, 0, 0, 0]
# [0, 0, 0, 0, 1]
# [0, 0, 1, 0, 0]
# [1, 0, 0, 0, 0]
