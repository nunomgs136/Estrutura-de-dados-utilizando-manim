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
        raio_no = 0.4
        cor_no = WHITE
        cor_aresta = GOLD

        # Estrutura lógica: valor -> [filho esquerdo, filho direito].
        # None representa um filho inexistente.
        filhos = {
            30: [15, 45],
            15: [7, 22],
            45: [None, None],
            7:  [None, None],
            22: [20, None],
            20: [None, None],
        }

        raiz = 30

        # ---------- Operações na estrutura ----------

        def altura(valor):
            if valor is None:
                return 0

            esquerdo, direito = filhos[valor]
            return 1 + max(altura(esquerdo), altura(direito))

        def fator_balanceamento(valor):
            esquerdo, direito = filhos[valor]
            return altura(esquerdo) - altura(direito)

        def rotacionar_esquerda(x):
            y = filhos[x][1]

            if y is None:
                raise ValueError("A rotação exige um filho direito.")

            beta = filhos[y][0]

            # Transfere a subárvore intermediária.
            filhos[x][1] = beta

            # x passa a ser filho esquerdo de y.
            filhos[y][0] = x

            # Nova raiz da subárvore.
            return y

        def rotacionar_direita(y):
            x = filhos[y][0]

            if x is None:
                raise ValueError("A rotação exige um filho esquerdo.")

            beta = filhos[x][1]

            # Transfere a subárvore intermediária.
            filhos[y][0] = beta

            # y passa a ser filho direito de x.
            filhos[x][1] = y

            # Nova raiz da subárvore.
            return x

        # ---------- Objetos visuais ----------

        def criar_no(valor, posicao):
            circulo = Circle(
                radius=raio_no,
                color=cor_no,
                fill_color=BLACK,
                fill_opacity=1,
            )

            texto = Text(
                str(valor),
                weight=BOLD,
                font_size=28,
            )

            return VGroup(circulo, texto).move_to(posicao)

        def criar_aresta(pai, filho):
            return Line(
                nos[pai][0].get_center(),
                nos[filho][0].get_center(),
                buff=raio_no,
                stroke_width=4,
                color=cor_aresta,
            ).set_z_index(-1)

        def calcular_posicoes(raiz_atual):
            posicoes = {}

            def visitar(valor, x, y, distancia):
                if valor is None:
                    return

                posicoes[valor] = RIGHT * x + UP * y
                esquerdo, direito = filhos[valor]

                visitar(
                    esquerdo,
                    x - distancia,
                    y - 1.15,
                    distancia / 2,
                )
                visitar(
                    direito,
                    x + distancia,
                    y - 1.15,
                    distancia / 2,
                )

            visitar(raiz_atual, 0, 1.7, 2.8)
            return posicoes

        def obter_pais(raiz_atual):
            # Cada nó, exceto a raiz, tem uma aresta de entrada.
            pais = {}

            def visitar(valor):
                if valor is None:
                    return

                for filho in filhos[valor]:
                    if filho is not None:
                        pais[filho] = valor
                        visitar(filho)

            visitar(raiz_atual)
            return pais

        def criar_texto(texto, direcao):
            objeto = Text(texto, font_size=23)

            if objeto.width > config.frame_width - 1:
                objeto.scale_to_fit_width(config.frame_width - 1)

            return objeto.to_edge(direcao, buff=0.35)

        posicoes = calcular_posicoes(raiz)

        nos = {
            valor: criar_no(valor, posicoes[valor])
            for valor in filhos
        }

        pais = obter_pais(raiz)

        # As arestas são identificadas pelo filho de destino.
        arestas = {
            filho: criar_aresta(pai, filho)
            for filho, pai in pais.items()
        }

        titulo = criar_texto(
            "Caso LR: FB(30) = 2 e FB(15) = -1",
            UP,
        )
        legenda = criar_texto(
            "FB = altura(esquerda) - altura(direita)",
            DOWN,
        )

        self.play(FadeIn(titulo), FadeIn(legenda))

        self.play(
            LaggedStart(
                *[FadeIn(no) for no in nos.values()],
                lag_ratio=0.15,
            )
        )
        self.play(*[Create(aresta) for aresta in arestas.values()])
        self.wait(2)

        # ---------- Atualização da animação ----------

        def atualizar_desenho(raiz_atual):
            novos_pais = obter_pais(raiz_atual)
            animacoes = []

            # Uma nova raiz perde sua aresta de entrada.
            for filho in list(arestas):
                if filho not in novos_pais:
                    animacoes.append(FadeOut(arestas.pop(filho)))

            # Redireciona as arestas cujo pai mudou.
            # As demais continuam visíveis.
            for filho, pai in novos_pais.items():
                if filho in arestas:
                    if pais.get(filho) != pai:
                        animacoes.append(
                            Transform(
                                arestas[filho],
                                criar_aresta(pai, filho),
                            )
                        )
                else:
                    arestas[filho] = criar_aresta(pai, filho)
                    animacoes.append(Create(arestas[filho]))

            if animacoes:
                self.play(*animacoes)

            pais.clear()
            pais.update(novos_pais)
            self.wait(0.5)

            # Reorganiza o desenho com as novas referências.
            destinos = calcular_posicoes(raiz_atual)

            movimentos = [
                nos[valor].animate.move_to(posicao)
                for valor, posicao in destinos.items()
            ]

            # Mantém cada aresta ligada aos nós durante o movimento.
            for filho, pai in novos_pais.items():
                movimentos.append(
                    UpdateFromFunc(
                        arestas[filho],
                        lambda linha, p=pai, f=filho: linha.become(
                            criar_aresta(p, f)
                        ),
                    )
                )

            self.play(*movimentos, run_time=2)

        # ---------- 1. Rotação à esquerda em 15 ----------

        self.play(
            Transform(
                titulo,
                criar_texto("1. Rotacao a esquerda em 15", UP),
            ),
            Transform(
                legenda,
                criar_texto(
                    "15.dir = 20; 22.esq = 15; 30.esq = 22",
                    DOWN,
                ),
            ),
            nos[15][0].animate.set_color(YELLOW),
            nos[22][0].animate.set_color(ORANGE),
        )
        self.wait(1)

        # O retorno da rotação substitui o filho esquerdo de 30.
        filhos[30][0] = rotacionar_esquerda(15)

        atualizar_desenho(raiz)
        self.wait(2)

        # ---------- 2. Rotação à direita em 30 ----------

        self.play(
            Transform(
                titulo,
                criar_texto("2. Rotacao a direita em 30", UP),
            ),
            Transform(
                legenda,
                criar_texto(
                    "30.esq = None; 22.dir = 30; raiz = 22",
                    DOWN,
                ),
            ),
            nos[15][0].animate.set_color(WHITE),
            nos[30][0].animate.set_color(YELLOW),
        )
        self.wait(1)

        # Como 30 era a raiz da árvore, atualizamos raiz.
        raiz = rotacionar_direita(raiz)

        atualizar_desenho(raiz)

        self.play(
            nos[30][0].animate.set_color(WHITE),
            nos[22][0].animate.set_color(GREEN),
            Transform(
                titulo,
                criar_texto("Arvore balanceada: raiz = 22", UP),
            ),
            Transform(
                legenda,
                criar_texto(
                    f"FB(22) = {fator_balanceamento(22)}; "
                    f"FB(15) = {fator_balanceamento(15)}; "
                    f"FB(30) = {fator_balanceamento(30)}",
                    DOWN,
                ),
            ),
        )
        self.wait(3)

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
        n = 4
        indice_remocao = 1

        largura_no = 2.4
        altura_no = 1.0
        espaco_horizontal = 3.4
        margem = 0.6

        cor_next = GOLD
        cor_prev = BLUE

        # Ajusta o tamanho de acordo com a quantidade de nós.
        largura_total = (
            n * largura_no
            + (n - 1) * (espaco_horizontal - largura_no)
        )

        escala = min(
            1.0,
            (config.frame_width - 2 * margem) / largura_total,
        )

        espaco_horizontal *= escala

        def criar_no(valor, posicao):
            retangulo = Rectangle(
                width=largura_no,
                height=altura_no,
                color=WHITE,
            )

            # Campos: prev | valor | next
            divisao_esquerda = Line(
                [-0.6, -altura_no / 2, 0],
                [-0.6, altura_no / 2, 0],
            )
            divisao_direita = Line(
                [0.6, -altura_no / 2, 0],
                [0.6, altura_no / 2, 0],
            )

            texto = Text(str(valor), font_size=28, weight=BOLD)

            texto_prev = Text(
                "prev", font_size=12, color=cor_prev
            ).move_to(LEFT * 0.9)

            texto_next = Text(
                "next", font_size=12, color=cor_next
            ).move_to(RIGHT * 0.9)

            return VGroup(
                retangulo,
                divisao_esquerda,
                divisao_direita,
                texto,
                texto_prev,
                texto_next,
            ).scale(escala).move_to(posicao)

        def criar_seta(origem, destino, sentido, curva=False):
            afastamento = 0.16 * escala
            folga = 0.04 * escala

            if sentido == "next":
                inicio = (
                    origem[0].get_right()
                    + UP * afastamento
                    + RIGHT * folga
                )
                fim = (
                    destino[0].get_left()
                    + UP * afastamento
                    + LEFT * folga
                )
                cor = cor_next
            else:
                inicio = (
                    origem[0].get_left()
                    + DOWN * afastamento
                    + LEFT * folga
                )
                fim = (
                    destino[0].get_right()
                    + DOWN * afastamento
                    + RIGHT * folga
                )
                cor = cor_prev

            if curva:
                # next passa acima; prev passa abaixo.
                return CurvedArrow(
                    inicio,
                    fim,
                    angle=-PI / 3,
                    color=cor,
                    stroke_width=3,
                    tip_length=0.15 * escala,
                )

            return Arrow(
                inicio,
                fim,
                buff=0,
                color=cor,
                stroke_width=3,
                tip_length=0.15 * escala,
            )

        def criar_ligacao(esquerdo, direito):
            return VGroup(
                criar_seta(esquerdo, direito, "next"),
                criar_seta(direito, esquerdo, "prev"),
            )

        def criar_legenda(texto):
            legenda = Text(texto, font_size=25)

            if legenda.width > config.frame_width - 1:
                legenda.scale_to_fit_width(config.frame_width - 1)

            return legenda.to_edge(UP, buff=0.4)

        def remover_intermediario(nos, setas, indice):
            if not 0 < indice < len(nos) - 1:
                raise ValueError(
                    "Esta função remove apenas nós intermediários."
                )

            anterior = nos[indice - 1]
            removido = nos[indice]
            proximo = nos[indice + 1]

            # Cada ligação contém [next, prev].
            ligacao_esquerda = setas[indice - 1]
            ligacao_direita = setas[indice]

            # Ponteiros dos vizinhos que serão redirecionados.
            next_anterior = ligacao_esquerda[0]
            prev_proximo = ligacao_direita[1]

            # Ponteiros pertencentes ao nó removido.
            prev_removido = ligacao_esquerda[1]
            next_removido = ligacao_direita[0]

            legenda = criar_legenda(
                "Identificar anterior, removido e proximo"
            )

            self.play(
                FadeIn(legenda),
                removido.animate.set_color(RED),
            )
            self.wait(1)

            # 1. anterior.next = proximo
            self.play(
                Transform(
                    legenda,
                    criar_legenda("anterior.next = proximo"),
                ),
                Transform(
                    next_anterior,
                    criar_seta(
                        anterior, proximo, "next", curva=True
                    ),
                ),
            )
            self.wait(1)

            # 2. proximo.prev = anterior
            self.play(
                Transform(
                    legenda,
                    criar_legenda("proximo.prev = anterior"),
                ),
                Transform(
                    prev_proximo,
                    criar_seta(
                        proximo, anterior, "prev", curva=True
                    ),
                ),
            )
            self.wait(1)

            # 3. Os vizinhos já contornam o nó.
            # Agora ele e seus próprios ponteiros podem desaparecer.
            self.play(
                Transform(
                    legenda,
                    criar_legenda("Remover o no desconectado"),
                ),
            )

            self.play(
                FadeOut(removido),
                FadeOut(prev_removido),
                FadeOut(next_removido),
            )

            nos.pop(indice)

            # Reaproveita as duas setas redirecionadas.
            nova_ligacao = VGroup(next_anterior, prev_proximo)

            # Substitui as duas ligações antigas por uma.
            setas[indice - 1:indice + 1] = [nova_ligacao]

            self.wait(1)

            # 4. Organização visual, após concluir a remoção.
            self.play(
                Transform(
                    legenda,
                    criar_legenda("Reorganizar o desenho"),
                ),
            )

            largura_centros = (
                len(nos) - 1
            ) * espaco_horizontal

            destinos = [
                RIGHT * (
                    i * espaco_horizontal - largura_centros / 2
                )
                for i in range(len(nos))
            ]

            # Cópias nas posições finais servem de referência
            # para os destinos das setas.
            nos_destino = [
                no.copy().move_to(posicao)
                for no, posicao in zip(nos, destinos)
            ]

            animacoes = [
                no.animate.move_to(posicao)
                for no, posicao in zip(nos, destinos)
            ]

            # As ligações continuam visíveis durante o movimento.
            for i, ligacao in enumerate(setas):
                animacoes.append(
                    Transform(
                        ligacao,
                        criar_ligacao(
                            nos_destino[i],
                            nos_destino[i + 1],
                        ),
                    )
                )

            self.play(*animacoes, run_time=1.5)
            self.play(FadeOut(legenda))
            self.wait(2)

        # Criação da lista.
        largura_centros = (n - 1) * espaco_horizontal

        posicoes = [
            RIGHT * (
                i * espaco_horizontal - largura_centros / 2
            )
            for i in range(n)
        ]

        nos = [
            criar_no(i, posicoes[i])
            for i in range(n)
        ]

        setas = [
            criar_ligacao(nos[i], nos[i + 1])
            for i in range(n - 1)
        ]

        self.play(FadeIn(nos[0]))

        for i in range(n - 1):
            self.play(
                FadeIn(nos[i + 1]),
                Create(setas[i]),
            )

        self.wait(1)
        remover_intermediario(nos, setas, indice_remocao)

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

