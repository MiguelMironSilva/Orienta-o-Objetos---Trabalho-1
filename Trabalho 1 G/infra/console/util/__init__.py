# framework_universidade/infra/console/util/__init__.py

"""
Pacote Utilitário de Console (Infraestrutura)
Contém classes e funções auxiliares genéricas para a interface de texto, 
como leitura segura de dados do teclado, tratamento de entradas inválidas 
e conversão de tipos.
"""

from .console_util import ConsoleUtil

# Define os módulos exportados ao utilizar 'from infra.console.util import *'
__all__ = [
    "ConsoleUtil"
]