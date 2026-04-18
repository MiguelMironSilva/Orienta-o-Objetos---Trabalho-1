#from universidade.console import MenuPrincipal
#from universidade.dados import FabricaDAOSQLite

import sys
import os

# Garante que o Python encontre as pastas 'infra' e 'universidade'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dados.fabrica_dao_sql import FabricaDAOSQLite
from universidade.negocio.gerenciador_alunos import GerenciadorAlunos
from universidade.negocio.gerenciador_cursos import GerenciadorCursos
from universidade.negocio.gerenciador_departamentos import GerenciadorDepartamentos
from universidade.negocio.gerenciador_matriculas import GerenciadorMatriculas
from universidade.negocio.gerenciador_professores import GerenciadorProfessores
from universidade.console.menu_principal import MenuPrincipal

def main():
    print("Iniciando Sistema da Universidade...")
    
    try:
        # 1. Instancia a fábrica (Cria o banco e tabelas se não existirem)
        fabrica = FabricaDAOSQLite(
            nome_banco="universidade.db", 
            caminho_schema="universidade/dados/schema.sql"
        )
        
        # 2. Monta a Camada de Negócio (Injetando os DAOs da fábrica)
        # É aqui que o seu sistema ganha "vida"
        g_alunos = GerenciadorAlunos(fabrica.criar_aluno_dao())
        g_cursos = GerenciadorCursos(fabrica.criar_curso_dao())
        g_deptos = GerenciadorDepartamentos(fabrica.criar_departamento_dao())
        g_matriculas = GerenciadorMatriculas(fabrica.criar_matricula_dao())
        g_professores = GerenciadorProfessores(fabrica.criar_professor_dao())
        
        # 3. Injeta os Gerenciadores no Menu Principal
        menu = MenuPrincipal(g_alunos, g_cursos, g_deptos, g_matriculas, g_professores)
        
        # 4. Inicia a interface
        menu.exibir()

    except Exception as e:
        print(f"\n[FALHA CRÍTICA] Erro ao iniciar camadas: {e}")
    finally:
        print("\nSistema encerrado de forma segura.")

if __name__ == "__main__":
    main()