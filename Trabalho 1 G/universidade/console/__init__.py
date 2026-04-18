# framework_universidade/universidade/console/__init__.py

"""
Pacote Console (Universidade)
Contém a interface de linha de comando específica para o sistema da Universidade.
"""

from .menu.menu_principal import MenuPrincipal

# Exibe apenas o MenuPrincipal para o app.py. 
# Os formulários específicos (FIAluno, etc.) serão importados e instanciados 
# sob demanda dentro do próprio MenuPrincipal ou de seus submenus.
__all__ = [
    "MenuPrincipal"
]