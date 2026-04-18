# framework_universidade/universidade/dados/fabrica_dao_sql.py

from infra import GerenciadorDB

# Importação das implementações concretas dos DAOs da Universidade
from universidade.dados.dao_departamentos import DAODepartamentos
from universidade.dados.dao_cursos import DAOCursos
from universidade.dados.dao_professores import DAOProfessores
from universidade.dados.dao_alunos import DAOAlunos
from universidade.dados.dao_matriculas import DAOMatriculas

class FabricaDAOSQLite:
    """
    Fábrica responsável por inicializar a conexão com o banco de dados SQLite
    e construir as instâncias de todos os DAOs específicos do domínio.
    """

    def __init__(self, nome_banco: str = "universidade.db", caminho_schema: str = "universidade/dados/schema.sql"):
        """
        No momento em que a fábrica é criada (lá no app.py), ela aciona o Singleton
        do GerenciadorDB, abre a conexão e garante que as tabelas existam.
        """
        self.db = GerenciadorDB()
        self.db.conectar(nome_banco)
        
        # Garante que a estrutura do banco (tabelas) esteja criada na primeira execução
        self.db.inicializar_banco_via_script(caminho_schema)

    # =========================================================================
    # MÉTODOS FABRICANTES (Factory Methods)
    # =========================================================================
    
    # Nota: Como o DAOBase já pega a conexão através do Singleton GerenciadorDB(),
    # nós só precisamos instanciar as classes concretas aqui e retorná-las.

    def criar_dao_departamentos(self) -> DAODepartamentos:
        return DAODepartamentos()

    def criar_dao_cursos(self) -> DAOCursos:
        return DAOCursos()

    def criar_dao_professores(self) -> DAOProfessores:
        return DAOProfessores()

    def criar_dao_alunos(self) -> DAOAlunos:
        return DAOAlunos()

    def criar_dao_matriculas(self) -> DAOMatriculas:
        return DAOMatriculas()