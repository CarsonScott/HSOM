### SelfOrganizingMap

<br/>

	__init__(learning_rate=0, boost_factor=0, input_size=0, node_count=0, winner_count=1, initial_range=(-1,1))

_Creates an instance of a self-organizing map._

* __learning_rate__ is a numerical value that controls the rate at which weights are changed during the learning process.
* __boost_factor__ is a numerical value that controls the handicap applied to the least-used nodes when selecting a winner/winners.
* __input_size__ is an integer value that determines the size of the weight vectors associated with each node.
* __node_count__ is an integer value that determines the number of nodes in the SOM and thus the size of the output vector.
* __winner_count__ is an integer value that determines the maximum number of nodes that are active at any given time.
* __initial_range__ is a numerical tuple that dictates the upper and lower limits of the initial random weight values. 

<br/>
	
	load(filename)

_Initializes the SelfOrganizingMap with parameters from a json file._

* __filename__ is a string that matches the directory of an existing json file. 

<br/>
	
	update(sample)

_Performs the mapping/learning process for one input (sample) and returns the result._

* __sample__ is a binary vector with a length equal to the input_size value passed to the SelfOrganizingMap constructor. 

<br/>

	train(samples)
		
_Performs the mapping/learning process for multiple inputs (samples)._

* __samples__ is a list of binary vectors that get passed to the update function one-by-one.

<br/>

	test(samples)
			
_Performs the mapping process for multiple inputs (samples) and returns the results without learning._

* __samples__ is a list of binary vectors that get passed to the update function one-by-one.

<br/>

	set_training(state)

_Turns the training process either on or off._

* __state__ is a boolean value that determines whether or not training occurs.

<br/>

***

<br/>

### SelfOrganizingMemory

<br/>

	__init__(learning_rate, input_size=0, layer_sizes=[], input_percents=[], learning_rates=[], boost_factors=[], node_counts=[], winner_counts=[], initial_ranges=[])
	
_Creates instance of self-organizing memory._

* __input_size__ is an integer value that determines the size of the weight vectors associated with each node in a SOM.
* __layer_sizes__ is a list of integers that dictate the size of each layer from the bottom to the top of the hierarchy.
* __input_percents__ is a list of values that determine the percentage of the input vector that the SOMs in each layer are connected to. 
* __learning_rates__ is a list of numerical values that controls the rate at which weights are changed during the learning process for each layer.
* __boost_factors__ is a list of numerical values that controls the handicap applied to the least-used nodes for each layer.
* __node_counts__ is a list of integer values that determines the number of nodes in each SOM for each layer.
* __winner_counts__ is a list of integers that determine the maximum number of active nodes per SOM for each layer.
* __initial_ranges__ is a list of numerical tuples that dictates the upper and lower limits of the initial weight values for each layer. 

<br/>
	
	load(filename)

_Initializes the SelfOrganizingMemory with parameters from a json file._

* __filename__ is a string that matches the directory of an existing json file. 

<br/>

	update(sample)

_Performs mapping/learning process for one input and returns result._

* __sample__ is a binary vector with a length equal to the input_size value passed to the SelfOrganizingMemory constructor. 

<br/>

	train(samples)
	
_Performs mapping/learning process for multiple inputs (samples)._

* __samples__ is a list of binary vectors that get passed to the update function one-by-one.

<br/>

	test(samples)
			
_Performs mapping process for multiple inputs (samples) and returns the results without learning._

* __samples__ is a list of binary vectors that get passed to the update function one-by-one.

<br/>

	set_training(state)

_Turns the training process either on or off._

* __state__ is a boolean value that determines whether or not training occurs.

<br/>
