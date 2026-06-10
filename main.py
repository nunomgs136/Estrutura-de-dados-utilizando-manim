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
		c = Circle()
		testeTexto = Text("22", weight = BOLD, font_size = 15)
		teste2 = Text("21", weight = BOLD, font_size = 15)
		teste3 = Text("23", weight = BOLD, font_size = 15)
		testeTexto.move_to(a.get_center())

		a.scale_to_fit_height(config.frame_height)
		b.scale_to_fit_height(config.frame_height)
		c.scale_to_fit_height(config.frame_height)
		a.scale_to_fit_width(config.frame_width)
		b.scale_to_fit_width(config.frame_width)
		c.scale_to_fit_width(config.frame_width)
		a.scale(0.08)
		b.scale(0.08)
		c.scale(0.08)
		b.next_to(a, DOWN, buff = 0.5)
		c.next_to(a,DOWN, buff = 0.5)
		b.shift(LEFT * 2)
		c.shift(RIGHT * 2)
		teste2.move_to(b.get_center())
		teste3.move_to(c.get_center())
		#self.play(FadeIn(a))
		#self.play(FadeIn(b))
		seta = Arrow(start=a.get_center(), end=b.get_center(), stroke_width=6, color=GOLD, max_tip_length_to_length_ratio = 0)
		seta2 = Arrow(start=a.get_center(), end=c.get_center(), stroke_width=6, color=GOLD, max_tip_length_to_length_ratio = 0)
		self.play(FadeIn(seta,seta2,a,b,c,testeTexto,teste2,teste3))
		grupo = VGroup(a,b,c,seta,seta2,testeTexto,teste2,teste3)
		self.play(grupo.animate.shift(LEFT * 2), grupo.animate.scale(0.5))

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
class TextoExplicacao(Scene):
	def construct(self):
		titulo = Text("O que é uma árvore AVL?", font_size = 50, weight = BOLD)
		titulo.to_edge(UP)
		self.play(Write(titulo))
		texto = Text("Uma árvore AVL é uma árvore autobalanceável, ou seja, segue o seguinte princípio:", font_size = 20)
		self.play(Write(texto))
		texto2 = MarkupText(f'* Um novo nó é inserido na árvore \n * É checado o balanceamento de cada nó \n * <span fgcolor = "{RED}">Se todos os nós tiveram um fator de balanceamento entre -1 e 1 </span>, a árvore está balanceada.', font_size = 20)
		texto2.next_to(texto, DOWN)
		self.play(Write(texto2))
		texto3 = Text("Mas como calcular o fator de balanceamento? ", weight=BOLD, font_size = 20)
		texto3.to_edge(DOWN)
		self.play(Write(texto3))
		self.play(FadeOut(titulo,texto,texto2,texto3))


class CirurgiaSiamesa(Scene):
	def construct(self):
		self.texto_titulo()
		self.texto_explicacao()
		self.texto_formula()
	
	def texto_titulo(self):
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
		self.play(FadeOut(titulo))
		self.remove(cursor)
	def texto_formula(self):
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
		self.play(FadeOut(titulo,formula,texto))
		self.wait(3)
	def texto_explicacao(self):
		titulo = Text("O que é uma árvore AVL?", font_size = 50, weight = BOLD)
		titulo.to_edge(UP)
		self.play(Write(titulo))
		texto = Text("Uma árvore AVL é uma árvore autobalanceável, ou seja, segue o seguinte princípio:", font_size = 20)
		self.play(Write(texto))
		texto2 = MarkupText(f'* Um novo nó é inserido na árvore \n * É checado o balanceamento de cada nó \n * <span fgcolor = "{RED}">Se todos os nós tiveram um fator de balanceamento entre -1 e 1 </span>, a árvore está balanceada.', font_size = 20)
		texto2.next_to(texto, DOWN)
		self.play(Write(texto2))
		texto3 = Text("Mas como calcular o fator de balanceamento? ", weight=BOLD, font_size = 20)
		texto3.to_edge(DOWN)
		self.play(Write(texto3))
		self.play(FadeOut(titulo,texto,texto2,texto3), scale=0.5)
