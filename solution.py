from manimlib.imports import *
from math import *
class Solution(GraphScene):
	def construct(self):
		watermark = ImageMobject("./assets/water_mark.png",opacity=0.7)
		watermark.scale(1.5)
		watermark.to_corner(DOWN+RIGHT, buff=0)
		self.play(FadeIn(watermark))
		Solve = TexMobject(r"\int_{-4}^{4} \sqrt{16 - x^{2}} \ dx" )
		Solve.to_edge(UP)
		self.play(Write(Solve))
		align_mark = TexMobject( r'abs', fill_opacity=0.00,height=0.5)
		align_mark.next_to(Solve,DOWN)
		self.wait(1)
		R0 = TexMobject(r" For \ the \ integrand \  \sqrt{16 \linebreak - x^{2}}, \ substitute \ x = 4 \sin(u) \ and \ dx = 4 \cos(u) \ du." )
		if R0.get_height() > 1:
			R0.set_height(height=1,stretch=False)
		if R0.get_width() > 10:
			R0.set_width(width=10,stretch=True)
		R1 = TexMobject(r" Then\  \sqrt{16 - x^{2}} = \sqrt{16 - \linebreak 16 \sin^2(u)} = 4 \sqrt{ \cos^2(u)}." )
		if R1.get_height() > 1:
			R1.set_height(height=1,stretch=False)
		if R1.get_width() > 10:
			R1.set_width(width=10,stretch=True)
		R2 = TexMobject(r" This \ substitution \ is \ invertible \ \linebreak over \ -\frac{\pi}{2}<u<\frac{\pi}{2} \ with \ inverse \ u = \sin^{-1}\frac{x}{4}." )
		if R2.get_height() > 1:
			R2.set_height(height=1,stretch=False)
		if R2.get_width() > 10:
			R2.set_width(width=10,stretch=True)
		R3 = TexMobject(r" This \ gives \ a \ new \ \linebreak lower \ bound \ u = \sin^{-1}\frac{-4}{4} = -\frac{\pi}{2} \ and \ upper \ bound \ u = \sin^{-1}\frac{4}{4} = \frac{\pi}{2}:" )
		if R3.get_height() > 1:
			R3.set_height(height=1,stretch=False)
		if R3.get_width() > 10:
			R3.set_width(width=10,stretch=True)
		R4 = TexMobject(r" = 4 \int_{{-\pi}/{2}}^{{\pi}/{2}} 4 \cos(u) \sqrt{\cos^2(u)} \ du \linebreak " )
		if R4.get_height() > 1:
			R4.set_height(height=1,stretch=False)
		if R4.get_width() > 10:
			R4.set_width(width=10,stretch=True)
		R5 = TexMobject(r" Factor \ out \ constants:" )
		if R5.get_height() > 1:
			R5.set_height(height=1,stretch=False)
		if R5.get_width() > 10:
			R5.set_width(width=10,stretch=True)
		R6 = TexMobject(r" = 16 \int_{-{\pi}/{2}}^{{\pi}/{2}} \cos(u) \sqrt{\cos^2(u)} \ du \linebreak " )
		if R6.get_height() > 1:
			R6.set_height(height=1,stretch=False)
		if R6.get_width() > 10:
			R6.set_width(width=10,stretch=True)
		R7 = TexMobject(r" Simplify \ \cos(u) \sqrt{ \cos^{2}(u)} \ assuming \ \linebreak -\frac{\pi}{2}<u<\frac{\pi}{2}" )
		if R7.get_height() > 1:
			R7.set_height(height=1,stretch=False)
		if R7.get_width() > 10:
			R7.set_width(width=10,stretch=True)
		R8 = TexMobject(r" = 16 \int_{-{\pi}/{2}}^{{\pi}/{2}} \cos^2(u) \ du" )
		if R8.get_height() > 1:
			R8.set_height(height=1,stretch=False)
		if R8.get_width() > 10:
			R8.set_width(width=10,stretch=True)
		R9 = TexMobject(r" Write \cos^{2}(u) \ as \ \frac{1}{2} \cos(2 u) \linebreak + \frac{1}{2}:" )
		if R9.get_height() > 1:
			R9.set_height(height=1,stretch=False)
		if R9.get_width() > 10:
			R9.set_width(width=10,stretch=True)
		R10 = TexMobject(r" = 16 \int_{-{\pi}/{2}}^{{\pi}/{2}} (\frac{1}{2} \cos(2 u) + \frac{1}{2}) \linebreak \ du" )
		if R10.get_height() > 1:
			R10.set_height(height=1,stretch=False)
		if R10.get_width() > 10:
			R10.set_width(width=10,stretch=True)
		R11 = TexMobject(r" Integrate \ the \ sum \ term \ \linebreak by \ term \ and \ factor \ out \ constants:" )
		if R11.get_height() > 1:
			R11.set_height(height=1,stretch=False)
		if R11.get_width() > 10:
			R11.set_width(width=10,stretch=True)
		R12 = TexMobject(r" = 8 \int_{-{\pi}/{2}}^{{\pi}/{2}} \cos(2 u) \ du + \linebreak 8 \int_{-{\pi}/{2}}^{{\pi}/{2}} 1 \ du" )
		if R12.get_height() > 1:
			R12.set_height(height=1,stretch=False)
		if R12.get_width() > 10:
			R12.set_width(width=10,stretch=True)
		R13 = TexMobject(r" For \ the \ integrand \cos(2 u), \ \linebreak substitute \ s = 2 u \ and \ ds = 2 \ du." )
		if R13.get_height() > 1:
			R13.set_height(height=1,stretch=False)
		if R13.get_width() > 10:
			R13.set_width(width=10,stretch=True)
		R14 = TexMobject(r" This \ gives \ a \ new \ \linebreak lower \ bound \ s = \frac{-2\pi}{ 2} = -\pi \ and \ upper \ bound \ s = \frac{2\pi}{ 2} = \pi:" )
		if R14.get_height() > 1:
			R14.set_height(height=1,stretch=False)
		if R14.get_width() > 10:
			R14.set_width(width=10,stretch=True)
		R15 = TexMobject(r" = 4 \int_{-\pi}^{\pi} \cos(s) \ ds + 8 \linebreak \int_{-\pi/2}^{\pi/2} 1 \ du" )
		if R15.get_height() > 1:
			R15.set_height(height=1,stretch=False)
		if R15.get_width() > 10:
			R15.set_width(width=10,stretch=True)
		R16 = TexMobject(r" Apply \ the \ fundamental \ theorem \ \linebreak of \ calculus." )
		if R16.get_height() > 1:
			R16.set_height(height=1,stretch=False)
		if R16.get_width() > 10:
			R16.set_width(width=10,stretch=True)
		R17 = TexMobject(r" The \ antiderivative \ of \cos(s) \ is \linebreak \sin(s):" )
		if R17.get_height() > 1:
			R17.set_height(height=1,stretch=False)
		if R17.get_width() > 10:
			R17.set_width(width=10,stretch=True)
		R18 = TexMobject(r" = 4 \sin(s) | _{-\pi}^{\pi} + 8 \int_{-\pi/2}^{\pi/2} \linebreak 1 \ du" )
		if R18.get_height() > 1:
			R18.set_height(height=1,stretch=False)
		if R18.get_width() > 10:
			R18.set_width(width=10,stretch=True)
		R19 = TexMobject(r" Evaluate \ the \ antiderivative \ at \ \linebreak the \ limits \ and \ subtract." )
		if R19.get_height() > 1:
			R19.set_height(height=1,stretch=False)
		if R19.get_width() > 10:
			R19.set_width(width=10,stretch=True)
		R20 = TexMobject(r" 4 \sin(s) |_{-\pi}^\pi = 4 \sin(\pi) - 4 \linebreak \sin(-\pi) = 0:" )
		if R20.get_height() > 1:
			R20.set_height(height=1,stretch=False)
		if R20.get_width() > 10:
			R20.set_width(width=10,stretch=True)
		R21 = TexMobject(r" = 8 \int_{-{\pi}/{2}}^{{\pi}/{2}} 1 \  du \linebreak " )
		if R21.get_height() > 1:
			R21.set_height(height=1,stretch=False)
		if R21.get_width() > 10:
			R21.set_width(width=10,stretch=True)
		R22 = TexMobject(r" Apply \ the \ fundamental \ theorem \ \linebreak of \ calculus." )
		if R22.get_height() > 1:
			R22.set_height(height=1,stretch=False)
		if R22.get_width() > 10:
			R22.set_width(width=10,stretch=True)
		R23 = TexMobject(r" The \ antiderivative \ of \ 1 \ \linebreak is \ u:" )
		if R23.get_height() > 1:
			R23.set_height(height=1,stretch=False)
		if R23.get_width() > 10:
			R23.set_width(width=10,stretch=True)
		R24 = TexMobject(r" = 8 u| _{-{\pi}/{2}}^{{\pi}/{2}}" )
		if R24.get_height() > 1:
			R24.set_height(height=1,stretch=False)
		if R24.get_width() > 10:
			R24.set_width(width=10,stretch=True)
		R25 = TexMobject(r" Evaluate \ the \ antiderivative \ at \ \linebreak the \ limits \ and \ subtract." )
		if R25.get_height() > 1:
			R25.set_height(height=1,stretch=False)
		if R25.get_width() > 10:
			R25.set_width(width=10,stretch=True)
		R26 = TexMobject(r" 8 u |_{-\pi/2}^{\pi/2} = \frac{8 \pi}{2} - \frac{8 \linebreak (-\pi)}{2} = 8 \pi:" )
		if R26.get_height() > 1:
			R26.set_height(height=1,stretch=False)
		if R26.get_width() > 10:
			R26.set_width(width=10,stretch=True)
		R27 = TexMobject(r" Answer: = 8\pi" )
		if R27.get_height() > 1:
			R27.set_height(height=1,stretch=False)
		if R27.get_width() > 10:
			R27.set_width(width=10,stretch=True)
		R0.next_to(align_mark,DOWN)
		self.play(Write(R0))
		self.wait(1)
		R1.next_to(R0, DOWN)
		self.play(Write(R1))
		self.wait(1)
		R2.next_to(R1, DOWN)
		self.play(Write(R2))
		self.wait(1)
		self.play(FadeOut(R0))
		self.play(ApplyMethod(R1.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R2.next_to,R1, DOWN))
		R3.next_to(R2, DOWN)
		self.play(Write(R3))
		self.play(FadeOut(R1))
		self.play(ApplyMethod(R2.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R3.next_to,R2, DOWN))
		R4.next_to(R3, DOWN)
		self.play(Write(R4))
		self.play(FadeOut(R2))
		self.play(ApplyMethod(R3.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R4.next_to,R3, DOWN))
		R5.next_to(R4, DOWN)
		self.play(Write(R5))
		self.play(FadeOut(R3))
		self.play(ApplyMethod(R4.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R5.next_to,R4, DOWN))
		R6.next_to(R5, DOWN)
		self.play(Write(R6))
		self.play(FadeOut(R4))
		self.play(ApplyMethod(R5.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R6.next_to,R5, DOWN))
		R7.next_to(R6, DOWN)
		self.play(Write(R7))
		self.play(FadeOut(R5))
		self.play(ApplyMethod(R6.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R7.next_to,R6, DOWN))
		R8.next_to(R7, DOWN)
		self.play(Write(R8))
		self.play(FadeOut(R6))
		self.play(ApplyMethod(R7.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R8.next_to,R7, DOWN))
		R9.next_to(R8, DOWN)
		self.play(Write(R9))
		self.play(FadeOut(R7))
		self.play(ApplyMethod(R8.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R9.next_to,R8, DOWN))
		R10.next_to(R9, DOWN)
		self.play(Write(R10))
		self.play(FadeOut(R8))
		self.play(ApplyMethod(R9.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R10.next_to,R9, DOWN))
		R11.next_to(R10, DOWN)
		self.play(Write(R11))
		self.play(FadeOut(R9))
		self.play(ApplyMethod(R10.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R11.next_to,R10, DOWN))
		R12.next_to(R11, DOWN)
		self.play(Write(R12))
		self.play(FadeOut(R10))
		self.play(ApplyMethod(R11.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R12.next_to,R11, DOWN))
		R13.next_to(R12, DOWN)
		self.play(Write(R13))
		self.play(FadeOut(R11))
		self.play(ApplyMethod(R12.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R13.next_to,R12, DOWN))
		R14.next_to(R13, DOWN)
		self.play(Write(R14))
		self.play(FadeOut(R12))
		self.play(ApplyMethod(R13.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R14.next_to,R13, DOWN))
		R15.next_to(R14, DOWN)
		self.play(Write(R15))
		self.play(FadeOut(R13))
		self.play(ApplyMethod(R14.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R15.next_to,R14, DOWN))
		R16.next_to(R15, DOWN)
		self.play(Write(R16))
		self.play(FadeOut(R14))
		self.play(ApplyMethod(R15.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R16.next_to,R15, DOWN))
		R17.next_to(R16, DOWN)
		self.play(Write(R17))
		self.play(FadeOut(R15))
		self.play(ApplyMethod(R16.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R17.next_to,R16, DOWN))
		R18.next_to(R17, DOWN)
		self.play(Write(R18))
		self.play(FadeOut(R16))
		self.play(ApplyMethod(R17.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R18.next_to,R17, DOWN))
		R19.next_to(R18, DOWN)
		self.play(Write(R19))
		self.play(FadeOut(R17))
		self.play(ApplyMethod(R18.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R19.next_to,R18, DOWN))
		R20.next_to(R19, DOWN)
		self.play(Write(R20))
		self.play(FadeOut(R18))
		self.play(ApplyMethod(R19.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R20.next_to,R19, DOWN))
		R21.next_to(R20, DOWN)
		self.play(Write(R21))
		self.play(FadeOut(R19))
		self.play(ApplyMethod(R20.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R21.next_to,R20, DOWN))
		R22.next_to(R21, DOWN)
		self.play(Write(R22))
		self.play(FadeOut(R20))
		self.play(ApplyMethod(R21.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R22.next_to,R21, DOWN))
		R23.next_to(R22, DOWN)
		self.play(Write(R23))
		self.play(FadeOut(R21))
		self.play(ApplyMethod(R22.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R23.next_to,R22, DOWN))
		R24.next_to(R23, DOWN)
		self.play(Write(R24))
		self.play(FadeOut(R22))
		self.play(ApplyMethod(R23.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R24.next_to,R23, DOWN))
		R25.next_to(R24, DOWN)
		self.play(Write(R25))
		self.play(FadeOut(R23))
		self.play(ApplyMethod(R24.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R25.next_to,R24, DOWN))
		R26.next_to(R25, DOWN)
		self.play(Write(R26))
		self.play(FadeOut(R24))
		self.play(ApplyMethod(R25.next_to,align_mark,DOWN))
		self.play(ApplyMethod(R26.next_to,R25, DOWN))
		R27.next_to(R26, DOWN)
		self.play(Write(R27))
		self.play(FadeOut(R27))
		self.play(FadeOut(R26))
		self.play(FadeOut(R25))
		self.play(FadeOut(Solve))
		