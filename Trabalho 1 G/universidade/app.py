import sys
import os

# Garante que o Python encontre as pastas 'infra' e 'universidade'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dados.fabrica_dao_sql import FabricaDAOSQLite
from universidade.console.menu.menu_principal import MenuPrincipal

def main():
    print("Iniciando Sistema da Universidade...")
    
    try:
        # 1. Instancia a fábrica (Cria o banco e tabelas se não existirem)
        fabrica = FabricaDAOSQLite(
            nome_banco="universidade.db", 
            caminho_schema="universidade/dados/schema.sql"
        )
        
        # 2. Injeta a Fábrica no Menu Principal
        # O MenuPrincipal se encarrega de criar os DAOs e Gerenciadores
        menu = MenuPrincipal(fabrica)
        
        # 3. Inicia a interface
        menu.executar()

    except Exception as e:
        print(f"\n[FALHA CRÍTICA] Erro ao iniciar camadas: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("\nSistema encerrado de forma segura.")

if __name__ == "__main__":
    main()
