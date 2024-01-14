from manim_ml.neural_network import NeuralNetwork, FeedForwardLayer
from manim import *      
        
class NnExample(Scene):
    def construct(self):

        nn = NeuralNetwork([
            FeedForwardLayer(num_nodes=4),
            FeedForwardLayer(num_nodes=5),
            FeedForwardLayer(num_nodes=6),
            FeedForwardLayer(num_nodes=5),
            FeedForwardLayer(num_nodes=4)
        ])
        nn.scale(3)
        self.add(nn)