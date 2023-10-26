from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica
from cursos import Curso
from aluno import Aluno
from inscrição import Inscricao

def main():
    pessoaFisica1 = PessoaFisica("Eduardo", "51999999999", "Rua X", "1999", "12345678")
    pessoaJuridica1 = PessoaJuridica("Empresa X", "51888888888", "Rua Y", "1234567/0001")

    cursos1 = Curso("Curso de Python", 120)
    aluno1 = Aluno(pessoaFisica1, "12345678", "aluno@gmail.com")

    cursos2 = Curso("Curso de POO", 120)
    aluno2 = Aluno(pessoaJuridica1, "12345678", "aluno@gmail.com")

    inscricao1 = Inscricao()

    print(pessoaFisica1)
    print(pessoaJuridica1)
    print(cursos1)
    print(aluno1)

    inscricao1.inscrever_aluno(aluno1.pessoa.nome, cursos1.nome)
    inscricao1.inscrever_aluno(aluno2.pessoa.nome, cursos2.nome)
    
    print(inscricao1)

if __name__ == "__main__":
    main()