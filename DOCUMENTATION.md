### SelfOrganizingMap

<br/>

	__init__(learning_rate, node_count, input_size, weight_range)

_Creates an instance of a self-organizing map._

* __learning_rate__ is a numerical value that controls the rate at which weights are changed during the learning process.
* __node_count__ is an integer value that determines the number of nodes in the SOM and thus the size of the output vector.
* __input_size__ is an integer value that determines the size of the weight vectors associated with each node.
* __weight_range__ is a numerical tuple that dictates the upper and lower limits of the initial random weight values. 

<br/><br/>
	
	update(sample)

_Performs the mapping/learning process for one input (sample) and returns the result._

* __sample__ is a binary vector with a length equal to the input_size value passed to the SelfOrganizingMap constructor. 

<br/><br/>

	train(samples)
		
_Performs the mapping/learning process for multiple inputs (samples)._

* __samples__ is a list of binary vectors that get passed to the update function one-by-one.

<br/><br/>

	test(samples)
			
_Performs the mapping process for multiple inputs (samples) and returns the results without learning._

* __samples__ is a list of binary vectors that get passed to the update function one-by-one.

<br/>

***

<br/>

### SelfOrganizingMemory

<br/>

	__init__(learning_rate, node_count, input_size, weight_range, layer_sizes=[], link_percentages=[])
	
_Creates instance of self-organizing memory._
	
* __learning_rate__ is a numerical value that controls the rate at which weights are changed during the learning process.
* __node_count__ is an integer value that determines the number of nodes in each SOM and thus the size of the output vector of each SOM.
* __input_size__ is an integer value that determines the size of the weight vectors associated with each node in a SOM.
* __weight_range__ is a numerical tuple that dictates the upper and lower limits of the initial random weight values.
* __layer_sizes__ is a list of integers that dictate the size of each layer from the bottom to the top of the hierarchy.
* __link_percentages__ is a list of values that determine the percentage of the input vector that the SOMs in each layer are connected to. 

<br/><br/>

	update(sample)

_Performs mapping/learning process for one input and returns result._

* __sample__ is a binary vector with a length equal to the input_size value passed to the SelfOrganizingMemory constructor. 

<br/><br/>

	train(samples)
	
_Performs mapping/learning process for multiple inputs (samples)._

* __samples__ is a list of binary vectors that get passed to the update function one-by-one.

<br/><br/>

	test(samples)
			
_Performs mapping process for multiple inputs (samples) and returns the results without learning._

* __samples__ is a list of binary vectors that get passed to the update function one-by-one.

