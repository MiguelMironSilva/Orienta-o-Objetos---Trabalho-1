from universidade.console import MenuPrincipal
from universidade.dados import FabricaDAOSQLite

if __name__ == "__main__":
    # Inicializa o banco e injeta as dependências
    fabrica = FabricaDAOSQLite()
    menu = MenuPrincipal(fabrica)
    menu.executar()