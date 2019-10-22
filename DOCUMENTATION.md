SelfOrganizingMap:

	__init__(learning_rate, node_count, input_size, weight_range)

		Creates instance of self-organizing map.

	save (filename)

		Saves self-organizing map as configuration file (filename).

	load (filename)

		Loads self-organizing map from configuration file (filename) and returns it.

	randomize (weight_range)

		Assigns random values within range (weight_range) to all nodes.

	update (sample)

		Performs mapping/learning process for one input (sample) and returns the result.

	train (samples)
		
		Performs mapping/learning process for multiple inputs (samples).

	test (samples)
			
		Performs mapping process for multiple inputs (samples) and returns the results (no learning).
