from som import SelfOrganizingMemory
from random import sample 

input_size = 100
node_count = 5
learning_rate = 0.05
weight_range = (0.01, 0.03)
layer_sizes = [20, 15, 10, 5, 2]
link_percentages = [0.2, 0.2, 0.2, 0.2, 0.75]

# Create hierarchical layers of size 20, 15, 10, 5, and 2
self_organizing_memory = SelfOrganizingMemory(
  learning_rate=learning_rate, 
  node_count=node_count, 
  input_size=input_size, 
  weight_range=weight_range, 
  layer_sizes=layer_sizes, 
  link_percentages=link_percentages)
  
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
# [1, 0, 0, 0, 0, 0, 1, 0, 0, 0]
# [0, 0, 0, 0, 1, 0, 0, 1, 0, 0]
# [0, 0, 1, 0, 0, 0, 0, 0, 0, 1]
# [0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
# [0, 1, 0, 0, 0, 0, 0, 0, 1, 0]
