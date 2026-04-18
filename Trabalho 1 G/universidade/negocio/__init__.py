# framework_universidade/universidade/negocio/__init__.py

"""
Pacote de Negócios (Universidade)
Contém as regras de negócio, validações e controladores do domínio da universidade.
Esta camada atua como intermediária entre a interface (console) e o acesso a dados (DAOs).
"""

from .gerenciador_departamentos import GerenciadorDepartamentos
from .gerenciador_cursos import GerenciadorCursos
from .gerenciador_professores import GerenciadorProfessores
from .gerenciador_alunos import GerenciadorAlunos
from .gerenciador_matriculas import GerenciadorMatriculas

# Define a API pública da camada de negócios da aplicação
__all__ = [
    "GerenciadorDepartamentos",
    "GerenciadorCursos",
    "GerenciadorProfessores",
    "GerenciadorAlunos",
    "GerenciadorMatriculas"
]