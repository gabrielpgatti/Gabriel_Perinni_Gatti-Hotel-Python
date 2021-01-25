from datetime import date
print('~*'*12)
print('Olá, seja bem-vindo(a)!')
print('~*'*12)
print('Digite o tipo de cliente e a(s) data(s) em que deseja se hospedar \n'
      'Por exemplo: Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)')
n1 = input("Digite aqui: ").upper().split(' ')

days = ["mon","tue","wed","thu","fri","sat","sun"]

dias_de_semana1 = [0,1,2,3,4]
dias_finais_de_semana1 = [5,6]

#Separar a primeira parte da frase (tipo de cliente)
frase_completa = len(n1)
parte_1 = n1[0].upper()
if parte_1 == 'REGULAR:':
        cliente = 1
else:
        cliente = 2

#Encontrar o dia de entrada e saída
primeira_data = n1[1]
segunda_data = n1[-1]
dia1 = int(primeira_data[0:2])
dia2 = int(segunda_data[0:2])

#Encontrar mes de entrada e saída:
primeira_data = n1[1]
segunda_data = n1[-1]
mes1 = primeira_data[2:5]
mes2 = segunda_data[2:5]

def monthToNum1(mes1):

    return {
            'JAN' : 1,
            'FEB' : 2,
            'MAR' : 3,
            'APR' : 4,
            'MAY' : 5,
            'JUN' : 6,
            'JUL' : 7,
            'AUG' : 8,
            'SEP' : 9,
            'OCT' : 10,
            'NOV' : 11,
            'DEC' : 12
    }[mes1]

def monthToNum2(mes2):

    return {
            'JAN' : 1,
            'FEB' : 2,
            'MAR' : 3,
            'APR' : 4,
            'MAY' : 5,
            'JUN' : 6,
            'JUL' : 7,
            'AUG' : 8,
            'SEP' : 9,
            'OCT' : 10,
            'NOV' : 11,
            'DEC' : 12
    }[mes2]

#Encontrar ano de entrada e saída
ano1 = int(primeira_data[5:9])
ano2 = int(segunda_data[5:9])

#Transformar os dados em dias de semana e final de semana
year_entrada = ano1
month_entrada = monthToNum1(mes1)
day_entrada = dia1
data_entrada = date(year=year_entrada, month=month_entrada, day=day_entrada)

year_saida = ano2
month_saida = monthToNum2(mes2)
day_saida = dia2
data_saida = date(year=year_saida, month=month_saida, day=day_saida)
indice_entrada = data_entrada.weekday()
indice_saida = data_saida.weekday()

dias_de_diferenca = int(data_saida.day-data_entrada.day)
dia_entrada_m = day_entrada
dias_de_semana = 0
dias_fds = 0
for i in range(1,dias_de_diferenca+2):
    data_de_entrada_m = date(year=year_entrada, month=month_entrada, day=dia_entrada_m)
    if data_de_entrada_m.weekday() in dias_de_semana1:
        dias_de_semana += 1
    else:
        dias_fds += 1
    dia_entrada_m += 1

# Hotel Lakewood
def hotel_lakewood(dias_de_semana,dias_fds,cliente):
    if cliente == 1:
        diaria_semana = 110
        diaria_fds = 90
        preco = (dias_de_semana*diaria_semana) + (dias_fds*diaria_fds)
    if cliente == 2:
        diaria_semana = 80
        diaria_fds = 80
        preco = (dias_de_semana * diaria_semana) + (dias_fds * diaria_fds)
    return preco


# Hotel Bridgewood
def hotel_bridgewood(dias_de_semana,dias_fds,cliente):
    if cliente == 1:
        diaria_semana = 160
        diaria_fds = 60
        preco = (dias_de_semana*diaria_semana) + (dias_fds*diaria_fds)
    if cliente == 2:
        diaria_semana = 110
        diaria_fds = 50
        preco = (dias_de_semana * diaria_semana) + (dias_fds * diaria_fds)
    return preco


# Hotel Ridgewood
def hotel_ridgewood(dias_de_semana,dias_fds,cliente):
    if cliente == 1:
        diaria_semana = 220
        diaria_fds = 150
        preco = (dias_de_semana*diaria_semana) + (dias_fds*diaria_fds)
    if cliente == 2:
        diaria_semana = 100
        diaria_fds = 40
        preco = (dias_de_semana * diaria_semana) + (dias_fds * diaria_fds)
    return preco

pr1 = int(hotel_lakewood(dias_de_semana,dias_fds,cliente))
pr2 = int(hotel_bridgewood(dias_de_semana,dias_fds,cliente))
pr3 = int(hotel_ridgewood(dias_de_semana,dias_fds,cliente))

#Determinar hotel mais barato
if pr1 == pr2:
    resultado_final = 'Hotel Bridgewood'
if pr2 == pr3:
    resultado_final = 'Hotel Ridgewood'
if pr1 == pr3:
    resultado_final = 'Hotel Ridgewood'

if pr1 < pr2 and pr1 < pr3:
    resultado_final = 'Hotel Lakewood'
if pr2 < pr1 and pr2 < pr3:
    resultado_final = 'Hotel Bridgewood'
if pr3 < pr1 and pr3 < pr2:
    resultado_final = 'Hotel Ridgewood'
print('O', resultado_final, 'é a melhor opção')