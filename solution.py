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
		'y_min':	-10,
		'y_max':	10,
		'y_labeled_nums' :range(-10,10,2)}

	def construct(self):
		watermark = ImageMobject("./assets/water_mark.png")
		watermark.scale(1.5)
		watermark.to_corner(DOWN+RIGHT, buff=0)
		self.play(FadeIn(watermark))
		R0 = TexMobject(r" plot \ x")
		self.play(Write(R0))
		self.wait(2)
		self.play(FadeOut(R0))
		self.setup_axes(animate=True)
		func_graph = self.get_graph(self.func, self.function_color)
		self.play(FadeIn(func_graph))
		self.wait(2)
		
	def func(self, x):
		f = x
		return f