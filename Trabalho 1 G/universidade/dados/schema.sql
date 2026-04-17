-- universidade/dados/schema.sql

CREATE TABLE IF NOT EXISTS departamento (
    id_departamento INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    sigla VARCHAR(10) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS curso (
    id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    creditos INTEGER NOT NULL,
    id_departamento INTEGER NOT NULL,
    FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento)
);

CREATE TABLE IF NOT EXISTS professor (
    id_professor INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    titulacao VARCHAR(50) NOT NULL,
    id_departamento INTEGER NOT NULL,
    FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento)
);

CREATE TABLE IF NOT EXISTS aluno (
    id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    data_ingresso DATE NOT NULL,
    matricula_ativa BOOLEAN NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS matricula (
    id_matricula INTEGER PRIMARY KEY AUTOINCREMENT,
    id_aluno INTEGER NOT NULL,
    id_curso INTEGER NOT NULL,
    semestre VARCHAR(10) NOT NULL,
    FOREIGN KEY (id_aluno) REFERENCES aluno(id_aluno),
    FOREIGN KEY (id_curso) REFERENCES curso(id_curso),
    UNIQUE(id_aluno, id_curso, semestre) -- Prevents duplicate enrollments in the same semester
);