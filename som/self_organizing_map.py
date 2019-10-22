from .util import *

class SelfOrganizingMap:
	def __init__(self, learning_rate, node_count, input_size, weight_range):
		self.learning_rate=learning_rate
		self.nodes=[]
		self.inputs=[]
		self.outputs=[]
		self.thresholds=[]
		self.winner=None
		self.training=True
		for i in range(node_count):
			self.nodes.append([])
			for j in range(input_size):
				self.nodes[i].append(uniform(*weight_range))
			self.inputs.append(0)
			self.outputs.append(0)
			self.thresholds.append(0)
			
	def set_training(self, training):
		self.training=training

	def compute_outputs(self, sample):
		for i in range(len(self.nodes)):
			h=self.thresholds[i]
			W=self.nodes[i]
			x=sum([sample[j]*W[j] for j in range(len(sample))])
			y=logistic(x-h)
			self.inputs[i]=x
			self.outputs[i]=y
		self.winner=self.outputs.index(max(self.outputs))
		output=[0 for i in range(len(self.nodes))]
		output[self.winner]=1
		return output

	def compute_weights(self, sample):
		W=self.nodes[self.winner]
		h=self.thresholds[self.winner]
		y=self.outputs[self.winner]
		x=self.inputs[self.winner]
		dh=self.learning_rate*(x-h)
		h+=dh
		for i in range(len(W)):
			wi=W[i]
			xi=sample[i]
			if xi==0:xi=-1
			dwij=self.learning_rate*y*xi
			wi+=dwij
			if abs(wi) > 4:
				wi=4*sign(wi)
			W[i]=wi
		self.nodes[self.winner]=W
		self.thresholds[self.winner]=h

	def update(self, sample):
		output=self.compute_outputs(sample)
		if self.training:self.compute_weights(sample)
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
