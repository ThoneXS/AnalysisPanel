from verificador_dominios import listar_dominios
from verificador_diretorios import analisar_subdiretorios
from port_scanner import verificar_portas_abertas
from todos_diretorios import obter_listas_diretorios
import colorama
from verificador_ip import obter_informacoes_ip
from colorama import Fore

colorama.init()

# Define as sequências de escape para as cores
azul_claro = colorama.Fore.LIGHTBLUE_EX
rosa = colorama.Fore.LIGHTMAGENTA_EX
reset = colorama.Fore.RESET


print(
    
"""

                                    \033[94m████████╗\033[0m\033[94m██╗░░██╗\033[0m\033[94m░█████╗░\033[0m\033[95m███╗░░██╗\033[0m\033[95m███████╗\033[0m\033[95m██╗░░██╗\033[0m 
                                    \033[94m╚══██╔══╝\033[0m\033[94m██║░░██║\033[0m\033[94m██╔══██╗\033[0m\033[95m████╗░██║\033[0m\033[95m██╔════╝\033[0m\033[95m╚██╗██╔╝\033[0m 
                                    \033[94m░░░██║░░░\033[0m\033[94m██╔══██║\033[0m\033[94m██║░░██║\033[0m\033[95m██║╚████║\033[0m\033[95m██╔══╝░░\033[0m\033[95m░██╔██╗░\033[0m 
                                    \033[94m░░░██║░░░\033[0m\033[94m██║░░██║\033[0m\033[94m╚█████╔╝\033[0m\033[95m██║░╚███║\033[0m\033[95m███████╗\033[0m\033[95m██╔╝╚██╗\033[0m 
                                    \033[94m░░░╚═╝░░░\033[0m\033[94m╚═╝░░╚═╝\033[0m\033[94m░╚════╝░\033[0m\033[95m╚═╝░░╚══╝\033[0m\033[95m╚══════╝\033[0m\033[95m╚═╝░░╚═╝\033[0m 

"""


                                             """Versão 0.0.1 \n"""
                                             
)


def options():
    print('\033[94m[1] \033[90mColeta de informação ativa WebSite\033[0m')
    print('\033[94m[2] \033[90mConsulta IP\033[0m')
    print('\033[94m[3] \033[90mMalware\033[0m')

    while True:
        escolha = input('\033[81m ———> \033[0m: ')

        if escolha == '1':
            print('[?] \033[90mListagem De Diretorios\033[0m')
            print('[?] \033[90mListagem De Dominios\033[0m')
            print('[?] \033[90mVerificação de portas\033[0m')
            print('[?] \033[90mTodos os diretorios\033[0m')


            escolha_coleta = input('\033[81mDigite o número da opção de coleta desejada\033[0m: ')
            
            if escolha_coleta == '1':
                site = input("Digite o nome do site a ser verificado: ")
                analisar_subdiretorios(site)
            
            elif escolha_coleta == '2':   
                site = input("Digite o nome do site para listar os domínios: ")
                listar_dominios(site)
                
            elif escolha_coleta == '3':
                host = input("Digite o endereço IP ou nome do host para verificar as portas: ")
                portas = [80, 443, 22, 3389]  
                verificar_portas_abertas(host, portas)

            elif escolha_coleta == '4':
             site = input("Digite o nome do site para listar os diretórios: ")
             listas = obter_listas_diretorios(site)
             print('Lista de Diretórios:')
             for diretorio in listas:
              print(diretorio)
            
        elif escolha == '2':
            ip = input('Digite o IP a ser verificado: ')
            obter_informacoes_ip(ip)
        
        elif escolha == '3':
            print('[?] \033[90mGet Ip\033[0m')
            print('[?] \033[90mRansomware\033[0m')
            print('[?] \033[90mRAT\033[0m')
            escolha_colet1 = input('\033[81mEscolha uma opção\033[0m: ')
            
            if escolha_colet1 == '1':
                print('https://github.com/ThoneXS/ipget/')
                
            elif escolha_colet1 == '2':
                print('https://github.com/ncorbuk/Python-Ransomware')
                
            elif escolha_colet1 == '3':
                print('https://github.com/FZGbzuw412/Python-RAT')
                
            else:
                print('Opção inválida.')
        
        else:
            print('Opção inválida.')

options()