class ExemploSICFEI(Scene):
     def construct(self):
        n = 4
        indice_remocao = 1

        largura_no = 2.4
        altura_no = 1.0
        espaco_horizontal = 3.4
        margem = 0.6

        cor_next = GOLD
        cor_prev = BLUE

        # Ajusta o tamanho de acordo com a quantidade de nós.
        largura_total = (
            n * largura_no
            + (n - 1) * (espaco_horizontal - largura_no)
        )

        escala = min(
            1.0,
            (config.frame_width - 2 * margem) / largura_total,
        )

        espaco_horizontal *= escala

        def criar_no(valor, posicao):
            retangulo = Rectangle(
                width=largura_no,
                height=altura_no,
                color=WHITE,
            )

            # Campos: prev | valor | next
            divisao_esquerda = Line(
                [-0.6, -altura_no / 2, 0],
                [-0.6, altura_no / 2, 0],
            )
            divisao_direita = Line(
                [0.6, -altura_no / 2, 0],
                [0.6, altura_no / 2, 0],
            )

            texto = Text(str(valor), font_size=28, weight=BOLD)

            texto_prev = Text(
                "prev", font_size=12, color=cor_prev
            ).move_to(LEFT * 0.9)

            texto_next = Text(
                "next", font_size=12, color=cor_next
            ).move_to(RIGHT * 0.9)

            return VGroup(
                retangulo,
                divisao_esquerda,
                divisao_direita,
                texto,
                texto_prev,
                texto_next,
            ).scale(escala).move_to(posicao)

        def criar_seta(origem, destino, sentido, curva=False):
            afastamento = 0.16 * escala
            folga = 0.04 * escala

            if sentido == "next":
                inicio = (
                    origem[0].get_right()
                    + UP * afastamento
                    + RIGHT * folga
                )
                fim = (
                    destino[0].get_left()
                    + UP * afastamento
                    + LEFT * folga
                )
                cor = cor_next
            else:
                inicio = (
                    origem[0].get_left()
                    + DOWN * afastamento
                    + LEFT * folga
                )
                fim = (
                    destino[0].get_right()
                    + DOWN * afastamento
                    + RIGHT * folga
                )
                cor = cor_prev

            if curva:
                # next passa acima; prev passa abaixo.
                return CurvedArrow(
                    inicio,
                    fim,
                    angle=-PI / 3,
                    color=cor,
                    stroke_width=3,
                    tip_length=0.15 * escala,
                )

            return Arrow(
                inicio,
                fim,
                buff=0,
                color=cor,
                stroke_width=3,
                tip_length=0.15 * escala,
            )

        def criar_ligacao(esquerdo, direito):
            return VGroup(
                criar_seta(esquerdo, direito, "next"),
                criar_seta(direito, esquerdo, "prev"),
            )

        def criar_legenda(texto):
            legenda = Text(texto, font_size=25)

            if legenda.width > config.frame_width - 1:
                legenda.scale_to_fit_width(config.frame_width - 1)

            return legenda.to_edge(UP, buff=0.4)

        def remover_intermediario(nos, setas, indice):
            if not 0 < indice < len(nos) - 1:
                raise ValueError(
                    "Esta função remove apenas nós intermediários."
                )

            anterior = nos[indice - 1]
            removido = nos[indice]
            proximo = nos[indice + 1]

            # Cada ligação contém [next, prev].
            ligacao_esquerda = setas[indice - 1]
            ligacao_direita = setas[indice]

            # Ponteiros dos vizinhos que serão redirecionados.
            next_anterior = ligacao_esquerda[0]
            prev_proximo = ligacao_direita[1]

            # Ponteiros pertencentes ao nó removido.
            prev_removido = ligacao_esquerda[1]
            next_removido = ligacao_direita[0]

            legenda = criar_legenda(
                "Identificar anterior, removido e proximo"
            )

            self.play(
                FadeIn(legenda),
                removido.animate.set_color(RED),
            )
            self.wait(1)

            # 1. anterior.next = proximo
            self.play(
                Transform(
                    legenda,
                    criar_legenda("anterior.next = proximo"),
                ),
                Transform(
                    next_anterior,
                    criar_seta(
                        anterior, proximo, "next", curva=True
                    ),
                ),
            )
            self.wait(1)

            # 2. proximo.prev = anterior
            self.play(
                Transform(
                    legenda,
                    criar_legenda("proximo.prev = anterior"),
                ),
                Transform(
                    prev_proximo,
                    criar_seta(
                        proximo, anterior, "prev", curva=True
                    ),
                ),
            )
            self.wait(1)

            # 3. Os vizinhos já contornam o nó.
            # Agora ele e seus próprios ponteiros podem desaparecer.
            self.play(
                Transform(
                    legenda,
                    criar_legenda("Remover o no desconectado"),
                ),
            )

            self.play(
                FadeOut(removido),
                FadeOut(prev_removido),
                FadeOut(next_removido),
            )

            nos.pop(indice)

            # Reaproveita as duas setas redirecionadas.
            nova_ligacao = VGroup(next_anterior, prev_proximo)

            # Substitui as duas ligações antigas por uma.
            setas[indice - 1:indice + 1] = [nova_ligacao]

            self.wait(1)

            # 4. Organização visual, após concluir a remoção.
            self.play(
                Transform(
                    legenda,
                    criar_legenda("Reorganizar o desenho"),
                ),
            )

            largura_centros = (
                len(nos) - 1
            ) * espaco_horizontal

            destinos = [
                RIGHT * (
                    i * espaco_horizontal - largura_centros / 2
                )
                for i in range(len(nos))
            ]

            # Cópias nas posições finais servem de referência
            # para os destinos das setas.
            nos_destino = [
                no.copy().move_to(posicao)
                for no, posicao in zip(nos, destinos)
            ]

            animacoes = [
                no.animate.move_to(posicao)
                for no, posicao in zip(nos, destinos)
            ]

            # As ligações continuam visíveis durante o movimento.
            for i, ligacao in enumerate(setas):
                animacoes.append(
                    Transform(
                        ligacao,
                        criar_ligacao(
                            nos_destino[i],
                            nos_destino[i + 1],
                        ),
                    )
                )

            self.play(*animacoes, run_time=1.5)
            self.play(FadeOut(legenda))
            self.wait(2)

        # Criação da lista.
        largura_centros = (n - 1) * espaco_horizontal

        posicoes = [
            RIGHT * (
                i * espaco_horizontal - largura_centros / 2
            )
            for i in range(n)
        ]

        nos = [
            criar_no(i, posicoes[i])
            for i in range(n)
        ]

        setas = [
            criar_ligacao(nos[i], nos[i + 1])
            for i in range(n - 1)
        ]

        self.play(FadeIn(nos[0]))

        for i in range(n - 1):
            self.play(
                FadeIn(nos[i + 1]),
                Create(setas[i]),
            )

        self.wait(1)
        remover_intermediario(nos, setas, indice_remocao)
        raio_no = 0.4
        cor_no = WHITE
        cor_aresta = GOLD

        # Estrutura lógica: valor -> [filho esquerdo, filho direito].
        # None representa um filho inexistente.
        filhos = {
            30: [15, 45],
            15: [7, 22],
            45: [None, None],
            7:  [None, None],
            22: [20, None],
            20: [None, None],
        }

        raiz = 30

        # ---------- Operações na estrutura ----------

        def altura(valor):
            if valor is None:
                return 0

            esquerdo, direito = filhos[valor]
            return 1 + max(altura(esquerdo), altura(direito))

        def fator_balanceamento(valor):
            esquerdo, direito = filhos[valor]
            return altura(esquerdo) - altura(direito)

        def rotacionar_esquerda(x):
            y = filhos[x][1]

            if y is None:
                raise ValueError("A rotação exige um filho direito.")

            beta = filhos[y][0]

            # Transfere a subárvore intermediária.
            filhos[x][1] = beta

            # x passa a ser filho esquerdo de y.
            filhos[y][0] = x

            # Nova raiz da subárvore.
            return y

        def rotacionar_direita(y):
            x = filhos[y][0]

            if x is None:
                raise ValueError("A rotação exige um filho esquerdo.")

            beta = filhos[x][1]

            # Transfere a subárvore intermediária.
            filhos[y][0] = beta

            # y passa a ser filho direito de x.
            filhos[x][1] = y

            # Nova raiz da subárvore.
            return x

        # ---------- Objetos visuais ----------

        def criar_no(valor, posicao):
            circulo = Circle(
                radius=raio_no,
                color=cor_no,
                fill_color=BLACK,
                fill_opacity=1,
            )

            texto = Text(
                str(valor),
                weight=BOLD,
                font_size=28,
            )

            return VGroup(circulo, texto).move_to(posicao)

        def criar_aresta(pai, filho):
            return Line(
                nos[pai][0].get_center(),
                nos[filho][0].get_center(),
                buff=raio_no,
                stroke_width=4,
                color=cor_aresta,
            ).set_z_index(-1)

        def calcular_posicoes(raiz_atual):
            posicoes = {}

            def visitar(valor, x, y, distancia):
                if valor is None:
                    return

                posicoes[valor] = RIGHT * x + UP * y
                esquerdo, direito = filhos[valor]

                visitar(
                    esquerdo,
                    x - distancia,
                    y - 1.15,
                    distancia / 2,
                )
                visitar(
                    direito,
                    x + distancia,
                    y - 1.15,
                    distancia / 2,
                )

            visitar(raiz_atual, 0, 1.7, 2.8)
            return posicoes

        def obter_pais(raiz_atual):
            # Cada nó, exceto a raiz, tem uma aresta de entrada.
            pais = {}

            def visitar(valor):
                if valor is None:
                    return

                for filho in filhos[valor]:
                    if filho is not None:
                        pais[filho] = valor
                        visitar(filho)

            visitar(raiz_atual)
            return pais

        def criar_texto(texto, direcao):
            objeto = Text(texto, font_size=23)

            if objeto.width > config.frame_width - 1:
                objeto.scale_to_fit_width(config.frame_width - 1)

            return objeto.to_edge(direcao, buff=0.35)

        posicoes = calcular_posicoes(raiz)

        nos = {
            valor: criar_no(valor, posicoes[valor])
            for valor in filhos
        }

        pais = obter_pais(raiz)

        # As arestas são identificadas pelo filho de destino.
        arestas = {
            filho: criar_aresta(pai, filho)
            for filho, pai in pais.items()
        }

        titulo = criar_texto(
            "Caso LR: FB(30) = 2 e FB(15) = -1",
            UP,
        )
        legenda = criar_texto(
            "FB = altura(esquerda) - altura(direita)",
            DOWN,
        )

        self.play(FadeIn(titulo), FadeIn(legenda))

        self.play(
            LaggedStart(
                *[FadeIn(no) for no in nos.values()],
                lag_ratio=0.15,
            )
        )
        self.play(*[Create(aresta) for aresta in arestas.values()])
        self.wait(2)

        # ---------- Atualização da animação ----------

        def atualizar_desenho(raiz_atual):
            novos_pais = obter_pais(raiz_atual)
            animacoes = []

            # Uma nova raiz perde sua aresta de entrada.
            for filho in list(arestas):
                if filho not in novos_pais:
                    animacoes.append(FadeOut(arestas.pop(filho)))

            # Redireciona as arestas cujo pai mudou.
            # As demais continuam visíveis.
            for filho, pai in novos_pais.items():
                if filho in arestas:
                    if pais.get(filho) != pai:
                        animacoes.append(
                            Transform(
                                arestas[filho],
                                criar_aresta(pai, filho),
                            )
                        )
                else:
                    arestas[filho] = criar_aresta(pai, filho)
                    animacoes.append(Create(arestas[filho]))

            if animacoes:
                self.play(*animacoes)

            pais.clear()
            pais.update(novos_pais)
            self.wait(0.5)

            # Reorganiza o desenho com as novas referências.
            destinos = calcular_posicoes(raiz_atual)

            movimentos = [
                nos[valor].animate.move_to(posicao)
                for valor, posicao in destinos.items()
            ]

            # Mantém cada aresta ligada aos nós durante o movimento.
            for filho, pai in novos_pais.items():
                movimentos.append(
                    UpdateFromFunc(
                        arestas[filho],
                        lambda linha, p=pai, f=filho: linha.become(
                            criar_aresta(p, f)
                        ),
                    )
                )

            self.play(*movimentos, run_time=2)

        # ---------- 1. Rotação à esquerda em 15 ----------

        self.play(
            Transform(
                titulo,
                criar_texto("1. Rotacao a esquerda em 15", UP),
            ),
            Transform(
                legenda,
                criar_texto(
                    "15.dir = 20; 22.esq = 15; 30.esq = 22",
                    DOWN,
                ),
            ),
            nos[15][0].animate.set_color(YELLOW),
            nos[22][0].animate.set_color(ORANGE),
        )
        self.wait(1)

        # O retorno da rotação substitui o filho esquerdo de 30.
        filhos[30][0] = rotacionar_esquerda(15)

        atualizar_desenho(raiz)
        self.wait(2)

        # ---------- 2. Rotação à direita em 30 ----------

        self.play(
            Transform(
                titulo,
                criar_texto("2. Rotacao a direita em 30", UP),
            ),
            Transform(
                legenda,
                criar_texto(
                    "30.esq = None; 22.dir = 30; raiz = 22",
                    DOWN,
                ),
            ),
            nos[15][0].animate.set_color(WHITE),
            nos[30][0].animate.set_color(YELLOW),
        )
        self.wait(1)

        # Como 30 era a raiz da árvore, atualizamos raiz.
        raiz = rotacionar_direita(raiz)

        atualizar_desenho(raiz)

        self.play(
            nos[30][0].animate.set_color(WHITE),
            nos[22][0].animate.set_color(GREEN),
            Transform(
                titulo,
                criar_texto("Arvore balanceada: raiz = 22", UP),
            ),
            Transform(
                legenda,
                criar_texto(
                    f"FB(22) = {fator_balanceamento(22)}; "
                    f"FB(15) = {fator_balanceamento(15)}; "
                    f"FB(30) = {fator_balanceamento(30)}",
                    DOWN,
                ),
            ),
        )
        self.wait(3)





