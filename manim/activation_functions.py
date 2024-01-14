from manim import *
import math
import cmath
import numpy as np

class TanhAnimation(Scene):
    def construct(self):
        tanh_axes = Axes(x_range=[-3, 3], y_range=[-2, 2], axis_config={"include_numbers": True})
        relu_axes = Axes(x_range=[-3, 3], y_range=[-4, 4], axis_config={"include_numbers": True})
        sigmoid_axes = Axes(x_range=[-6, 6], y_range=[-2, 2], axis_config={"include_numbers": True})
        
        tanh_labels = tanh_axes.get_axis_labels(x_label='x', y_label='y')
        relu_labels = tanh_axes.get_axis_labels(x_label='x', y_label='y')
        sigmoid_labels = tanh_axes.get_axis_labels(x_label='x', y_label='y')
        
        def tanh_function(x): return math.tanh(x)
        def relu_function(x): return max(0, x)
        def sigmoid_function(x): return 1/(1+math.exp(-x))
        
        tanh_plot = tanh_axes.plot(tanh_function, color=TEAL_D)
        relu_plot = relu_axes.plot(relu_function, color=TEAL_D)
        sigmoid_plot = sigmoid_axes.plot(sigmoid_function, color=TEAL_D)
        
        tanh_text = Text('Funció Tanh')
        relu_text = Text('Funció ReLU')
        sigmoid_text = Text('Funció Sigmoide')      
          
        self.wait(1)
        self.play(Write(tanh_text))
        self.wait(3)
        self.play(Unwrite(tanh_text))
        self.play(Write(tanh_axes), Write(tanh_labels))
        self.play(Write(tanh_plot), run_time=4)
        self.wait(5)
        self.play(AnimationGroup(Unwrite(tanh_plot), Unwrite(tanh_axes), Unwrite(tanh_labels)))
        
        self.wait(1)
        self.play(Write(relu_text))
        self.wait(3)
        self.play(Unwrite(relu_text))
        self.play(Write(relu_axes), Write(relu_labels))
        self.play(Write(relu_plot), run_time=4)
        self.wait(5)
        self.play(AnimationGroup(Unwrite(relu_plot), Unwrite(relu_axes), Unwrite(relu_labels)))
        
        self.wait(1)
        self.play(Write(sigmoid_text))
        self.wait(3)
        self.play(Unwrite(sigmoid_text))
        self.play(Write(sigmoid_axes), Write(sigmoid_labels))
        self.play(Write(sigmoid_plot), run_time=4)
        self.wait(5)
        self.play(AnimationGroup(Unwrite(sigmoid_plot), Unwrite(sigmoid_axes), Unwrite(sigmoid_labels)))
        
