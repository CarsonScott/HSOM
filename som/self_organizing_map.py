from .util import *

class SelfOrganizingMap:
	def __init__(self, learning_rate, boost_factor, input_size, node_count, weight_range, winner_count=1):
		self.learning_rate=learning_rate
		self.input_size=input_size
		self.boost_factor=boost_factor
		self.node_count=node_count
		self.winner_count=winner_count
		self.nodes=[]
		self.inputs=[]
		self.outputs=[]
		self.thresholds=[]
		self.winners=[]
		self.averages=[]
		self.histories=[]
		self.training=True
		for i in range(node_count):
			self.nodes.append([])
			for j in range(input_size):
				self.nodes[i].append(uniform(*weight_range))
			self.inputs.append(0)
			self.outputs.append(0)
			self.averages.append(0)
			self.histories.append([])
			self.thresholds.append(0)
			
	def set_training(self, training):
		self.training=training

	def compute_boost(self, index):
		min_average=0.01*max(self.averages)
		if self.averages[index] < min_average and min_average!=0:
			return self.boost_factor*(self.averages[index]/min_average)
		else:return 0

	def compute_averages(self):
		for i in range(len(self.nodes)):
			H=self.histories[i]
			if i in self.winners:
				H.append(1)
			else:H.append(0)
			if len(H) > 1000:
				del H[0]
			a=sum(H)/len(H)
			self.histories[i]=H
			self.averages[i]=a

	def compute_winners(self):
		scores=[]
		for i in range(len(self.nodes)):
			y=self.outputs[i]
			s=y+self.compute_boost(i)
			scores.append(s)
		best_indices=reverse(sort(scores))[0:self.winner_count]
		best_scores=[scores[i] for i in best_indices]
		options=[]
		for i in range(len(self.nodes)):
			if scores[i] >= min(best_scores):
				options.append(i)
		self.winners=sample(options, self.winner_count)

	def compute_outputs(self, sample):
		for i in range(len(self.nodes)):
			h=self.thresholds[i]
			W=self.nodes[i]
			x=sum([sample[j]*W[j] for j in range(len(sample))])
			y=logistic(x-h)
			self.inputs[i]=x
			self.outputs[i]=y

	def get_outputs(self):
		outputs=[]
		for i in range(len(self.nodes)):
			if i in self.winners:
				outputs.append(1)
			else:outputs.append(0)
		return outputs

	def compute_weights(self, sample):
		for winner in self.winners:
			W=self.nodes[winner]
			h=self.thresholds[winner]
			y=self.outputs[winner]
			x=self.inputs[winner]
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
			self.nodes[winner]=W
			self.thresholds[winner]=h

	def update(self, sample):
		self.compute_outputs(sample)
		self.compute_winners()
		self.compute_averages()
		if self.training:
			self.compute_weights(sample)
		return self.get_outputs()

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