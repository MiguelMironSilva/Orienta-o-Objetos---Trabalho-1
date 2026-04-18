from infra import FListagem
from universidade.negocio.gerenciador_departamentos import GerenciadorDepartamentos

class FLDepartamento(FListagem):
    """Exibe a lista de unidades acadêmicas (sigla e nome)."""
    def __init__(self, gerenciador_deptos: GerenciadorDepartamentos):
        super().__init__(titulo="LISTAGEM DE DEPARTAMENTOS", gerenciador=gerenciador_deptos, colunas=["ID", "Nome", "Sigla"], atributos=["id_departamento", "nome", "sigla"])