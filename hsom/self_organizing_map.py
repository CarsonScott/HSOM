from .util import *

class SelfOrganizingMap:

	def __init__(self, learning_rate=None, 
					   boost_factor=None, 
					   input_size=None, 
					   node_count=None, 
					   winner_count=1, 
					   initial_range=(-1,1)):

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
				self.nodes[i].append(uniform(*initial_range))
			self.inputs.append(0)
			self.outputs.append(0)
			self.averages.append(0)
			self.histories.append([])
			self.thresholds.append(0)
			
	def set_training(self, training):
		self.training=training

	def compute_boost(self, index):
		min_average=0.01*max(self.averages)
		if self.averages[index] >= min_average:return 1
		else:return 1+(min_average-self.averages[index])*self.boost_factor

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
		best_indices=reverse(sort(self.outputs))[0:self.winner_count]
		best_outputs=[self.outputs[i] for i in best_indices]
		options=[]
		for i in range(len(self.nodes)):
			if self.outputs[i] >= min(best_outputs):
				options.append(i)
		self.winners=sample(options, self.winner_count)

	def compute_outputs(self, sample):
		for i in range(len(self.nodes)):
			h=self.thresholds[i]
			W=self.nodes[i]
			x=0
			for j in range(len(W)):
				xj=sample[j]
				wj=W[j]
				x+=xj*wj
			y=logistic(x-h)*self.compute_boost(i)
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
				if sample[i]==1:
					dwi=self.learning_rate*y
				else:dwi=-self.learning_rate*y
				wi=W[i]
				wi+=dwi
				if abs(wi) > 4:
					wij=4*sign(wi)
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

	def load(self, filename):
		data=json.load(open(filename, 'r'))
		learning_rate=data['learning_rate']
		boost_factor=data['boost_factor']
		input_size=data['input_size']
		node_count=data['node_count']
		winner_count=data['winner_count']
		initial_range=data['initial_range']
		self.__init__(
			learning_rate=learning_rate,
			boost_factor=boost_factor,
			input_size=input_size,
			node_count=node_count,
			winner_count=winner_count,
			initial_range=initial_range)
		return self