import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}]

def exibir_nome_do_programa():
      '''Essa função apenas exibe o nome do programa, quando chamada'''


      print("""
╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮
┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━━╯
┃╰━━┳━━┫╰━┳━━┳━╮┃╰━━┳╮╭┳━━┳━┳━━┳━━┳━━╮
╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃╭━━┻╋╋┫╭╮┃╭┫┃━┫━━┫━━┫
┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━━┳╋╋┫╰╯┃┃┃┃━╋━━┣━━┃
╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┫╭━┻╯╰━━┻━━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯

""")

def exibir_opcoes():
      '''Essa função dá ao usuário as opções disponíveis a serem escolhidas'''
      print('1. Cadastrar restaurante')
      print('2. Listar restaurante')
      print('3. Alternar estado do restaurante')
      print('4. Sair')

def finalizando_app():
      '''Essa função limpa a tela e finaliza o app'''

      os.system('cls')
      exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
      '''Essa função é anterior ao retorno ao menu principal'''

      input('\nDigite uma tecla para voltar ao menu principal')
      main()

def opcao_invalida():
      '''Essa função imprimir um texto alertando que a opção que o usuário escolheu não existe'''

      print('Opção inválida!')
      voltar_ao_menu_principal()

def exibir_subtitulo(texto):
      '''Essa função exibe os substitulos da opções depois de serem escolhidas'''

      os.system('cls')
      linha = '*' * (len(texto))
      print(linha)
      print(texto)
      print(linha)
      print()

def cadastrar_novo_restaurante():
      '''Essa função é responsável por cadastrar um novo restaurante
      
      Inputs:
      -Nome do restaurante
      -Categoria do restaurante

      Outputs:
      - Adiciona um novo restaurante à lista de restaurantes
      
      '''
      exibir_subtitulo('Cadastro de novos restaurantes')
      nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
      categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
      dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
      restaurantes.append(dados_do_restaurante)
      print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

      voltar_ao_menu_principal()

def listar_restaurantes():
      '''Essa função lista os restaurantes cadastrados
      
      Outputs:
      - Exibe o nome, categoria e se o restaurante está ativo ou não
      '''
      exibir_subtitulo('Listando os restaurantes')

      print(f'{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | {'Status'}')
      for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

      voltar_ao_menu_principal()

def alternar_estado_restaurante():
      '''Essa função altera os estados entre ativo e inativo
      
      Outputs:
      - Além de mudar o status, ela imprime uma mensagem confirmando se o restaurante foi ativado ou desativado
      '''
      exibir_subtitulo('Alterando estado do restaurante')
      nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
      restaurante_encontrado = False

      for restaurante in restaurantes:
            if nome_restaurante == restaurante['nome']:
                  restaurante_encontrado = True
                  restaurante['ativo'] = not restaurante['ativo']
                  mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
                  print(mensagem)

      if not restaurante_encontrado:
            print('O restaurante não foi encontrado.')

      voltar_ao_menu_principal()

def escolher_opcao():
      '''Essa função é onde o usuário irá inserir o número da opção escolhida
      
      Inputs:
      - Número da opção escolhida

      Outputs:
      - Leva à função da opção escolhida
      
      '''
      try:
            opcao_escolhida = int(input('Escolha uma opcão: '))

            if opcao_escolhida == 1:
                  cadastrar_novo_restaurante()
            elif opcao_escolhida == 2:
                  listar_restaurantes()
            elif opcao_escolhida == 3:
                  alternar_estado_restaurante()
            elif opcao_escolhida == 4:
                  finalizando_app()
            else:
                  opcao_invalida()
      except:
            opcao_invalida()

def main():
      os.system('cls')
      exibir_nome_do_programa()
      exibir_opcoes()
      escolher_opcao()
    

if __name__ == '__main__':
      main()