from som import SelfOrganizingMemory
from random import sample 

input_size = 100
node_count = 5
learning_rate = 0.05
weight_range = (0.01, 0.03)

som = SelfOrganizingMemory(
  learning_rate=learning_rate, 
  node_count=node_count, 
  input_size=input_size, 
  weight_range=weight_range, 
  layer_sizes=[20, 15, 10, 5, 2], 
  link_percentages=[0.2, 0.2, 0.2, 0.2, 0.75])
  
# Create a set of sparse samples
samples=[]
	for i in range(node_count):
    X = [0 for j in range(input_size)]
    I = [j for j in range(input_size)]
    for j in sample(I, int(input_size*0.2)):
      X[j] = 1
    samples.append(X)
    
for i in range(200):
  som.train(samples)
  
outputs=som.test(samples)
for i in range(len(outputs)):
  print(outputs[i])
