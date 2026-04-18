-- framework_universidade/universidade/dados/schema.sql

-- Ativa suporte a chaves estrangeiras no SQLite
PRAGMA foreign_keys = ON;

-- 1. Tabela Departamento (Não tem chaves estrangeiras, deve ser a primeira)
CREATE TABLE IF NOT EXISTS departamento (
    id_departamento INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    sigla TEXT NOT NULL UNIQUE
);

-- 2. Tabela Curso (Depende de Departamento)
CREATE TABLE IF NOT EXISTS curso (
    id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    duracao_semestres INTEGER NOT NULL,
    id_departamento INTEGER NOT NULL,
    FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento) ON DELETE RESTRICT
);

-- 3. Tabela Professor (Depende de Departamento)
CREATE TABLE IF NOT EXISTS professor (
    id_professor INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    titulacao TEXT NOT NULL,
    id_departamento INTEGER NOT NULL,
    FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento) ON DELETE RESTRICT
);

-- 4. Tabela Aluno (Independente)
CREATE TABLE IF NOT EXISTS aluno (
    id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL UNIQUE,
    data_ingresso TEXT NOT NULL,
    matricula_ativa INTEGER DEFAULT 1 -- SQLite não tem booleano nativo, usamos 1 para True e 0 para False
);

-- 5. Tabela Associativa Matrícula (Depende de Aluno e Curso)
CREATE TABLE IF NOT EXISTS matricula (
    id_matricula INTEGER PRIMARY KEY AUTOINCREMENT,
    id_aluno INTEGER NOT NULL,
    id_curso INTEGER NOT NULL,
    data_matricula TEXT NOT NULL,
    status TEXT DEFAULT 'Ativa',
    FOREIGN KEY (id_aluno) REFERENCES aluno(id_aluno) ON DELETE CASCADE,
    FOREIGN KEY (id_curso) REFERENCES curso(id_curso) ON DELETE RESTRICT
);