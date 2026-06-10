from manim import *
class CreateCircle(Scene):
	def construct(self):
		circle = Circle()
		circle.set_fill(PINK, opacity = 0.5)
		self.play(Create(circle))

class SquareToCircle(Scene):
	def construct(self):
		circle = Circle()
		circle.set_fill(PINK, opacity = 0.5)

		square = Square()
		square.rotate(PI/4)
		self.play(Create(square))
		self.play(Transform(square,circle))
		self.play(FadeOut(square))
class SquareAndCircle(Scene):
	def construct(self):
		circle = Circle()
		circle.set_fill(PINK, opacity = 0.5)

		square = Square()
		square.set_fill(BLUE, opacity = 0.5)
		
		square.next_to(circle, LEFT)
		self.play(Create(circle), Create(square))
class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(Transform(square, circle))  # transform the square into a circle
        self.play(
            square.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen

class DifferentRotations(Scene):
	def construct(self):
		left_square = Square(color=BLUE, fill_opacity=0.7).shift(0.2*LEFT)
		right_square = Square(color=GREEN, fill_opacity=0.7).shift(0.2*RIGHT)
		left_square.next_to(right_square, LEFT, buff = 0.5)
		self.play(
			left_square.animate.rotate(PI), Rotate(right_square, angle = PI), run_time = 2)
		self.wait()
class TwoTransforms(Scene):
	def transform(self):
		a = Circle()
		b = Square()
		c = Triangle()
		self.play(Transform(a,b))
		self.play(Transform(a,c))
		self.play(FadeOut(a))
	def replacement_transform(self):	
		a = Circle()
		b = Square()
		c = Triangle()
		self.play(ReplacementTransform(a,b))
		self.play(ReplacementTransform(b,c))
		self.play(FadeOut(c))
	def construct(self):
		self.transform()
		self.wait(0.5)
		self.replacement_transform()

class TesteSecoes(Scene):
		def construct(self):
			# Conteúdo de CreateCircle
			circle = Circle()
			circle.set_fill(PINK, opacity=0.5)

			self.play(Create(circle))
			self.wait(1)
			circle.shift(LEFT)
			circle.animate.shift(DOWN)
			self.next_section()
			

			# Conteúdo de TwoTransforms
			self.wait(2)
			a = Circle()
			b = Square()
			c = Triangle()
			self.play(Transform(a, b))
			self.play(Transform(a, c))
			self.play(FadeOut(a))
class HelloWorld(Scene):
    def construct(self):
        text = Text("A árvore AVL é uma árvore na qual todos os seus vértices estão balanceados", color=BLUE , font_size=12, font="Cursive")
        self.add(text)
        self.play(FadeIn(text))

class TentarArvore(Scene):
	def construct(self):
		a = Circle()
		b = Circle()

		a.scale_to_fit_height(config.frame_height)
		b.scale_to_fit_height(config.frame_height)
		a.scale_to_fit_width(config.frame_width)
		b.scale_to_fit_width(config.frame_width)
		a.scale(0.25)
		b.scale(0.25)
		b.next_to(a, RIGHT, buff = 0.5)
		#self.play(FadeIn(a))
		#self.play(FadeIn(b))
		seta = Arrow(start=a.get_center(), end=b.get_center(), stroke_width=6, color=GOLD, max_tip_length_to_length_ratio = 0)
		self.add(seta)
		self.play(FadeIn(seta,a,b))

class TextoFormulaFB(Scene):
	def construct(self):
		titulo = Text("Fator de balanceamento", weight = BOLD, font_size = 50)
		titulo.to_edge(UP)
		formula = Tex(r"${F}_b = {h}_d - {h}_e$", font_size = 80)
		self.play(Write(titulo)) #Animação para escrever texto na tela 
		self.wait(1) #Espera um segundo
		self.play(Write(formula)) # Escreve fórmula
		texto = Tex(r"${F}_b$ é o fator de balanceamento \\", r"${h}_d$ é a altura do ramo direito \\", r"${h}_e$ é a altura do ramo esquerdo", font_size = 30)
		texto.shift(DOWN * 3)
		texto.shift(LEFT * 2)
		self.play(Write(texto))
		self.wait(10)
		self.play(FadeOut(titulo))
		self.play(FadeOut(formula))
		self.play(FadeOut(texto))
		self.wait(3)

class TextoTitulo(Scene):
	def construct(self):
		titulo = Text("Árvores AVL", weight = ULTRAHEAVY, font_size = 100)
		cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = 1.1,
            width = 0.5,
        ).move_to(titulo[0])
		self.play(TypeWithCursor(titulo, cursor))
		self.play(Blink(cursor, blinks=5))
		self.wait(5)
		self.play(Blink(cursor, blinks=2))
		self.play(FadeOut(titulo))
		self.remove(cursor)
	

