### SelfOrganizingMap

	__init__(learning_rate, node_count, input_size, weight_range)

_Creates instance of self-organizing map._

	update(sample)

_Performs mapping/learning process for one input (sample) and returns the result._

	train(samples)
		
_Performs mapping/learning process for multiple inputs (samples)._

	test(samples)
			
_Performs mapping process for multiple inputs (samples) and returns the results without learning._

___

### SelfOrganizingMemory

	__init__(learning_rate, node_count, input_size, weight_range, layer_sizes=[], link_percentages=[])

_Creates instance of self-organizing memory._

	update(sample)

_Performs mapping/learning process for one input and returns result._

	train(samples)

_Performs mapping/learning process for multiple inputs (samples)._

	test(samples)
			
_Performs mapping process for multiple inputs (samples) and returns the results without learning._
