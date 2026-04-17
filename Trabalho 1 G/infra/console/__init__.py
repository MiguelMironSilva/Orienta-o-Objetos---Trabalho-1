# framework_universidade/infra/console/__init__.py

"""
Pacote Console (Infraestrutura)
Fornece as classes base e utilitários genéricos para construção de interfaces de texto.
"""

# Importações limpas puxando diretamente dos sub-pacotes (graças aos __init__.py deles)
from .menus import Menu, MenuCadastro

from .formularios import (
    FormularioBase,
    FInclusao,
    FAlteracao,
    FExclusao,
    FListagem,
    FVisualizacao
)

from .util import ConsoleUtil

# Define explicitamente a API pública do pacote infra.console
__all__ = [
    "Menu",
    "MenuCadastro",
    "FormularioBase",
    "FInclusao",
    "FAlteracao",
    "FExclusao",
    "FListagem",
    "FVisualizacao",
    "ConsoleUtil"
]