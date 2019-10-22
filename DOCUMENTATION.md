__SelfOrganizingMap__

	__init__(learning_rate, node_count, input_size, weight_range)

_Creates instance of self-organizing map._

	save (filename)

_Saves self-organizing map as configuration file (filename)._

	load (filename)

_Loads self-organizing map from configuration file (filename) and returns it._

	randomize (weight_range)

_Assigns random values within range (weight_range) to all nodes._

	update (sample)

_Performs mapping/learning process for one input (sample) and returns the result._

	train (samples)
		
_Performs mapping/learning process for multiple inputs (samples)._

	test (samples)
			
_Performs mapping process for multiple inputs (samples) and returns the results (no learning)._
