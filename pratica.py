print("Hello world")

cancao = 'Roda mundo, roda gigante, roda moinho, roda pião.'

print(cancao.upper())
print(cancao.title())
print(cancao.replace("Roda", "Gira").replace("roda", "gira"))

noticia = 'Selic vai a 2,75% e supera expectativas; ' + \
'é a primeira alta em 6 anos.'

selic = noticia[12:16]
ano = noticia[62:63]

print(f"Valor da Selic: {selic}%")
print(f"Valor do ano: {ano}")

a = False
b = True
x = not a & b

x = True