# JARVIS PYTHON PURO - SEM DEPENDÊNCIAS
# Funciona em QUALQUER PC com Python instalado

import datetime
import os
import subprocess
import webbrowser
import sys

def limpar_tela():
    subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)

def mostrar_hora():
    agora = datetime.datetime.now()
    print(f"\n🕐 HORA ATUAL: {agora.strftime('%H:%M:%S')}")
    print(f"📅 DATA: {agora.strftime('%d/%m/%Y %A')}")
    input("\nPressione Enter para continuar...")

def abrir_site():
    print("\n🌐 ESCOLHA UM SITE:")
    print("1 - YouTube")
    print("2 - Google")
    print("3 - GitHub")
    print("4 - Whatsapp")
    print("5 - Tiktok")
    print("6 - Instagram")
    
    escolha = input("Digite o número: ").strip()
    sites = {'1': 'https://youtube.com', '2': 'https://google.com', '3': 'https://github.com', '4': 'https://web.whatsapp.com', '5': 'https://tiktok.com', '6': 'https://instagram.com'}
    
    if escolha in sites:
        webbrowser.open(sites[escolha])
        print(f"✅ ABRINDO {sites[escolha]}")
    else:
        print("❌ Opção inválida!")
    
    input("\nPressione Enter para continuar...")

def info_sistema():
    print("\n💻 INFORMAÇÕES DO SISTEMA:")
    print(f"Sistema: {os.name.upper()}")
    print(f"Usuário: {os.getenv('USERNAME', os.getenv('USER', 'Desconhecido'))}")
    print(f"Pasta atual: {os.getcwd()}")
    input("\nPressione Enter para continuar...")

def menu_principal():
    while True:
        limpar_tela()
        print("🤖" + "="*50)
        print("         J A R V I S   S I M P L E")
        print("🤖" + "="*50)
        print("1 - 🕐 Mostrar Hora")
        print("2 - 🌐 Abrir Site")
        print("3 - 💻 Info do PC")
        print("4 - 💬 Abrir whatsapp")
        print("5 - 🎵 Abrir Tiktok")
        print("6 - 💬 Abrir Instagram")
        print("7 - ❌ Sair")
        print("="*50)
        
        escolha = input(" Digite sua escolha senhor(a): ").strip()
        
        if escolha == "1":
            mostrar_hora()
        elif escolha == "2":
            abrir_site()
        elif escolha == "3":
            info_sistema()
        elif escolha == "4":
            webbrowser.open("https://web.whatsapp.com")
            print("\n✅ ABRINDO WHATSAPP")
            input("Pressione Enter para continuar...")
        elif escolha == "5":
            webbrowser.open("https://tiktok.com")
            print("\n✅ ABRINDO TIKTOK")
            input("Pressione Enter para continuar...")
        elif escolha == "6":
            print("\n👋 JARVIS desligando. Até logo senhor(a)!")
            sys.exit(0)
        else:
            print("\n❌ Opção inválida! Tente novamente.")
            input("Pressione Enter...")

if __name__ == "__main__":
    print("Iniciando JARVIS...")
    menu_principal()