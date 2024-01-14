from manim import *
import numpy as np

class NeuronAnimation(Scene):
    def construct(self):
        
        matrix = Matrix([
            ["\\vcenter{Dades}", "\\vcenter{Pesos}"],
            ["x_1", "w_1"],
            ["x_2", "w_2"],
            ["\\vdots", "\\vdots"],
            ["x_n", "w_n"]
        ])
        
        bias = Text("+ biaix")
        arrow = Arrow(1.5*LEFT, RIGHT)
        activation = Text("activació")
        
        matrix.scale(0.75)
        self.play(Create(matrix.shift(4.5*LEFT)))
        self.wait(2)


        self.play(AnimationGroup(Write(bias), bias.animate.shift(2.35*LEFT).scale(0.75)))
        self.wait(3)
        
        
        self.play(AnimationGroup(Write(arrow), arrow.animate.scale(0.75)))
        self.wait(1)
        
        self.play(AnimationGroup(Write(activation), activation.animate.shift(2.15*RIGHT).scale(0.75)))
        self.wait(3)
        