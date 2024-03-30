#Interpolação basica de strings
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal (ABCDEF0123456789)

nome = 'ana'
preco = 10.58
variavel = '%s, o preço e %f' % (nome, preco)
print (variavel)
print (' O hexadecimal de %d é %X' % (15, 15))