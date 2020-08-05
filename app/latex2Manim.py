import math
config = """
\tCONFIG = {
\t\t'x_min':           -10,
\t\t'x_max':            10,
\t\t'y_min':            -1,
\t\t'y_max':             1,
\t\t'graph_origin': ORIGIN,
\t\t'function_color':WHITE,
\t\t'axes_color':     BLUE,}
\n
"""

construct_graph = """self.setup_axes(animate=True)
\t\tfunc_graph = self.get_graph(self.func, self.function_color)
\t\tself.play(FadeIn(func_graph))
\t\tself.wait(2)\n\t\t"""

watermark="""\n\t\twatermark = ImageMobject("./assets/water_mark.png")
\t\twatermark.scale(1.5)
\t\twatermark.to_corner(DOWN+RIGHT, buff=0)\n\t\tself.play(FadeIn(watermark))\n\t\t"""

def generateTexMobject(line):
    retval = ' = TexMobject(r"' + line.split("\n")[0]+ '")\n\t\t'
    return retval

def latex2Manim(latexArr,query,func):
	graph = False
	if "plot" in list(query.split(" ")):
		graph = True 
		print("A Graph will be generated")
	else:
		graph = False
		print("A Graph will not be generated")
	retval = 'from manimlib.imports import *\nfrom math import *\n'
	if graph == True:
		retval += 'class Solution(GraphScene):'
	else:
		retval = 'class Solution(Scene):'

	retval += generate_config(func)
	retval += '\n\tdef construct(self):'
	retval += watermark

	if len(latexArr) > 2 :
		retval = retval + 'Solve' + generateTexMobject(latexArr[0])
		retval = retval + 'Solve.to_edge(UP)\n\t\t'+'self.play(Write(Solve))\n\t\t'
		retval = retval + 'self.wait(2)\n\t\t'
		retval = retval + 'R0' + generateTexMobject(latexArr[1])
		retval = retval + 'self.play(Write(R0))\n\t\tself.wait(2)\n\t\t'
		
		for i in range(2,len(latexArr)):
			if not latexArr[i].isspace(): 
				retval = retval + 'R1' + generateTexMobject(latexArr[i])
				retval = retval + 'self.play(Transform(R0,R1))\n\t\tself.wait(2)\n\t\t'

		if graph == True:
 			retval += construct_graph
	else:
		if graph != True:
			raise Exception('Latex array has no steps')
		else:
			retval += "R0" + generateTexMobject(latexArr[0])
			retval += 'self.play(Write(R0))\n\t\tself.wait(2)\n\t\tself.play(FadeOut(R0))\n\t\t'
			retval += construct_graph

	if graph != True:
		retval = retval + 'self.play(FadeOut(R0))'

	if graph == True:
		retval = retval + makeGraph(func)
	return retval

def readFile2Array(path_to_file):
	file = open(path_to_file)
	retval = file.readlines()
	file.close()
	return retval

def makeGraph(func):

	retval = """
\tdef func(self, x):
\t\tf = """
	retval += func + "\n"
	retval +=  "\t\treturn f"
	return retval


def generate_config(func,x_range=[-10,10]):
	config = """\n\tCONFIG = {
\t\t'graph_origin': ORIGIN,
\t\t'function_color': WHITE,
\t\t'axes_color': BLUE,\n"""
	f = lambda x : eval(func)
	for i in range(len(x_range)):
		x_range[i] = round(x_range[i])
	config += "\t\t'x_min':\t" + str(x_range[0]) +",\n"
	config += "\t\t'x_max':\t" + str(x_range[1]) +",\n"
	config += "\t\t'x_labeled_nums' :range("+ str(x_range[0]) + "," + str(x_range[1]) + ", 2),\n"
	y_vals = [f(t) for t in range(x_range[0],x_range[1]+1)]
	y_range = [math.floor(min(y_vals)),math.floor(max(y_vals))]
	config += "\t\t'y_min':\t" + str(y_range[0]) +",\n"
	config += "\t\t'y_max':\t" + str(y_range[1]) +",\n"
	marking_distance = (y_range[1] - y_range[0])//10
	print(marking_distance)
	config += "\t\t'y_labeled_nums' :range("+ str(y_range[0]) + "," + str(y_range[1]) + "," + str(marking_distance) + ")}\n"
	return config

"""
src = './2.txt'

latex = readFile2Array(src)
print(len(latex))
for line in latex:
    print(line,end="")
print ("")
print(latex2Manim(latex))
"""
