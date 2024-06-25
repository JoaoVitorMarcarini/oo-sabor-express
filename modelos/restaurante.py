from modelos.avaliacao import Avaliacao

class Restaurante:
    """Representa um restaurante e suas características."""
    restaurantes = []

    def __init__(self, nome, categoria):
        """Inicializa uma instância de Restaurante.
        
            Pârametro:
            - nome(str): Nome do restaurante.
            - categoria(str): A categoria do restaurante. 
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        """Retorna representação em string do restaurante"""
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        """Lista todos os restaurantes em um string formatada"""
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avalicoes).ljust(25)} | {restaurante.ativo.ljust(25)}')
    
    @property
    def ativo(self):
        """Muda a exibição do atributo ativo, para um simbolo."""
        return '☑' if self._ativo else '☐'
    
    def alternar_status(self):
        """Alterna status do restaurante entre True e False."""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """Recebe a valiaçãi do restaurante se for maior igual a 0 e maior igual a 5 e adiciona a lista 'avaliacao'.
        
           Parâmetros:
           - cliente (str): Nome do cliente.
           -nota (float): nota do cliente para o restaurante (entre 1 e 5).
        """
        avaliacao = Avaliacao(cliente, nota) 
        self._avaliacao.append(avaliacao) if 0 < nota <= 5 else ''

    @property
    def media_avalicoes(self):
        """Faz uma media com as notas de todas as avaliaçôes.
        
            output:
            -media (float): retorna a media das notas do restaurante.
        """
        if not self._avaliacao:
            return '-'
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_notas / quantidade_de_notas, 1)
        return media






