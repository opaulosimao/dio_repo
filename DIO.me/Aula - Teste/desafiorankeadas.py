heroi = 'Paulo'
def calculadora_de_partidas_rankeadas(vitorias, derrotas):
    saldo_de_partidas = vitorias - derrotas

    if saldo_de_partidas < 10:
        nivel = 'Ferro'
    elif 11 <= saldo_de_partidas <= 20:
        nivel = 'Bronze'
    elif 21 <= saldo_de_partidas <= 50:
        nivel = 'Prata'
    elif 51 <= saldo_de_partidas <= 80:
        nivel = 'Ouro'
    elif 81 <= saldo_de_partidas <= 90:
        nivel = 'Diamante'
    elif 91 <= saldo_de_partidas <= 100:
        nivel = 'Lendário'
    else:
        nivel = 'Radiante'

    return saldo_de_partidas, nivel

while True:
    vitoria = int(input('Quantidade de vitorias: '))
    derrotas = int(input('Quantidade de derrotas: '))

    saldo, nivel = calculadora_de_partidas_rankeadas(vitoria, derrotas)

    print(f'O herói {heroi} tem um saldo de {saldo} está no nível de {nivel}')