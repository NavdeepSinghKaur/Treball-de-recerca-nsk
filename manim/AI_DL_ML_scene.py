from manim import *

class CirclesAppearing(Scene):
    def construct(self):
        circle_ai = Circle(radius=3, color=RED_E).set_fill(RED_E, opacity=1.0)
        circle_ml = Circle(radius=2, color=BLUE_D).set_fill(BLUE_D, opacity=1.0)
        circle_dl = Circle(radius=1.25, color=ORANGE).set_fill(ORANGE, opacity=1.0)
        

        text_ai = Text('Intel·ligència Artificial').scale(0.75)
        text_ml = Text('Machine Learning').scale(0.5)
        text_dl = Text('Deep Learning').scale(0.35)
        
        self.play(FadeIn(circle_ai))
        self.wait(1)
        self.play(Write(text_ai))
        self.wait(1)    
        self.play(text_ai.animate.shift(1.25*UP).scale(0.8))  
        
        self.play(AnimationGroup(circle_ml.animate.shift(DOWN), text_ml.animate.shift(DOWN)))
        self.wait(2)
        self.play(text_ml.animate.shift(UP))
        
        self.play(AnimationGroup(circle_dl.animate.shift(1.75*DOWN), text_dl.animate.shift(1.75*DOWN)))
        self.wait(1)

