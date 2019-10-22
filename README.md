# A Self-Organizing Map for Multiclass Classification

A self-organizing map (SOM) is an artificial neural network that uses unsupervised learning to generate a low-dimensional representation of the input space. 

This specific SOM is a feedforward neural network. Each node in the output layer has a weight vector that defines a particular input pattern. Nodes produce a logistic output which allows them to be ranked from the most to least responsive when a given input is observed. The most responsive node is called the winner and has a state equal to 1, whereas the less responsive nodes have states equal to 0. 

The winner represents a class to which the given input is mapped. The weights of the winner are trained so that they better resemble the input pattern. The SOM produces a state vector as output, which shows at any given time only one node active in response to a given input.

### Example

    from som import SelfOrganizingMap

    learning_rate = 0.05
    node_count = 5
    input_size = 6
    weight_range = (0.01, 0.03)

    self_organizing_map = SelfOrganizingMap(
        learning_rate=learning_rate, 
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
      
The result of this code should produce 5 unique output vectors, in which every node responds exactly once to a given input.
  
  [Documentation](https://github.com/CarsonScott/self-organizing-map/blob/master/DOCUMENTATION.md)
