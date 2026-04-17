# framework_universidade/infra/__init__.py

"""
Infra Package
Este pacote contém o mini-framework base para aplicações CRUD.
Ele é agnóstico de domínio e pode ser reutilizado em qualquer sistema.
"""

# 1. Importações da Camada de Entidades
from .entidades import Registro

# 2. Importações da Camada de Dados
from .dados import DAOBase, GerenciadorDB

# 3. Importações da Camada de Apresentação (Console)
#from .console.menus.menu import Menu
#from .console.menus.menu_cadastro import MenuCadastro

#from .console.formularios.formulario_base import FormularioBase
#from .console.formularios.f_inclusao import FInclusao
#from .console.formularios.f_alteracao import FAlteracao
#from .console.formularios.f_exclusao import FExclusao
#from .console.formularios.f_listagem import FListagem
#from .console.formularios.f_visualizacao import FVisualizacao

from .console import (
    Menu,
    MenuCadastro,
    FormularioBase,
    FInclusao,
    FAlteracao,
    FExclusao,
    FListagem,
    FVisualizacao,
    ConsoleUtil
)

from .console.util.console_util import ConsoleUtil

# 4. Importações de Exceções Comuns
from .excecoes import RegistroNaoEncontradoError, ErroDeValidacao

# Define explicitamente o que é exportado quando alguém usa `from infra import *`
__all__ = [
    "Registro",
    "DAOBase",
    "GerenciadorDB",
    "Menu",
    "MenuCadastro",
    "FormularioBase",
    "FInclusao",
    "FAlteracao",
    "FExclusao",
    "FListagem",
    "FVisualizacao",
    "ConsoleUtil",
    "RegistroNaoEncontradoError",
    "ErroDeValidacao"
]