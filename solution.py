from manimlib.imports import *
from math import *
class Solution(GraphScene):
	CONFIG = {
		'graph_origin': ORIGIN,
		'function_color': WHITE,
		'axes_color': BLUE,
		'x_min':	-10,
		'x_max':	10,
		'x_labeled_nums' :range(-10,10, 2),
		'y_min':	-7,
		'y_max':	114,
		'y_labeled_nums' :range(-7,114,12)}

	def construct(self):
		watermark = ImageMobject("./assets/water_mark.png")
		watermark.scale(1.5)
		watermark.to_corner(DOWN+RIGHT, buff=0)
		self.play(FadeIn(watermark))
		Solve = TexMobject(r" Solve \ for \ x \ over \ the \ real \ numbers:")
		Solve.to_edge(UP)
		self.play(Write(Solve))
		self.wait(2)
		R0 = TexMobject(r" x^{2} + 2 x - 6 = 0")
		R1 = TexMobject(r" Add 6 \ to \ both \ sides:")
		R2 = TexMobject(r" x^{2} + 2 x = 6")
		R3 = TexMobject(r" Add 1 \ to \ both \ sides:")
		R4 = TexMobject(r" x^{2} + 2 x + 1 = 7")
		R5 = TexMobject(r" Write \ the \ left \ hand \ side \ as \ a \ square:")
		R6 = TexMobject(r" (x + 1)^{2} = 7")
		R7 = TexMobject(r" Take \ the \ square \ root \ of \ both \ sides:")
		R8 = TexMobject(r" x + 1 = \sqrt{7} \ or \ x + 1 = -\sqrt{7}")
		R9 = TexMobject(r" Subtract 1 \ from \ both \ sides:")
		R10 = TexMobject(r" x = \sqrt{7} - 1 \ or \ x + 1 = -\sqrt{7}")
		R11 = TexMobject(r" Subtract 1 \ from \ both \ sides:")
		R12 = TexMobject(r" Answer: x = \sqrt{7} - 1 \ or \ x = -1 - \sqrt{7}")
		R0.shift([0,0.7,0])
		self.play(Write(R0))
		self.wait(1)
		R1.next_to(R0, DOWN)
		self.play(Write(R1))
		self.wait(1)
		R2.next_to(R1, DOWN)
		self.play(Write(R2))
		self.wait(1)
		self.play(FadeOut(R0))
		self.play(ApplyMethod(R1.shift,[0,0.7,0]))
		self.play(ApplyMethod(R2.next_to,R1, DOWN))
		R3.next_to(R2, DOWN)
		self.play(Write(R3))
		self.play(FadeOut(R1))
		self.play(ApplyMethod(R2.shift,[0,0.7,0]))
		self.play(ApplyMethod(R3.next_to,R2, DOWN))
		R4.next_to(R3, DOWN)
		self.play(Write(R4))
		self.play(FadeOut(R2))
		self.play(ApplyMethod(R3.shift,[0,0.7,0]))
		self.play(ApplyMethod(R4.next_to,R3, DOWN))
		R5.next_to(R4, DOWN)
		self.play(Write(R5))
		self.play(FadeOut(R3))
		self.play(ApplyMethod(R4.shift,[0,0.7,0]))
		self.play(ApplyMethod(R5.next_to,R4, DOWN))
		R6.next_to(R5, DOWN)
		self.play(Write(R6))
		self.play(FadeOut(R4))
		self.play(ApplyMethod(R5.shift,[0,0.7,0]))
		self.play(ApplyMethod(R6.next_to,R5, DOWN))
		R7.next_to(R6, DOWN)
		self.play(Write(R7))
		self.play(FadeOut(R5))
		self.play(ApplyMethod(R6.shift,[0,0.7,0]))
		self.play(ApplyMethod(R7.next_to,R6, DOWN))
		R8.next_to(R7, DOWN)
		self.play(Write(R8))
		self.play(FadeOut(R6))
		self.play(ApplyMethod(R7.shift,[0,0.7,0]))
		self.play(ApplyMethod(R8.next_to,R7, DOWN))
		R9.next_to(R8, DOWN)
		self.play(Write(R9))
		self.play(FadeOut(R7))
		self.play(ApplyMethod(R8.shift,[0,0.7,0]))
		self.play(ApplyMethod(R9.next_to,R8, DOWN))
		R10.next_to(R9, DOWN)
		self.play(Write(R10))
		self.play(FadeOut(R8))
		self.play(ApplyMethod(R9.shift,[0,0.7,0]))
		self.play(ApplyMethod(R10.next_to,R9, DOWN))
		R11.next_to(R10, DOWN)
		self.play(Write(R11))
		self.play(FadeOut(R9))
		self.play(ApplyMethod(R10.shift,[0,0.7,0]))
		self.play(ApplyMethod(R11.next_to,R10, DOWN))
		R12.next_to(R11, DOWN)
		self.play(Write(R12))
		self.play(FadeOut(R12))
		self.play(FadeOut(R11))
		self.play(FadeOut(R10))
		self.play(FadeOut(Solve))
		