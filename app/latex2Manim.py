import math
from math import *
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
\t\tself.play(ShowCreation(func_graph))
\t\tself.wait(3)\n\t\tself.play(FadeOut(func_graph))\n\t\tself.play(FadeOut(self.axes))\n\t\t"""

watermark="""\n\t\twatermark = ImageMobject("./assets/water_mark.png",opacity=0.7)
\t\twatermark.scale(1.5)
\t\twatermark.to_corner(DOWN+RIGHT, buff=0)\n\t\tself.play(FadeIn(watermark))\n\t\t"""

def generateTexMobject(line):
    retval = ' = TexMobject(r"' + line.split("\n")[0]+ '" )\n\t\t'
    return retval

def latex2Manim(latexArr,query = "" ,func = None):
    graph = False
    if "plot" in list(query.split(" ")):
        graph = True
        print("A Graph will be generated automatically")
    else:
        print("Do you want to generate a graph for {}? yes/no".format(str(query)))
        selection = input().strip("\n")
        while selection not in ["yes", "no"]:
            selection = input().strip("\n")
            print("Do you want to generate a graph for {}? yes/no".format(str(query)))
        if selection == "yes":
            graph = True
        else:
            selection = input("Do you wish to graph a custom fnction? yes/no")
            if selection == "yes":
                func = input("Input the inline python function")
                query = func
    retval = 'from manimlib.imports import *\nfrom math import *\n'
    retval += 'class Solution(GraphScene):'
    if graph == True:
        retval += generate_config(func)


    retval += '\n\tdef construct(self):'
    retval += watermark
    #retval += "align_mark = TextMobject( 'abs', height = 1 , width = 1, fill_opacity=0)\n\t\talign_mark.next_to(Solve,2*DOWN)\n\t\t"
    sol_length = len(latexArr) - 1 # 1st line is the question
    if len(latexArr) >= 1 :
        retval = retval + 'Solve' + generateTexMobject(latexArr[0])
        retval = retval + 'Solve.to_edge(UP)\n\t\t'+'self.play(Write(Solve))\n\t\t'
        retval = retval + "align_mark = TexMobject( r'abs', fill_opacity=0.00,height=0.5)\n\t\t"
        retval = retval + 'align_mark.next_to(Solve,DOWN)\n\t\t'#+'self.play(Write(align_mark))\n\t\t'
        #retval = retval + 'align_mark.move_to(DOWN)\n\t\t'
        retval = retval + 'self.wait(1)\n\t\t'
        for i in range(1, len(latexArr)):
            retval = retval + 'R'+ str(i-1) + generateTexMobject(latexArr[i])
            retval = retval + 'if R'+ str(i-1) + ".get_height() > 1:\n\t\t\tR"+ str(i-1) + ".set_height(height=1,stretch=False)\n\t\t"
            retval = retval + 'if R'+ str(i-1) + ".get_width() > 12:\n\t\t\tR"+ str(i-1) + ".set_width(width=12,stretch=False)\n\t\t"
        for i in range(3):
            if sol_length > i:
                if i == 0:
                    retval = retval + 'R' + str(i) + '.next_to(align_mark,DOWN)\n\t\t'
                    retval = retval + 'self.play(Write(R'+ str(i) +'))\n\t\tself.wait(1)\n\t\t'
                    #second_line.shift(3*DOWN)
                else:
                    retval += 'R' + str(i) + ".next_to(R"+ str(i-1) +", DOWN)\n\t\t"
                    retval = retval + 'self.play(Write(R'+ str(i) +'))\n\t\tself.wait(1)\n\t\t'
            else:
                break

        for i in range(3,sol_length):
            retval = retval + "self.play(FadeOut(R"+ str(i-3) +"))\n\t\t"
            retval = retval + 'self.play(ApplyMethod(R' + str(i-2) + '.next_to,align_mark,DOWN))\n\t\t'
            retval += "self.play(ApplyMethod(R"+str(i-1)+".next_to,R" + str(i-2) +", DOWN))\n\t\t"
            retval += 'R' + str(i) + ".next_to(R"+ str(i-1) +", DOWN)\n\t\t"
            retval = retval + 'self.play(Write(R'+ str(i) +'))\n\t\t'
            #retval = retval + 'self.play(\n\t\tself.wait(2)\n\t\t'

        ## Fade out every step
        for i in range(sol_length-1,sol_length-4,-1):
            if i >= 0:
                retval += 'self.play(FadeOut(R'+ str(i) +'))\n\t\t'
        retval = retval + 'self.play(FadeOut(Solve))\n\t\t'
        
        if graph == True:
            retval += construct_graph
    else:
        if graph != True:
            raise Exception('Latex array has no steps')
        else:
            #retval += "R0" + generateTexMobject(latexArr[0])
            #retval += 'self.play(Write(R0))\n\t\tself.wait(2)\n\t\tself.play(FadeOut(R0))\n\t\t'
            retval += construct_graph

    #if graph != True:
        #retval = retval + 'self.play(FadeOut(R0))'

    retval += "self.play(ApplyMethod(watermark.next_to,align_mark,DOWN))\n\t\t"
    retval += "self.play(FadeOut(watermark))\n"
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
	y_lim = max(abs(math.floor(min(y_vals))),abs(math.floor(max(y_vals))))
	y_range = [-1*y_lim,y_lim]
	config += "\t\t'y_min':\t" + str(y_range[0]) +",\n"
	config += "\t\t'y_max':\t" + str(y_range[1]) +",\n"
	marking_distance = math.ceil((y_range[1] - y_range[0])/10)

	#print(marking_distance)
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
