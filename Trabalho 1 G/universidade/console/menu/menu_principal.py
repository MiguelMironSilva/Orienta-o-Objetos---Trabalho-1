# framework_universidade/universidade/console/menus/menu_principal.py

from infra import Menu, MenuCadastro

# Importa a fábrica que criará nossas conexões com o banco de dados
from universidade.dados import FabricaDAOSQLite

# Importa os gerenciadores que contêm as regras de negócio
from universidade.negocio import (
    GerenciadorDepartamentos, GerenciadorCursos, 
    GerenciadorProfessores, GerenciadorAlunos, GerenciadorMatriculas
)

# Importa todas as telas usando a nossa fachada limpa
from universidade.console.formularios import (
    FIDepartamento, FADepartamento, FEDepartamento, FVDepartamento, FLDepartamento,
    FICurso, FACurso, FECurso, FVCurso, FLCurso,
    FIProfessor, FAProfessor, FEProfessor, FVProfessor, FLProfessor,
    FIAluno, FAAluno, FEAluno, FVAluno, FLAluno,
    FIMatricula, FAMatricula, FEMatricula, FVMatricula, FLMatricula
)

class MenuPrincipal(Menu):
    """
    Menu Principal do Sistema Universitário.
    Responsável por instanciar todas as dependências (DAOs e Gerenciadores),
    injetá-las nos formulários corretos e construir a árvore de navegação.
    """

    def __init__(self, fabrica_db: FabricaDAOSQLite):
        super().__init__("SISTEMA DE GESTÃO UNIVERSITÁRIA")

        # 1. Criação dos DAOs (Acesso a Dados)
        dao_deptos = fabrica_db.criar_dao_departamentos()
        dao_cursos = fabrica_db.criar_dao_cursos()
        dao_profs = fabrica_db.criar_dao_professores()
        dao_alunos = fabrica_db.criar_dao_alunos()
        dao_matriculas = fabrica_db.criar_dao_matriculas()

        # 2. Criação dos Gerenciadores (Regras de Negócio)
        # Injetamos os DAOs para que a camada de negócio possa salvar os dados
        ger_deptos = GerenciadorDepartamentos(dao_deptos)
        ger_cursos = GerenciadorCursos(dao_cursos)
        ger_profs = GerenciadorProfessores(dao_profs)
        ger_alunos = GerenciadorAlunos(dao_alunos)
        ger_matriculas = GerenciadorMatriculas(dao_matriculas)

        # 3. Montagem dos Submenus (Utilizando a abstração do MenuCadastro)
        
        # Módulo de Departamentos
        telas_depto = (
            FIDepartamento(ger_deptos), FADepartamento(ger_deptos),
            FEDepartamento(ger_deptos), FVDepartamento(ger_deptos), FLDepartamento(ger_deptos)
        )
        menu_deptos = MenuCadastro("MÓDULO DE DEPARTAMENTOS", *telas_depto)

        # Módulo de Cursos
        telas_curso = (
            FICurso(ger_cursos), FACurso(ger_cursos),
            FECurso(ger_cursos), FVCurso(ger_cursos), FLCurso(ger_cursos)
        )
        menu_cursos = MenuCadastro("MÓDULO DE CURSOS", *telas_curso)

        # Módulo de Professores
        telas_prof = (
            FIProfessor(ger_profs), FAProfessor(ger_profs),
            FEProfessor(ger_profs), FVProfessor(ger_profs), FLProfessor(ger_profs)
        )
        menu_profs = MenuCadastro("MÓDULO DE PROFESSORES", *telas_prof)

        # Módulo de Alunos
        telas_aluno = (
            FIAluno(ger_alunos), FAAluno(ger_alunos),
            FEAluno(ger_alunos), FVAluno(ger_alunos), FLAluno(ger_alunos)
        )
        menu_alunos = MenuCadastro("MÓDULO DE ALUNOS", *telas_aluno)

        # Módulo de Matrículas
        telas_matricula = (
            FIMatricula(ger_matriculas), FAMatricula(ger_matriculas),
            FEMatricula(ger_matriculas), FVMatricula(ger_matriculas), FLMatricula(ger_matriculas)
        )
        menu_matriculas = MenuCadastro("MÓDULO DE MATRÍCULAS", *telas_matricula)

        # 4. Registro das Opções no Menu Principal
        self.adicionar_opcao(1, "Gerenciar Departamentos", menu_deptos.executar)
        self.adicionar_opcao(2, "Gerenciar Cursos", menu_cursos.executar)
        self.adicionar_opcao(3, "Gerenciar Professores", menu_profs.executar)
        self.adicionar_opcao(4, "Gerenciar Alunos", menu_alunos.executar)
        self.adicionar_opcao(5, "Gerenciar Matrículas", menu_matriculas.executar)