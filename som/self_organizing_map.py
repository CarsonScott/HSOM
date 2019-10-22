from .util import *

class SelfOrganizingMap:
	def __init__(self, learning_rate=0, node_count=0, input_size=0, weight_range=(0,0)):
		self.learning_rate=learning_rate
		self.nodes=[]
		self.inputs=[]
		self.outputs=[]
		self.thresholds=[]
		self.winner=None
		self.training=True
		for i in range(node_count):
			node=[0 for j in range(input_size)]
			self.nodes.append(node)
			self.inputs.append(0)
			self.outputs.append(0)
			self.thresholds.append(0)
		self.randomize(weight_range)

	def save(self, filename):
		config=ConfigParser()
		config['Map']={
			'learning_rate':str(self.learning_rate),
			'node_count':str(len(self.nodes)),
			'input_size':str(len(self.nodes[0]))}
		config['Weights']={}
		for i in range(len(self.nodes)):
			config['Weights'][str(i)]=str(self.nodes[i])
		config['Thresholds']={}
		for i in range(len(self.nodes)):
			config['Thresholds'][str(i)]=str(self.thresholds[i])
		config.write(open(filename, 'w'))

	def load(self, filename):
		config=ConfigParser()
		config.read(filename)
		learning_rate=eval(config['Map']['learning_rate'])
		node_count=eval(config['Map']['node_count'])
		input_size=eval(config['Map']['input_size'])
		output=SelfOrganizingMap(learning_rate, node_count, input_size)
		for i in range(node_count):
			weights=eval(config['Weights'][str(i)])
			threshold=eval(config['Thresholds'][str(i)])
			output.nodes[i]=weights
			output.thresholds[i]=threshold
		return output

	def randomize(self, weight_range):
		for i in range(len(self.nodes)):
			self.nodes[i]=[uniform(*weight_range) for j in range(len(self.nodes[i]))]

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

	def compute_weights(self, X):
		W=self.nodes[self.winner]
		h=self.thresholds[self.winner]
		y=self.outputs[self.winner]
		x=self.inputs[self.winner]
		dh=self.learning_rate*(x-h)
		h+=dh
		for i in range(len(W)):
			wi=W[i]
			xi=X[i]
			if xi==0:xi=-1
			dwij=self.learning_rate*y*xi
			wi+=dwij
			if abs(wi) > 4:
				wi=4*sign(wi)
			W[i]=wi
		self.nodes[self.winner]=W
		self.thresholds[self.winner]=h

	def update(self, X):
		Y=self.compute_outputs(X)
		if self.training:
			self.compute_weights(X)
		return Y

	def train(self, samples, iterations):
		index=0
		for i in range(iterations):
			X=samples[index]
			Y=self.update(X)
			index+=1
			if index >= len(samples):
				index=0

	def test(self, samples):
		outputs=[]
		training=self.training
		self.training=False
		for X in samples:
			Y=self.update(X)
			outputs.append(Y)
		self.training=training
		return outputs