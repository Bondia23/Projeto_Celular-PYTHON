import sys
inicio = input('Deseja incializar? s/n')
if inicio == 's':
    print('---------Bem-Vindo-------------- ')
    print('Deseja:')
    while True:
      comeco = input('Deseja: cadastrar (1), fazer login (2), desligar (3) ')
      if comeco == '1':
        usuario = input('Digite seu usuario: ')
        senha = input('Digite sua senha: ')
        print('Cadastro efetuado com sucesso! ')
      elif comeco == '2':
        tentativas = 3
        while tentativas > 0:
            usuario1 = input("Digite seu usuario: ")
            senha1 = input('Digite sua senha: ')
            if usuario1 == usuario and senha1 == senha:
                print("Login confirmado")
                sys.exit(0)  
            else:
                tentativas -= 1
                print(f"Tente denovo, voce tem {tentativas} tentativas.")
                if tentativas == 0:
                    print("Voce atingiu o numero maximo de tentativas, o celular agora está bloqueado.")
                    sys.exit(0) 
      elif comeco == '3':
                 print('Desligando')
                 break
      else:
        print('Opção inválida') 
        break
if inicio == 'n':    
    print('Desligando')
         
