# Em uma escola é necessário que um aluno pertença a somente menos uma turma.
# Você foi contratado para desenvolver um sistema que gerencie as turmas e os alunos.
# Cada turma tem um nome e uma lista de alunos.
# Cada aluno tem um nome e uma idade.
# O sistema deve permitir:
# - Adicionar uma nova turma
# - Adicionar um aluno a uma turma (verificando se o aluno já não pertence a outra turma)
# - Remover um aluno de uma turma
# - Listar todos os alunos de uma turma
# - Listar todas as turmas e seus respectivos alunos
# Utilize conjuntos para armazenar as turmas e os alunos, garantindo que um aluno não possa estar em mais de uma turma ao mesmo tempo.
class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __hash__(self):
        return hash((self.nome, self.idade))

    def __eq__(self, other):
        return self.nome == other.nome and self.idade == other.idade

    def __repr__(self):
        return f"{self.nome} ({self.idade} anos)"

class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = set()

    def adicionar_aluno(self, aluno):
        self.alunos.add(aluno)

    def remover_aluno(self, aluno):
        self.alunos.discard(aluno)

    def listar_alunos(self):
        return list(self.alunos)

    def __repr__(self):
        return f"Turma: {self.nome}, Alunos: {self.listar_alunos()}"

class SistemaEscolar:
    def __init__(self):
        self.turmas = {}
        self.alunos_em_turmas = set()

    def adicionar_turma(self, nome_turma):
        if nome_turma not in self.turmas:
            self.turmas[nome_turma] = Turma(nome_turma)

    def adicionar_aluno_a_turma(self, nome_turma, aluno):
        if aluno in self.alunos_em_turmas:
            print(f"O aluno {aluno.nome} já pertence a outra turma.")
            return
        if nome_turma in self.turmas:
            self.turmas[nome_turma].adicionar_aluno(aluno)
            self.alunos_em_turmas.add(aluno)
        else:
            print(f"A turma {nome_turma} não existe.")

    def remover_aluno_de_turma(self, nome_turma, aluno):
        if nome_turma in self.turmas:
            self.turmas[nome_turma].remover_aluno(aluno)
            self.alunos_em_turmas.discard(aluno)
        else:
            print(f"A turma {nome_turma} não existe.")

    def listar_alunos_de_turma(self, nome_turma):
        if nome_turma in self.turmas:
            return self.turmas[nome_turma].listar_alunos()
        else:
            print(f"A turma {nome_turma} não existe.")
            return []

    def listar_turmas(self):
        return list(self.turmas.values())

# Exemplo de uso
sistema = SistemaEscolar()
sistema.adicionar_turma("Matemática")
sistema.adicionar_turma("História")
aluno1 = Aluno("João", 15)
aluno2 = Aluno("Maria", 14)
sistema.adicionar_aluno_a_turma("Matemática", aluno1)
sistema.adicionar_aluno_a_turma("História", aluno2)
sistema.adicionar_aluno_a_turma("História", aluno1)  # Deve avisar que João já está em outra turma
print(sistema.listar_alunos_de_turma("Matemática"))  # [João (15 anos)]
print(sistema.listar_turmas())  # Lista todas as turmas e seus alunos
