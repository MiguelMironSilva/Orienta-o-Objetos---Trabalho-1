from .aluno import Aluno
from .curso import Curso
from .departamento import Departamento
from .matricula import Matricula
from .professor import Professor

# Define a API pública da camada de negócios da aplicação
__all__ = [
	"Aluno",
	"Curso",
	"Departamento",
	"Matricula",
	"Professor"
]