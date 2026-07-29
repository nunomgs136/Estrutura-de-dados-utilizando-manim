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
        # --- Configurações fixas (evita cálculos redundantes de scale) ---
        raio_no = 0.4
        cor_no = WHITE
        cor_aresta = GOLD

        def criar_no(rotulo, posicao):
            """Cria um círculo com o número centralizado dentro."""
            circulo = Circle(radius=raio_no, color=cor_no)
            texto = Text(rotulo, weight=BOLD, font_size=28)
            texto.move_to(circulo.get_center())
            circulo.move_to(posicao)
            texto.move_to(posicao)
            return VGroup(circulo, texto)

        def criar_aresta(no_origem, no_destino):
            """Cria uma linha entre as bordas de dois nós (não do centro)."""
            return Line(
                no_origem[0].get_center(),
                no_destino[0].get_center(),
                stroke_width=4,
                color=cor_aresta,
                z_index=-1,  # fica atrás dos círculos
            ).set_length(
                Line(no_origem[0].get_center(), no_destino[0].get_center()).get_length()
                - 2 * raio_no
            )

        # --- Posicionamento (espelha a imagem) ---
        pos_30 = UP * 2
        pos_15 = pos_30 + DOWN * 1.5 + LEFT * 2.5
        pos_45 = pos_30 + DOWN * 1.5 + RIGHT * 2.5
        pos_7  = pos_15 + DOWN * 1.5 + LEFT * 1.5
        pos_22 = pos_15 + DOWN * 1.5 + RIGHT * 1.5

        # --- Criação dos nós ---
        no_30 = criar_no("30", pos_30)
        no_15 = criar_no("15", pos_15)
        no_45 = criar_no("45", pos_45)
        no_7  = criar_no("7", pos_7)
        no_22 = criar_no("22", pos_22)

        # --- Criação das arestas ---
        aresta_30_15 = criar_aresta(no_30, no_15)
        aresta_30_45 = criar_aresta(no_30, no_45)
        aresta_15_7  = criar_aresta(no_15, no_7)
        aresta_15_22 = criar_aresta(no_15, no_22)

        arvore = VGroup(
            aresta_30_15, aresta_30_45, aresta_15_7, aresta_15_22,
            no_30, no_15, no_45, no_7, no_22,
        )

        # --- Animação ---
        self.play(
            LaggedStart(
                FadeIn(no_30),
                Create(VGroup(aresta_30_15, aresta_30_45)),
                FadeIn(no_15, no_45),
                Create(VGroup(aresta_15_7, aresta_15_22)),
                FadeIn(no_7, no_22),
                lag_ratio=0.4,
            )
        )
        self.wait()

        # Reposiciona a árvore inteira, se precisar (ex: para mostrar código ao lado)
        self.play(arvore.animate.shift(LEFT * 2).scale(0.7))
        self.wait()

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

class ListaDuplamenteLigada(Scene):
    def construct(self):
        # --- Configurações fixas ---
        lado_no = 0.8
        espaco_horizontal = 4.6
        cor_no = WHITE
        cor_seta = GOLD

        def criar_no(rotulo, posicao):
            """Cria um quadrado com o valor centralizado dentro."""
            retangulo = Rectangle(grid_ystep = 3.0, grid_xstep = 1.30)
            ''' line1 = Line(
            start=retangulo.get_center() + LEFT * 0.85 + DOWN,
            end=retangulo.get_center() + LEFT * 0.85 + UP
        	)
            line2 = Line(
            start=retangulo.get_center() + RIGHT * 0.85 + DOWN,
            end=retangulo.get_center() + RIGHT * 0.85 + UP
        	) '''
            texto = Text(rotulo, weight=BOLD, font_size=28)
            retangulo.move_to(posicao)
            texto.move_to(posicao)
            return VGroup(retangulo, texto)

        def criar_seta_dupla(no_origem, no_destino):
            """Cria uma seta bidirecional entre as bordas de dois nós."""
            return DoubleArrow(
                no_origem[0].get_right(),
                no_destino[0].get_left(),
                stroke_width=4,
                color=cor_seta,
                buff=0.05,
                tip_length=0.15,
            )

        # --- Valores da lista (baseado na imagem) ---
        valores = [ "2", "3", "4"]
        n = len(valores)

        # --- Posicionamento em linha, centralizado ---
        largura_total = (n - 1) * espaco_horizontal
        posicoes = [
            LEFT * (largura_total / 2) + RIGHT * i * espaco_horizontal
            for i in range(n)
        ]

        # --- Criação dos nós ---
        nos = [criar_no(valores[i], posicoes[i]) for i in range(n)]

        # --- Criação das setas entre nós consecutivos ---
        setas = [criar_seta_dupla(nos[i], nos[i + 1]) for i in range(n - 1)]

        lista = VGroup(*nos, *setas)

        # --- Animação ---
        self.play(FadeIn(nos[0]))
        for i in range(n - 1):
            self.play(
                Create(setas[i]),
                FadeIn(nos[i + 1]),
            )
        self.wait()

        # Reposiciona a lista inteira, se precisar
        self.play(lista.animate.scale(0.8).shift(UP * 1.5))
        self.wait()

class VerticalLineInSquare(Scene):
    def construct(self):
        # Create a square with a side length of 4 units
        sq = Rectangle()
        
        # Create a vertical line matching the height of the square
        # top edge is UP * 2, bottom edge is DOWN * 2

        texto = Text("5", weight=BOLD, font_size=40)
        texto.move_to(sq.get_center())


        # Group them together so they act as one object
        grouped_shape = VGroup(sq, line1,line2,texto)
        
        # Animate drawing the group on the screen
        self.play(Create(grouped_shape))
        self.wait(1)
