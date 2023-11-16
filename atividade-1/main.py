from pessoaJuridica import PessoaJuridica
from cursos import Curso
from aluno import Aluno
from Inscricao import Inscricao

def main():
    
    # Criando instâncias da classe PessoaJuridica
    pessoaJuridica2 = PessoaJuridica("Empresa Y", "7654321/0002", "Maria", "51888888888", "Rua B")

    # Criando instâncias da classe Aluno
    aluno1 = Aluno("João", "5199999999", "Rua A", "20/04/2001", "94217491145", "1001")
    aluno2 = Aluno("Maria", "51888888888", "Rua B", "25/06/2000", "925871111", "1002")
    
    # Criando instâncias da classe Curso
    curso1 = Curso("Curso de Python", "40 horas")
    curso2 = Curso("Curso de POO", "60 horas")

    # Criando instâncias da classe Inscricao
    inscricao1 = Inscricao("123456789", "01/03/2023", curso1, aluno1, aluno1)
    inscricao2 = Inscricao("987654321", "15/03/2023", curso2, aluno2, pessoaJuridica2)

    # Exibindo informaçõesda da Inscrição 1
    print(f"Informações da Inscrição 1:\nNome aluno: {inscricao1.aluno_matriculado.nome}\nCurso: {inscricao1.curso.nome}\nNúmero matrícula: {inscricao1.numero_matricula}\nData Matrícula: {inscricao1.data_matricula}\nContratante: {inscricao1.aluno_matriculado.nome}\n")

    # Exibindo informaçõesda da Inscrição 2
    print(f"\nInformações da Inscrição 2:\nNome aluno: {inscricao2.aluno_matriculado.nome}\nCurso: {inscricao2.curso.nome}\nNúmero matrícula: {inscricao2.numero_matricula}\nData Matrícula: {inscricao2.data_matricula}\nContratante: {inscricao2.contratante.razao_social}\n")

if __name__ == "__main__":
    main()