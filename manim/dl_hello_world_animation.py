import numpy as np
from PIL import Image
from manim_ml.neural_network import NeuralNetwork, FeedForwardLayer, Convolutional2DLayer, ImageLayer
from manim import *

class nn_model(Scene):
    def construct(self):
        
        image = Image.open("number-9-mnist.jpeg") 
        numpy_image = np.asarray(image)

        nn = NeuralNetwork([
                ImageLayer(numpy_image, height=1.5),
                Convolutional2DLayer(1, 5, 2, filter_spacing=0.1),
                FeedForwardLayer(8, activation_function='ReLU'),
                FeedForwardLayer(8, activation_function='ReLU'),
                FeedForwardLayer(10, activation_function='Sigmoid'),
            ],
            layer_spacing=0.4,
        )
        
        nn.move_to(2*LEFT)
        nn.scale(2)
        self.add(nn)
        
        forward_pass = nn.make_forward_pass_animation()
        self.play(forward_pass, run_time=25)