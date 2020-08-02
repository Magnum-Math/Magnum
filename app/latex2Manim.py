def generateTexMobject(line):
    retval = ' = TexMobject(r"' + line.split("\n")[0]+ '")\n\t\t'
    return retval

def latex2Manim(latexArr):
    retval = 'class Solution(Scene):\n\tdef construct(self):\n\t\t'
    if len(latexArr) > 2 :
        retval = retval + 'Solve' + generateTexMobject(latexArr[0])
        retval = retval + 'Solve.to_edge(UP)\n\t\t'+'self.play(Write(Solve))\n\t\t'
        retval = retval + 'self.wait(2)\n\t\t'
        retval = retval + 'R0' + generateTexMobject(latexArr[1])
        retval = retval + 'self.play(Write(R0))\n\t\tself.wait(2)\n\t\t'

        for i in range(2,len(latexArr)):
            retval = retval + 'R1' + generateTexMobject(latexArr[i])
            retval = retval + 'self.play(Transform(R0,R1))\n\t\tself.wait(2)\n\t\t'

    else:
        raise Exception('Latex array has no steps')

    retval = retval + 'self.play(FadeOut(R0))'
    return retval

def readFile2Array(path_to_file):
	file = open(path_to_file)
	retval = file.readlines()
	file.close()
	return retval
    
"""
src = './2.txt'

latex = readFile2Array(src)
print(len(latex))
for line in latex:
    print(line,end="")
print ("")
print(latex2Manim(latex))
"""
