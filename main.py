from tkinter import LEFT, Text

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
class TextoExercicio(Scene):
    def construct(self):
        titulo = Text("Exemplo", weight = BOLD, font_size = 50)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        texto = Text("Considere a inserção do elemento 20 e a posterior realização das operações de balanceamento (caso sejam necessárias). \n Após essas etapas, ao realizar o percurso na árvore em in-ordem, qual será a sequência de visita dos nós\?", font_size = 20)
        texto.next_to(titulo, DOWN)
        self.play(Write(texto))
        self.wait(10)
        self.play(FadeOut(titulo,texto))
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
        pos_20 = pos_22 + DOWN * 1.5 + LEFT * 1.5

        # --- Criação dos nós ---
        no_30 = criar_no("30", pos_30)
        no_15 = criar_no("15", pos_15)
        no_45 = criar_no("45", pos_45)
        no_7  = criar_no("7", pos_7)
        no_22 = criar_no("22", pos_22)
        no_20 = criar_no("20", pos_20)

        # --- Criação das arestas ---
        aresta_30_15 = criar_aresta(no_30, no_15)
        aresta_30_45 = criar_aresta(no_30, no_45)
        aresta_15_7  = criar_aresta(no_15, no_7)
        aresta_15_22 = criar_aresta(no_15, no_22)
        aresta_22_20 = criar_aresta(no_22, no_20)
        arvore = VGroup(
            aresta_30_15, aresta_30_45, aresta_15_7, aresta_15_22, aresta_22_20,
            no_30, no_15, no_45, no_7, no_22, no_20,
        )

        # --- Animação ---
        self.play(
            LaggedStart(
                FadeIn(no_30),
                Create(VGroup(aresta_30_15, aresta_30_45)),
                FadeIn(no_15, no_45),
                Create(VGroup(aresta_15_7, aresta_15_22)),
                FadeIn(no_7, no_22),
				Create(aresta_22_20),
				FadeIn(no_20),
                lag_ratio=0.4,
            )
        )
        self.wait()

        # Reposiciona a árvore inteira, se precisar (ex: para mostrar código ao lado)
        #self.play(arvore.animate.shift(LEFT * 2).scale(0.7))
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

from manim import *

