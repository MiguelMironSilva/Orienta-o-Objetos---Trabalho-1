# framework_universidade/infra/console/menus/__init__.py

"""
Pacote de Menus Base (Infraestrutura)
Contém as classes genéricas para a criação, gerenciamento e renderização 
de menus interativos de texto no console.
"""

from .menu import Menu
from .menu_cadastro import MenuCadastro

# Define os módulos exportados ao utilizar 'from infra.console.menus import *'
__all__ = [
    "Menu",
    "MenuCadastro"
]