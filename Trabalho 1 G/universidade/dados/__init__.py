# framework_universidade/universidade/dados/__init__.py

"""
Pacote de Dados (Universidade)
Contém as implementações concretas de acesso ao banco de dados relacional (SQL)
para o domínio da universidade, utilizando o framework 'infra'.
"""

from .dao_departamentos import DAODepartamentos
from .dao_cursos import DAOCursos
from .dao_professores import DAOProfessores
from .dao_alunos import DAOAlunos
from .dao_matriculas import DAOMatriculas
from .fabrica_dao_sql import FabricaDAOSQLite

# Define a API pública da camada de dados da aplicação
__all__ = [
    "DAODepartamentos",
    "DAOCursos",
    "DAOProfessores",
    "DAOAlunos",
    "DAOMatriculas",
    "FabricaDAOSQLite"
]