class ListaDuplamenteLigada(Scene):
    def construct(self):
        # --- Configurações fixas ---
        lado_no = 0.8
        espaco_horizontal = 4.6
        cor_no = WHITE
        cor_seta = GOLD
        n = 4  # Número de nós na lista
        def criar_no(rotulo, posicao):
            """Cria um quadrado com o valor centralizado dentro."""
            retangulo = Rectangle(
            width=4,
            height=2,
            grid_ystep=3.0,
            grid_xstep=1.30,
            color=cor_no,
            )
            texto = Text(rotulo, weight=BOLD, font_size=28)
            retangulo.move_to(posicao)
            texto.move_to(posicao)
            return VGroup(retangulo, texto)

        def criar_seta(no_origem, no_destino):

            seta1 = Arrow(
                start=no_origem[0].get_right(),
                end=no_destino[0].get_left(),
                stroke_width=4,
                color=cor_seta,
                buff=0.05,
            )
            seta2 = Arrow(
                start=no_destino[0].get_left(),
                end=no_origem[0].get_right(),
                stroke_width=4,
                color=cor_seta,
                buff=0.05,
            )
            seta2.shift(DOWN * 0.2)  # Ajusta a posição da seta de volta
            return VGroup(seta1, seta2)
        def remover_seta(seta):
            self.play(FadeOut(seta))
            self.wait()
        def remover_no(no,lista):
            self.play(FadeOut(no))
            lista.remove(no)
            self.wait()
        def reposicionar_lista(lista, nova_posicao):
            self.play(lista.animate.move_to(nova_posicao))
            self.wait()
        def remocao_completa(lista, nos, setas, indice):
            if not 0 <= indice < len(nos):
                raise IndexError("Índice de nó inválido")

            no_removido = nos[indice]

            # setas[i] liga nos[i] a nos[i + 1].
            afetadas = [
                seta
                for i, seta in enumerate(setas)
                if i in (indice - 1, indice)
            ]

            preservadas = [
                (seta, nos[i])
                for i, seta in enumerate(setas)
                if i not in (indice - 1, indice)
            ]

            # Se há vizinhos dos dois lados, prepara a nova ligação.
            # A cópia preserva o tamanho e o estilo das setas já escaladas.
            nova_seta = None

            if 0 < indice < len(nos) - 1:
                nova_seta = setas[indice - 1].copy()
                vizinho_esquerdo = nos[indice - 1]
                posicao_anterior = vizinho_esquerdo.get_center().copy()

            self.play(
                FadeOut(no_removido),
                *[FadeOut(seta) for seta in afetadas],
            )

            lista.remove(no_removido, *afetadas)
            nos.pop(indice)
            setas[:] = [seta for seta, _ in preservadas]

            if not nos:
                return

            largura_total = (len(nos) - 1) * espaco_horizontal

            destinos = [
                RIGHT * (i * espaco_horizontal - largura_total / 2)
                for i in range(len(nos))
            ]

            # Calcula os deslocamentos antes de começar a animação.
            deslocamentos = {
                id(no): destino - no.get_center()
                for no, destino in zip(nos, destinos)
            }

            self.play(
                *[
                    no.animate.move_to(destino)
                    for no, destino in zip(nos, destinos)
                ],
                *[
                    seta.animate.shift(deslocamentos[id(origem)])
                    for seta, origem in preservadas
                ],
            )

            if nova_seta is not None:
                nova_seta.shift(
                    vizinho_esquerdo.get_center() - posicao_anterior
                )

                # Mantém a ordem das ligações na lista Python.
                setas.insert(indice - 1, nova_seta)
                lista.add(nova_seta)

                self.play(Create(nova_seta))

            self.wait()
        def ajustar_setas(nos, setas):
            for i in range(len(setas)):
                seta1, seta2 = setas[i]
                seta1.put_start_and_end_on(
                    nos[i][0].get_right(), nos[i + 1][0].get_left()
                )
                seta2.put_start_and_end_on(
                    nos[i + 1][0].get_left(), nos[i][0].get_right()
                )
                seta2.shift(DOWN * 0.2)
            self.wait()
        n = 4  # Número de nós na lista
        # --- Posicionamento em linha, centralizado ---
        largura_total = (n - 1) * espaco_horizontal
        posicoes = [
            LEFT * (largura_total / 2) + RIGHT * i * espaco_horizontal
            for i in range(n)
        ]

        # --- Criação dos nós ---
        nos = [criar_no(str(i), posicoes[i]) for i in range(n)]

        # --- Criação das setas entre nós consecutivos ---
        setas = [criar_seta(nos[i], nos[i + 1]) for i in range(3)]
        lista = VGroup(*nos, *setas)
        # Margem em cada lado da cena, em unidades do Manim.
        margem = 0.5

        largura_disponivel = config.frame_width - 2 * margem
        altura_disponivel = config.frame_height - 2 * margem

        # Reduz apenas quando necessário, preservando as proporções.
        fator = min(
            1.0,
            largura_disponivel / lista.width,
            altura_disponivel / lista.height,
        )

        lista.scale(fator)
        lista.move_to(ORIGIN)

        # Mantém o reposicionamento após a remoção compatível
        # com o tamanho que acabamos de aplicar.
        espaco_horizontal *= fator

        # --- Animação ---
        self.play(FadeIn(nos[0]))
        for i in range(n-1):
            self.play(
                Create(setas[i]),
                FadeIn(nos[i + 1]),
            )
        self.wait()
        
        remocao_completa(lista, nos, setas, 1)
        #ajustar_setas(nos, setas)
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
class TextoTituloListas(Scene):
	def construct(self):
		titulo = Text("Listas Duplamente Ligadas", weight = ULTRAHEAVY, font_size = 50)
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
class TextoExplicacaoListas(Scene):
    def construct(self):
        titulo = Text("O que é uma lista duplamente ligada?", font_size = 50, weight = BOLD)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        texto = Text("Uma lista duplamente ligada é uma estrutura de dados linear na qual cada elemento (ou nó) \n contém referências para o próximo e o anterior elemento da lista.",font_size = 20)
        self.play(Write(texto))
        texto2 = MarkupText(f'* Cada nó possui um ponteiro para o próximo nó \n * Cada nó possui um ponteiro para o nó anterior \n * Permite percorrer a lista em ambas as direções', font_size = 20)
        texto2.next_to(texto, DOWN)
        self.play(Write(texto2))
        self.wait(10)
        self.play(FadeOut(titulo,texto,texto2))
class RepresentacaoListas(Scene):
    def construct(self):
        def criar_no(rotulo, posicao):
            """Cria um quadrado com o valor centralizado dentro."""
            retangulo = Rectangle(grid_ystep = 2.8, grid_xstep = 2.0)
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
            texto.move_to(RIGHT + posicao)
            texto2 = Text("/", weight=BOLD, font_size=28)
            texto2.move_to(LEFT + posicao)
            return VGroup(retangulo, texto, texto2)
        titulo = Text("Representação de uma lista duplamente ligada", font_size = 40, weight = BOLD)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        no = criar_no("5", LEFT)
        self.play(FadeIn(no))
		#indicadores de cada quadrado
        seta1 = Arrow(
                start=no[0].get_top() + UP + LEFT,
                end=no[0].get_top() + DOWN * 0.5 + LEFT,
                stroke_width=2,
                color=GOLD,
                buff=0.05,
            )
        seta2 = Arrow(
                start=no[0].get_top() + RIGHT + UP,
                end=no[0].get_top() + DOWN * 0.5 + RIGHT,
                stroke_width=2,
                color=GOLD,
                buff=0.05,
            )
        texto1 = Text("Primeiro", weight=BOLD, font_size=20)
        texto1.move_to(seta1.get_top() + LEFT * 0.5 + UP * 0.2)
        texto2 = Text("Quantidade", weight=BOLD, font_size=20)  
        texto2.move_to(seta2.get_top() + RIGHT * 0.5 + UP * 0.2)
        geral = VGroup(no,seta1,seta2,texto1,texto2)
        self.play(Create(geral))
        #texto = Text("A representação de uma lista duplamente ligada pode ser visualizada como uma sequência de nós conectados por ponteiros.",font_size = 20)
        #self.play(Write(texto))
        self.wait(10)
        self.play(FadeOut(titulo,no))