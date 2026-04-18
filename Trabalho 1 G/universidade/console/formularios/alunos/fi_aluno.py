from infra import FInclusao
from universidade.entidades.aluno import Aluno

class FIAluno(FInclusao):
    def __init__(self, gerenciador_alunos):
        # Injeção de dependência e título
        super().__init__(titulo="INCLUSÃO DE ALUNO", gerenciador=gerenciador_alunos)

    def _coletar_dados(self) -> Aluno:
        # Captura inputs do console
        nome = input("Nome Completo: ").strip()
        data = input("Data de Ingresso: ").strip()
        
        # Retorna a entidade sem ID (será gerado pelo banco)
        return Aluno(id_aluno=None, nome=nome, data_ingresso=data)