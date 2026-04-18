# framework_universidade/infra/console/menus/menu_cadastro.py

from infra.console.menus.menu import Menu
from typing import Any

class MenuCadastro(Menu):
    """
    Submenu genérico padronizado para operações de CRUD (Cadastro).
    Ele herda de Menu e já pré-configura as 5 opções clássicas:
    Inclusão, Alteração, Exclusão, Visualização e Listagem.
    """

    def __init__(self, titulo: str, 
                 form_inclusao: Any, 
                 form_alteracao: Any, 
                 form_exclusao: Any, 
                 form_visualizacao: Any, 
                 form_listagem: Any):
        """
        Construtor que recebe o título do menu e as instâncias das 5 telas 
        (formulários) específicas da entidade que será gerenciada.
        """
        super().__init__(titulo)

        # Injeção de Dependência: O menu não sabe SE é Aluno ou Professor, 
        # ele apenas mapeia os métodos 'executar' de cada formulário injetado.
        self.adicionar_opcao(1, "Incluir", form_inclusao.executar)
        self.adicionar_opcao(2, "Alterar", form_alteracao.executar)
        self.adicionar_opcao(3, "Excluir", form_exclusao.executar)
        self.adicionar_opcao(4, "Visualizar", form_visualizacao.executar)
        self.adicionar_opcao(5, "Listar Todos", form_listagem.executar)