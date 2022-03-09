'''
⚠️⚠️ DESAFIO DA SEMANA ⚠️⚠️

Caixa eletrônico 

O programa deve pergunta seu nome e número da conta depois disso ele deverá ter 3 opções sacar, depositar,sair 

Opção saca ele te enformar quanto dinheiro vc tem na conta se o valor for = 0 ele tem que informar vc precisa depositar algum valor primeiro 
Se o valor sacado for maior que o valor em contato ele tem que falar saldo para saque insuficiente 


Na opção depósito ele tem que mostrar o valor anterior e o novo valor
'''
print('### Caixa Eletronico ###')

nome = input('Insira seu nome: ')
num_conta = int(input('Insira o numero da sua conta: '))

nome_cli = 'william'
num_cli = 100
saldo = float(1000)

if nome == nome_cli and num_conta == num_cli :
	pag_1 = int(0)
	print('><'*20)
	print('Ola {} o que deseja ?'.format(nome))
	
	while pag_1 != 3:
		print('><'*20)
		print('SAQUE digite 1')
		print('DEPOSITO digite 2')
		print('SAIR digite 3')
		pag_1 = int(input('Digite a funcao: '))
		
		if pag_1 == 1:
			if saldo <= 0:
				print('Saldo insuficiente, realizar um deposito')
			else:	
				print('><'*20)
				print('Funcao SAQUE selecionada')
				print('Seu Saldo {}'.format(saldo))
				saque = float(input('Digite o valor do saque :'))
				if saque > saldo:
					print('Saldo insuficiente para saque')
					print('Seu saldo é de: {}'.format(saldo))
					
				else:
					saldo = saldo - saque
					print('')
					print('Saque realizado com sucesso')
					print('Seu Saldo {}'.format(saldo))
					print('')
				
		if pag_1 == 2:
			print('><'*20)
			print('Funcao DEPOSITO selecionada')
			print('Seu Saldo {}'.format(saldo))
			deposito = float(input('Digite o valor do deposito: '))
			saldo = saldo + deposito
			print('')
			print('Deposito realizado com sucesso')
			print('Seu Saldo {}'.format(saldo))
			print('')
			
		if pag_1 > 3:
			print('Digite a funcao novamente!')
else:
	print('Usuario invalido')			
			
		
	
