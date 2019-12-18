from .self_organizing_map import SelfOrganizingMap
from .util import *

class SelfOrganizingMemory:
	def __init__(self, learning_rate, boost_factor, input_size, node_count, weight_range, layer_sizes=[], link_percentages=[], winner_counts=[]):
		self.maps=[]
		self.links=[]
		self.outputs=[]
		self.training=True
		if winner_counts==None:
			winner_counts=[1 for i in range(len(layer_sizes))]
		for i in range(len(layer_sizes)):
			som_count=layer_sizes[i]
			winner_count=winner_counts[i]
			link_percentage=link_percentages[i]
			link_count=int(link_percentage*input_size)
			self.maps.append([])
			self.links.append([])
			self.outputs.append([])
			for j in range(som_count):
				som=SelfOrganizingMap(
					learning_rate=learning_rate, 
					boost_factor=boost_factor,
					input_size=link_count, 
					node_count=node_count, 
					weight_range=weight_range, 
					winner_count=winner_count)
				links=sample([j for j in range(input_size)], link_count)
				self.maps[i].append(som)
				self.links[i].append(links)
			input_size=som_count*node_count

	def compute_outputs(self, sample):
		inputs=sample
		outputs=None
		for i in range(len(self.outputs)):
			maps=self.maps[i]
			links=self.links[i]
			outputs=[]
			for j in range(len(maps)):
				sample=[inputs[j] for j in links[j]]
				output=maps[j].update(sample)
				outputs+=output
			inputs=outputs
			self.outputs[i]=outputs
		return outputs

	def set_training(self, training):
		for i in range(len(self.maps)):
			for j in range(len(self.maps[i])):
				self.maps[i][j].set_training(training)

	def update(self, sample):
		output=self.compute_outputs(sample)
		return output

	def train(self, samples):
		for sample in samples:
			self.update(sample)

	def test(self, samples):
		outputs=[]
		training=self.training
		self.set_training(False)
		for sample in samples:
			output=self.update(sample)
			outputs.append(output)
		self.set_training(training)
		return outputs