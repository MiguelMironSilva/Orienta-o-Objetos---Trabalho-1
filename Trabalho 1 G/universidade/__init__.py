# framework_universidade/universidade/__init__.py

"""
Pacote Universidade (Aplicação Principal)
Este pacote contém a implementação específica do sistema de gerenciamento 
universitário, construído inteiramente sobre o framework genérico 'infra'.
"""

# Metadados da aplicação
__version__ = "1.0.0"
__author__ = "Sua Equipe"

# Puxando os inicializadores principais dos sub-pacotes
from .dados import FabricaDAOSQLite 
from .console import MenuPrincipal

# Define a API pública de alto nível da aplicação
__all__ = [
    "FabricaDAOSQLite",
    "MenuPrincipal"
]