class ExemploSICFEI2(Scene):
    def construct(self):
        # Uma única Scene gera um único vídeo.
        self.demonstrar_lista(n=4, indice=1)
        self.play(*[FadeOut(objeto) for objeto in list(self.mobjects)])
        self.wait(0.5)
        self.demonstrar_avl()

    def texto_na_borda(self, texto, direcao, tamanho=25):
        objeto = Text(texto, font_size=tamanho)
        if objeto.width > config.frame_width - 1:
            objeto.scale_to_fit_width(config.frame_width - 1)
        return objeto.to_edge(direcao, buff=0.35)

    def demonstrar_lista(self, n=4, indice=1):
        # A demonstração trata a remoção de um nó intermediário.
        if not 0 < indice < n - 1:
            raise ValueError("Escolha um nó intermediário para remover.")

        largura_no = 2.4
        altura_no = 1.0
        distancia_base = 3.4
        largura_total = largura_no + (n - 1) * distancia_base
        escala = min(1.0, (config.frame_width - 1.2) / largura_total)
        distancia = distancia_base * escala

        titulo = self.texto_na_borda("Lista duplamente ligada", UP)
        legenda = self.texto_na_borda(
            "Dourado: next | Azul: prev", DOWN
        )

        def criar_no(valor, posicao):
            caixa = Rectangle(width=largura_no, height=altura_no)
            divisoes = VGroup(*[
                Line([x, -0.5, 0], [x, 0.5, 0])
                for x in (-0.6, 0.6)
            ])
            valor_texto = Text(str(valor), font_size=28, weight=BOLD)
            prev = Text("prev", font_size=12, color=BLUE).shift(LEFT * 0.9)
            next_ = Text("next", font_size=12, color=GOLD).shift(RIGHT * 0.9)
            return VGroup(caixa, divisoes, valor_texto, prev, next_).scale(
                escala
            ).move_to(posicao)

        def criar_seta(origem, destino, sentido, curva=False):
            afastamento = 0.16 * escala
            folga = 0.04 * escala
            if sentido == "next":
                inicio = origem[0].get_right() + UP * afastamento + RIGHT * folga
                fim = destino[0].get_left() + UP * afastamento + LEFT * folga
                cor = GOLD
            else:
                inicio = origem[0].get_left() + DOWN * afastamento + LEFT * folga
                fim = destino[0].get_right() + DOWN * afastamento + RIGHT * folga
                cor = BLUE
            estilo = dict(color=cor, stroke_width=3, tip_length=0.15 * escala)
            if curva:
                return CurvedArrow(inicio, fim, angle=-PI / 3, **estilo)
            return Arrow(inicio, fim, buff=0, **estilo)

        def criar_ligacao(esquerdo, direito):
            return VGroup(
                criar_seta(esquerdo, direito, "next"),
                criar_seta(direito, esquerdo, "prev"),
            )

        def posicoes(quantidade):
            return [
                RIGHT * ((i - (quantidade - 1) / 2) * distancia)
                for i in range(quantidade)
            ]

        nos = [criar_no(i, p) for i, p in enumerate(posicoes(n))]
        setas = [criar_ligacao(nos[i], nos[i + 1]) for i in range(n - 1)]

        # Relações lógicas independentes das posições no desenho.
        ponteiros = {
            i: {"prev": i - 1 if i > 0 else None,
                "next": i + 1 if i < n - 1 else None}
            for i in range(n)
        }

        self.play(FadeIn(titulo), FadeIn(legenda), FadeIn(nos[0]))
        for i in range(n - 1):
            self.play(Create(setas[i]), FadeIn(nos[i + 1]))
        self.wait(1)

        anterior_valor = ponteiros[indice]["prev"]
        proximo_valor = ponteiros[indice]["next"]
        anterior, removido, proximo = nos[indice - 1:indice + 2]
        next_anterior, prev_removido = setas[indice - 1]
        next_removido, prev_proximo = setas[indice]

        self.play(
            removido.animate.set_color(RED),
            Transform(legenda, self.texto_na_borda(
                "Identificar anterior, removido e proximo", DOWN
            )),
        )
        self.wait(1)

        # Primeiro redireciona o ponteiro next do vizinho anterior.
        ponteiros[anterior_valor]["next"] = proximo_valor
        self.play(
            Transform(legenda, self.texto_na_borda(
                "anterior.next = proximo", DOWN
            )),
            Transform(next_anterior, criar_seta(
                anterior, proximo, "next", curva=True
            )),
        )
        self.wait(1)

        # Depois redireciona o ponteiro prev do próximo vizinho.
        ponteiros[proximo_valor]["prev"] = anterior_valor
        self.play(
            Transform(legenda, self.texto_na_borda(
                "proximo.prev = anterior", DOWN
            )),
            Transform(prev_proximo, criar_seta(
                proximo, anterior, "prev", curva=True
            )),
        )
        self.wait(1)

        self.play(Transform(legenda, self.texto_na_borda(
            "Remover o no desconectado", DOWN
        )))
        self.play(
            FadeOut(removido), FadeOut(prev_removido), FadeOut(next_removido)
        )
        del ponteiros[indice]
        nos.pop(indice)
        setas[indice - 1:indice + 1] = [VGroup(next_anterior, prev_proximo)]
        self.wait(1)

        self.play(Transform(legenda, self.texto_na_borda(
            "Reorganizar o desenho", DOWN
        )))
        destinos = posicoes(len(nos))
        referencias = [no.copy().move_to(p) for no, p in zip(nos, destinos)]
        animacoes = [no.animate.move_to(p) for no, p in zip(nos, destinos)]
        animacoes.extend(
            Transform(ligacao, criar_ligacao(referencias[i], referencias[i + 1]))
            for i, ligacao in enumerate(setas)
        )
        self.play(*animacoes, run_time=1.5)
        self.play(Transform(legenda, self.texto_na_borda(
            "Os vizinhos agora apontam um para o outro", DOWN
        )))
        self.wait(2)

    def demonstrar_avl(self):
        raio_no = 0.4

        # valor -> [filho esquerdo, filho direito]
        filhos = {
            30: [15, 45],
            15: [7, 22],
            45: [None, None],
            7: [None, None],
            22: [20, None],
            20: [None, None],
        }
        raiz = 30

        def altura(valor):
            if valor is None:
                return 0
            esquerdo, direito = filhos[valor]
            return 1 + max(altura(esquerdo), altura(direito))

        def fator_balanceamento(valor):
            esquerdo, direito = filhos[valor]
            return altura(esquerdo) - altura(direito)

        def rotacionar_esquerda(x):
            y = filhos[x][1]
            if y is None:
                raise ValueError("A rotação exige um filho direito.")
            beta = filhos[y][0]
            filhos[x][1] = beta
            filhos[y][0] = x
            return y

        def rotacionar_direita(y):
            x = filhos[y][0]
            if x is None:
                raise ValueError("A rotação exige um filho esquerdo.")
            beta = filhos[x][1]
            filhos[y][0] = beta
            filhos[x][1] = y
            return x

        def calcular_posicoes(raiz_atual):
            resultado = {}

            def visitar(valor, x, y, distancia):
                if valor is None:
                    return
                resultado[valor] = RIGHT * x + UP * y
                esquerdo, direito = filhos[valor]
                visitar(esquerdo, x - distancia, y - 1.15, distancia / 2)
                visitar(direito, x + distancia, y - 1.15, distancia / 2)

            visitar(raiz_atual, 0, 1.7, 2.8)
            return resultado

        def obter_pais(raiz_atual):
            resultado = {}

            def visitar(valor):
                for filho in filhos[valor]:
                    if filho is not None:
                        resultado[filho] = valor
                        visitar(filho)

            visitar(raiz_atual)
            return resultado

        def criar_no(valor, posicao):
            circulo = Circle(
                radius=raio_no, color=WHITE,
                fill_color=BLACK, fill_opacity=1,
            )
            texto = Text(str(valor), weight=BOLD, font_size=28)
            return VGroup(circulo, texto).move_to(posicao)

        def criar_aresta(pai, filho):
            return Line(
                nos[pai][0].get_center(), nos[filho][0].get_center(),
                buff=raio_no, stroke_width=4, color=GOLD,
            ).set_z_index(-1)

        posicoes = calcular_posicoes(raiz)
        nos = {valor: criar_no(valor, posicoes[valor]) for valor in filhos}
        pais = obter_pais(raiz)
        arestas = {
            filho: criar_aresta(pai, filho) for filho, pai in pais.items()
        }
        titulo = self.texto_na_borda("Arvore AVL: caso LR", UP)
        legenda = self.texto_na_borda(
            "FB = altura(esquerda) - altura(direita)", DOWN
        )
        self.play(FadeIn(titulo), FadeIn(legenda))
        self.play(LaggedStart(
            *[FadeIn(no) for no in nos.values()], lag_ratio=0.15
        ))
        self.play(*[Create(aresta) for aresta in arestas.values()])
        self.play(Transform(legenda, self.texto_na_borda(
            "FB(30) = 2; FB(15) = -1: rotacao dupla LR", DOWN
        )))
        self.wait(2)

        def atualizar_desenho(raiz_atual):
            novos_pais = obter_pais(raiz_atual)
            animacoes = []
            for filho in list(arestas):
                if filho not in novos_pais:
                    animacoes.append(FadeOut(arestas.pop(filho)))
            for filho, pai in novos_pais.items():
                if filho in arestas:
                    if pais.get(filho) != pai:
                        animacoes.append(Transform(
                            arestas[filho], criar_aresta(pai, filho)
                        ))
                else:
                    arestas[filho] = criar_aresta(pai, filho)
                    animacoes.append(Create(arestas[filho]))
            if animacoes:
                self.play(*animacoes)
            pais.clear()
            pais.update(novos_pais)
            self.wait(0.5)

            destinos = calcular_posicoes(raiz_atual)
            movimentos = [
                nos[valor].animate.move_to(posicao)
                for valor, posicao in destinos.items()
            ]
            for filho, pai in novos_pais.items():
                movimentos.append(UpdateFromFunc(
                    arestas[filho],
                    lambda linha, p=pai, f=filho: linha.become(criar_aresta(p, f)),
                ))
            self.play(*movimentos, run_time=2)

        self.play(
            Transform(titulo, self.texto_na_borda(
                "1. Rotacao a esquerda em 15", UP
            )),
            Transform(legenda, self.texto_na_borda(
                "15.dir = 20; 22.esq = 15; 30.esq = 22", DOWN
            )),
            nos[15][0].animate.set_color(YELLOW),
            nos[22][0].animate.set_color(ORANGE),
        )
        self.wait(1)
        filhos[30][0] = rotacionar_esquerda(15)
        atualizar_desenho(raiz)
        self.wait(2)

        self.play(
            Transform(titulo, self.texto_na_borda(
                "2. Rotacao a direita em 30", UP
            )),
            Transform(legenda, self.texto_na_borda(
                "30.esq = None; 22.dir = 30; raiz = 22", DOWN
            )),
            nos[15][0].animate.set_color(WHITE),
            nos[30][0].animate.set_color(YELLOW),
        )
        self.wait(1)
        raiz = rotacionar_direita(raiz)
        atualizar_desenho(raiz)
        self.play(
            nos[30][0].animate.set_color(WHITE),
            nos[22][0].animate.set_color(GREEN),
            Transform(titulo, self.texto_na_borda(
                "Arvore balanceada: raiz = 22", UP
            )),
            Transform(legenda, self.texto_na_borda(
                f"FB(22) = {fator_balanceamento(22)}; "
                f"FB(15) = {fator_balanceamento(15)}; "
                f"FB(30) = {fator_balanceamento(30)}", DOWN
            )),
        )
        self.wait(3)
