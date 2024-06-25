from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_praca.receber_avaliacao('João', 4)
restaurante_praca.receber_avaliacao('Maria', 2)
restaurante_praca.receber_avaliacao('Duda', 5)
retaurante_japabrow = Restaurante('Japa Brow', 'japonesa')
retaurante_japabrow.alternar_status()


def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()