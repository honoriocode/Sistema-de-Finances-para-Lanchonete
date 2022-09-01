print('Sistema de Finanças - Chico Lanches')
prod = input('O que você comprou de produtos para lanches hoje? : ')
prod1 = input('O que você comprou de produtos para marmita hoje? : ')
gasto = int(input('Quanto foi gasto com esses produtos? : '))
meta = int(input('Qual vai ser o valor da meta de hoje? : '))

lanches = int(input('Valor de lanches vendidos : '))
marmitas = int(input('Valor de marmitas vendidas: '))
bebidas = int(input('Valor de bebidas vendidas: '))
cupu = int(input('Valor de cupuaçu e açai vendidos : '))

total = lanches + marmitas + bebidas + cupu
lucro = total - gasto
prejuizo = total - gasto


print("Produtos comprados hoje : ", prod, " , ", prod1)
print('Valor gasto na compra de materiais e produtos : ', gasto)
print('Valor total arrecadado hoje : ', total)

if lucro == meta or lucro > meta:
    print('Você teve um lucro hoje no valor de : ', lucro)
    print('A meta era de valor igual ou acima de :', meta)
    print('Meta atingida')
elif lucro == gasto:
    print('Você não teve lucro, nem prejuizo hoje. Valor alcançado: ', lucro)
    print('A meta era de valor igual ou acima de :', meta)
    print('Meta não atingida')
elif lucro < gasto:
    print('Hoje você teve um prejuízo de : ', prejuizo)
    print('Meta não atingida')
