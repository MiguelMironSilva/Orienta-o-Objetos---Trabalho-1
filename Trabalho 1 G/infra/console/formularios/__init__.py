# framework_universidade/infra/console/formularios/__init__.py

"""
Pacote de Formulários Base (Infraestrutura)
Contém as classes genéricas para a construção de telas e formulários
de texto no console para operações CRUD.
"""

from .formulario_base import FormularioBase
from .f_inclusao import FInclusao
from .f_alteracao import FAlteracao
from .f_exclusao import FExclusao
from .f_listagem import FListagem
from .f_visualizacao import FVisualizacao

# Define os módulos exportados ao utilizar 'from infra.console.formularios import *'
__all__ = [
    "FormularioBase",
    "FInclusao",
    "FAlteracao",
    "FExclusao",
    "FListagem",
    "FVisualizacao"
]