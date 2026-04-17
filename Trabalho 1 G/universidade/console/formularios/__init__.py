# framework_universidade/universidade/console/formularios/__init__.py

"""
Pacote de Formulários Específicos (Universidade)
Centraliza e exporta todas as telas (formulários de console) para as 
operações de CRUD do domínio da Universidade.
"""

# Importações do sub-pacote de Departamentos
from .departamentos import FIDepartamento, FADepartamento, FEDepartamento, FVDepartamento, FLDepartamento

# Importações do sub-pacote de Cursos
from .cursos import FICurso, FACurso, FECurso, FVCurso, FLCurso

# Importações do sub-pacote de Professores
from .professores import FIProfessor, FAProfessor, FEProfessor, FVProfessor, FLProfessor

# Importações do sub-pacote de Alunos
from .alunos import FIAluno, FAAluno, FEAluno, FVAluno, FLAluno

# Importações do sub-pacote de Matrículas
from .matriculas import FIMatricula, FAMatricula, FEMatricula, FVMatricula, FLMatricula

# Define a API pública de formulários para o MenuPrincipal
__all__ = [
    # Departamentos
    "FIDepartamento", "FADepartamento", "FEDepartamento", "FVDepartamento", "FLDepartamento",
    
    # Cursos
    "FICurso", "FACurso", "FECurso", "FVCurso", "FLCurso",
    
    # Professores
    "FIProfessor", "FAProfessor", "FEProfessor", "FVProfessor", "FLProfessor",
    
    # Alunos
    "FIAluno", "FAAluno", "FEAluno", "FVAluno", "FLAluno",
    
    # Matrículas
    "FIMatricula", "FAMatricula", "FEMatricula", "FVMatricula", "FLMatricula"
]