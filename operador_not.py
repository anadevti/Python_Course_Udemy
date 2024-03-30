# Operador logico "not"
# Usado para inverter expressoes
# Not True = False
# Not False = True

senha = input('Senha: ')

#Utilizando o Not
if not senha == '123456':
  print('Acesso liberado')
else:
  print('Acesso negado')
  
#Sem o Not  
if senha == '123456':
  print('Acesso liberado')
else:
  print('Acesso negado')