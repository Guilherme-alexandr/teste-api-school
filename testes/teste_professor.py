import unittest
from models.professores import professor_bp
import requests
from models.alunos import alunos_bp


class ProfessoresTestCase(unittest.TestCase):

    '''def test_000_professores_retorna_lista(self):
        r = requests.get('http://127.0.0.1:5000/professor/listar')
        if r.status_code == 404:
            self.fail("Você não definiu a página / professor no seu server")
        try:
            obj_retornado = r.json()
        except:
            self.fail("Queria um JSON mas você retornou outra coisa")

        self.assertEqual(type(obj_retornado),type([]))
        for professor in obj_retornado:
            print(f"Professor ID: {professor['id']}, Nome: {professor['nome']}, Idade: {professor['idade']}, Data de Nasc: {professor['data_nascimento']}, Disciplina{professor['disciplina']}, Salário{professor['salario']}")

    def test_001_adiciona_professores(self):

        r_marcos = requests.post('http://127.0.0.1:5000/professor/criar', json={'id': 2, 'nome': 'Marcos Paulo', 'idade': 44, 'datanasc': "01/07/1984", 'disciplina': 'Linguagem de Programação', 'salario': 3750.00})
        r_joao = requests.post('http://127.0.0.1:5000/professor/criar', json={'id': 3, 'nome': 'João Silva', 'idade': 25, 'datanasc': '01/01/2000', 'disciplina': 'Banco de Dados', 'salario': 4000.00})
        
        print(f"Status Code Marcos Paulo: {r_marcos.status_code}")
        print(f"Status Code Silva: {r_joao.status_code}")
        self.assertEqual(r_marcos.status_code, 201, "Erro ao criar professor Marcos Paulo")
        self.assertEqual(r_joao.status_code, 201, "Erro ao criar professor João Silva")
        
        r_lista = requests.get('http://127.0.0.1:5000/professor/listar')
        
        print(f"Status Code Listar Professores: {r_lista.status_code}")
        self.assertEqual(r_lista.status_code, 200, "Erro ao listar professor")

        lista_retornada = r_lista.json()
        print(f"Lista de professor atualizada: {lista_retornada}")
        
        achei_marcos = False
        achei_joao = False
        for professor in lista_retornada:
            if professor['nome'] == 'Marcos Paulo':
                achei_marcos = True
            if professor['nome'] == 'João Silva':
                achei_joao = True

        if not achei_marcos:
            self.fail('Professor "Marcos Paulo" não apareceu na lista de professor')
        if not achei_joao:
            self.fail('Professor "João Silva" não apareceu na lista de professor')
        if achei_marcos and achei_joao:
            print("Ambas os professor foram encontrados com sucesso na lista!")

    def test_002_professor_por_id(self):
        r = requests.post('http://127.0.0.1:5000/professor/criar', json={'id': 4, 'nome': 'Sérgio Perez', 'idade': 50, 'datanasc': '12/03/1980', 'disciplina': 'Linguagem SQL', 'salario': 2500.00})
    
        print("Resposta da criação de professor:", r.status_code, r.text)
        self.assertEqual(r.status_code, 201, "Erro ao criar professor")

        resposta = requests.get('http://127.0.0.1:5000/professor/filtrar/4')
        dict_retornado = resposta.json()
    
        print("Resposta da consulta do professor:", resposta.status_code, dict_retornado)

        self.assertEqual(type(dict_retornado), dict, "Resposta não é um dicionário")
        self.assertIn('nome', dict_retornado, "A chave 'nome' não foi encontrada na resposta")
        self.assertEqual(dict_retornado['nome'], 'Sérgio Perez', f"Esperado 'Sérgio Perez', mas obtido: {dict_retornado['nome']}")



    def test_003_reseta(self):
        r = requests.post('http://127.0.0.1:5000/professor/criar', json={'id': 1, 'nome': 'Pedro Santos', 'idade': 65, 'datanasc': '23/05/1960', 'disciplina': 'Soft Skills', 'salario': 3000.00})
        
        print("Resposta da criação de professor:", r.status_code, r.text)
        self.assertEqual(r.status_code, 201, "Erro ao criar professor")

        r_lista = requests.get('http://127.0.0.1:5000/professor/listar')
        print("Lista de professor antes do reset:", r_lista.status_code, r_lista.json())
        self.assertTrue(len(r_lista.json()) > 0)

        r_reset = requests.post('http://127.0.0.1:5000/professor/reseta')
        print("Resposta do reset de professor:", r_reset.status_code, r_reset.text)

        self.assertEqual(r_reset.status_code,200)
        r_lista_depois = requests.get('http://127.0.0.1:5000/professor/listar')
        print("Lista de professor após o reset:", r_lista_depois.status_code, r_lista_depois.json())
        
        self.assertEqual(len(r_lista_depois.json()),0)

    def test_004_deleta(self):
        r_reset = requests.post('http://127.0.0.1:5000/professor/reseta')
        print("Resposta do reset de professores:", r_reset.status_code, r_reset.text)
        self.assertEqual(r_reset.status_code,200)

        r_1 = requests.post('http://127.0.0.1:5000/professor/criar', json={'id': 1, 'nome': 'Marcos Paulo', 'idade': 44, 'data_nascimento': "01/07/1984", 'disciplina': 'Linguagem de Programação', 'salario': 3750.00})
        r_2 = requests.post('http://127.0.0.1:5000/professor/criar', json={'id': 2, 'nome': 'João Silva', 'idade': 25, 'data_nascimento': '01/01/2000', 'disciplina': 'Banco de Dados', 'salario': 4000.00})
        r_3 = requests.post('http://127.0.0.1:5000/professor/criar', json={'id': 3, 'nome': 'Gisele', 'idade': 43, 'data_nascimento': '06/05/1978', 'disciplina': 'Full-Stack', 'salario': 4000.00})

        print("Criação da Professor:", r_1.status_code, r_1.text)
        print("Criação da Professor:", r_2.status_code, r_2.text)
        print("Criação da Professor:", r_3.status_code, r_3.text)

        r_lista = requests.get('http://127.0.0.1:5000/professor/listar')
        lista_retornada = r_lista.json()
        print("Lista de professores após criação:", r_lista.status_code, lista_retornada)
        self.assertEqual(len(lista_retornada),3)
        
        r_delete_2 = requests.delete('http://127.0.0.1:5000/professor/2')
        print("Professor:", r_delete_2.status_code, r_delete_2.text)

        r_lista2 = requests.get('http://127.0.0.1:5000/professor/listar')
        lista_retornada2 = r_lista2.json()
        print("Lista de professores após deleção 2:", r_lista2.status_code, lista_retornada2)
        self.assertEqual(len(lista_retornada2),2) 

        acheiMarcos = False
        acheiGisele = False
        for professor in lista_retornada:
            if professor['nome'] == 'Marcos Paulo':
                acheiMarcos=True
            if professor['nome'] == 'Gisele':
                acheiGisele=True
        if not acheiMarcos or not acheiGisele:
            self.fail("voce parece ter deletado o professor errado!")

        requests.delete('http://127.0.0.1:5000/professor/3')

        r_delete_3 = r_lista3 = requests.get('http://127.0.0.1:5000/professor/listar')
        print("Resposta da deleção do professor:", r_delete_3.status_code, r_delete_3.text)
        lista_retornada3 = r_lista3.json()
        print("Lista de professores após deleção do professor 3:", r_lista3.status_code, lista_retornada3)
        self.assertEqual(len(lista_retornada3),1) 

        if lista_retornada3[0]['nome'] == 'Marcos Paulo':
            pass
        else:
            self.fail("voce parece ter deletado o aluno errado!")


        requests.delete('http://127.0.0.1:5000/professor/3')
    
    def test_005_edita(self):
        r_reset = requests.post('http://127.0.0.1:5000/professor/reseta')
        print("Resposta do reset de professor:", r_reset.status_code, r_reset.text)
        self.assertEqual(r_reset.status_code,200)

        r_criar =requests.post('http://127.0.0.1:5000/professor/criar', json={'id': 6, 'nome': 'Luis Araujo', 'idade': 56, 'datanasc': '03/04/1980', 'disciplina': 'Logica de Programação', 'salario': 4000.00})
        print("Resposta da criação:", r_criar.status_code, r_criar.text)

        r_antes = requests.get('http://127.0.0.1:5000/professor/filtrar/1')
        print("Resposta antes da edição:", r_antes.status_code, r_antes.json())
        self.assertEqual(r_antes.json()['nome'],'Luis Araujo')

        r_editar = requests.put('http://127.0.0.1:5000/professor/atualizar/1', json={'nome':'Jorge'})
        print("Resposta da edição dos professor:", r_editar.status_code, r_editar.text)

        r_depois = requests.get('http://127.0.0.1:5000/professor/filtrar/1')
        print("Resposta depois da edição:", r_depois.status_code, r_depois.json())

        self.assertEqual(r_depois.json()['nome'],'Jorge')
        self.assertEqual(r_depois.json()['id'],1)


    def test_006b_id_inexistente_no_get(self):

        r_reset = requests.post('http://127.0.0.1:5000/professor/reseta')
        print("Resposta do reset de professor:", r_reset.status_code, r_reset.text)

        self.assertEqual(r_reset.status_code, 200)

        r = requests.get('http://127.0.0.1:5000/professor/filtrar/15')
        print("Resposta da requisição GET para ID inexistente:", r.status_code, r.text)
        self.assertIn(r.status_code, [400, 404])

        error_retornado = r.json().get('error', '')
        print("Resposta JSON do erro:", error_retornado)
        self.assertEqual(error_retornado, 'Professor não encontrado')

     
    def test_006c_id_inexistente_no_delete(self):
     
        r_reset = requests.post('http://127.0.0.1:5000/professor/reseta')
        print("Resposta do reset de professor:", r_reset.status_code, r_reset.text)
        self.assertEqual(r_reset.status_code,200)

        r = requests.delete('http://127.0.0.1:5000/professor/15')
        print("Resposta da requisição DELETE para ID inexistente:", r.status_code, r.text)
        self.assertIn(r.status_code,[400,404])

        error_retornado = r.json().get('error', '')
        print("Resposta JSON do erro:", error_retornado)
        self.assertEqual(error_retornado, 'Professor não encontrado.')
    
    def test_007_criar_com_id_ja_existente(self):

        r_reset = requests.post('http://127.0.0.1:5000/professor/reseta')
        print("Resposta do reset de professor:", r_reset.status_code, r_reset.text)
        self.assertEqual(r_reset.status_code, 200, "Erro ao resetar as professor")

        r_1 = requests.post('http://127.0.0.1:5000/professor/criar', json={"id": 1, "nome": "Junior Santos", "idade": 34, "data_nascimento": "13/04/1980", "disciplina": "Desenvolvimento mobile", "salario": 7000.00})
        print("Resposta da criação do Professor", r_1.status_code, r_1.text)
        self.assertEqual(r_1.status_code, 201, "Erro ao criar Professor'")

        r_2 = requests.post('http://127.0.0.1:5000/professor/criar', json={"id": 1, "nome": "Carlos Miranda", "idade": 37, "data_nascimento": "05/04/1980", "disciplina": "Banco de Dados", "salario": 7000.00})
        print("Resposta ao tentar criar Professor com ID já existente:", r_2.status_code, r_2.text)
        self.assertEqual(r_2.status_code, 400, "O código de status não foi 400.")
    
        error_retornado = r_2.json().get('error', '')
        print("Resposta JSON do erro:", error_retornado)
        self.assertEqual(error_retornado, 'ID já utilizado.')


    def test_008a_post_sem_nome(self):
        r_reset = requests.post('http://127.0.0.1:5000/professor/reseta')
        print("Resposta do reset de professor:", r_reset.status_code, r_reset.text)
        self.assertEqual(r_reset.status_code, 200, "Erro ao resetar as professor")

        r = requests.post('http://127.0.0.1:5000/professor/criar', json={'id': 1})
        print("Resposta ao tentar criar professor sem nome:", r.status_code, r.text)

        self.assertEqual(r.status_code, 400, "O código de status não foi 400.")
        error_retornado = r.json().get('error', '')
        print("Resposta JSON do erro:", error_retornado)
        self.assertEqual(error_retornado, 'Nome é obrigatório.')'''

    def test_008b_put_sem_nome(self):
        r_reset = requests.post('http://127.0.0.1:5000/professor/reseta')
        print(f"Resposta do reset de professor: {r_reset.status_code} {r_reset.json()}")
        self.assertEqual(r_reset.status_code,200)

        r = requests.post('http://127.0.0.1:5000/professor/criar',json={"nome":"Minimus","id":1})
        print(f"Resposta ao criar professor: {r.status_code} {r.json()}")
        self.assertEqual(r.status_code,201)

        r = requests.put('http://127.0.0.1:5000/professor/atualizar/1',json={"id":1})
        print(f"Resposta ao editar professor sem nome: {r.status_code} {r.json()}")
        self.assertEqual(r.status_code,400)
        self.assertEqual(r.json()['erro'],'Professor sem nome')

    '''def test_100b_nao_confundir_professor_e_aluno(self):
        r_reset = requests.post('http://127.0.0.1:5000/professor/reseta')
        print("Reset response:", r_reset.status_code, r_reset.json())
        self.assertEqual(r_reset.status_code, 200)

        r = requests.post('http://127.0.0.1:5000/aluno/criar', json={'nome': '', 'idade': ''})
        print("Add aluno Yuri Tito response:", r.status_code, r.json())

        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()['error'], 'Nome e idade são obrigatórios.')

        r_aluno = requests.post('http://127.0.0.1:5000/aluno/criar', json={'nome': 'Yuri Tito', 'idade': 22})
        print("Add aluno Yuri Tito response:", r_aluno.status_code, r_aluno.json())
        self.assertEqual(r_aluno.status_code, 200)


    def test_101_adiciona_professores(self):
        r = requests.post('http://127.0.0.1:5000/professor/criar', json={'nome': 'Yuri Tito', 'id': 1})
        print("Resposta ao adicionar Yuri Tito:", r.status_code, r.json() if r.content else "(Sem resposta JSON)")
        r = requests.post('http://127.0.0.1:5000/professor/criar', json={'nome': 'Luiz Queiroz', 'id': 2})
        print("Resposta ao adicionar Luiz Queiroz:", r.status_code, r.json() if r.content else "(Sem resposta JSON)")
        r_lista = requests.get('http://127.0.0.1:5000/professor/listar')
        print("Lista de professores:", r_lista.json())
        achei_yuri = False
        achei_luiz = False
        for professor in r_lista.json():
            if professor['nome'] == 'Yuri Tito':
                achei_yuri = True
            if professor['nome'] == 'Luiz Queiroz':
                achei_luiz = True
        if not achei_yuri:
            self.fail('Professor Yuri Tito nao apareceu na lista de professores')
        if not achei_luiz:
            self.fail('Professor Luiz Queiroz nao apareceu na lista de professores')


    def test_102_professores_por_id(self):
        r = requests.post('http://127.0.0.1:5000/professor/criar', json={'nome': 'Luciano Silva', 'id': 20})
        print("POST /professores:", r.status_code, r.json() if r.status_code == 200 else r.text)

        r_lista = requests.get('http://127.0.0.1:5000/professor/filtrar/20')
        print("GET /professores/20:", r_lista.status_code, r_lista.json() if r_lista.status_code == 200 else r.text)

        self.assertEqual(r_lista.json()['nome'], 'Luciano Silva')


    def test_103_adiciona_e_reseta(self):
        r = requests.post('http://127.0.0.1:5000/professor/criar', json={'nome': 'João Roberto', 'id': 29})
        print("POST /professores:", r.status_code, r.json() if r.status_code == 200 else r.text)
        r_lista = requests.get('http://127.0.0.1:5000/professor/listar')
        print("GET /professores antes do reset:", r_lista.status_code, r_lista.json() if r_lista.status_code == 200 else r.text)
        self.assertTrue(len(r_lista.json()) > 0)
        r_reset = requests.post('http://127.0.0.1:5000/reseta')
        print("POST /reseta:", r_reset.status_code, r_reset.json() if r_reset.status_code == 200 else r.text)
        self.assertEqual(r_reset.status_code, 200)
        r_lista_depois = requests.get('http://127.0.0.1:5000/professor/listar')
        print("GET /professores depois do reset:", r_lista_depois.status_code, r_lista_depois.json() if r_lista_depois.status_code == 200 else r.text)
        self.assertEqual(len(r_lista_depois.json()), 0)


    def test_104_deleta(self):
        r_reset = requests.post('http://127.0.0.1:5000/professor/reseta')
        print("POST /reseta:", r_reset.status_code, r_reset.json() if r_reset.status_code == 200 else r_reset.text)
        self.assertEqual(r_reset.status_code, 200)
        r1 = requests.post('http://127.0.0.1:5000/professor/criar', json={'nome': 'João Roberto', 'id': 29})
        print("POST /professores (João Roberto):", r1.status_code, r1.json() if r1.status_code == 200 else r1.text)
        r2 = requests.post('http://127.0.0.1:5000/professor/criar', json={'nome': 'Vanessa Lima', 'id': 28})
        print("POST /professores (Vanessa Lima):", r2.status_code, r2.json() if r2.status_code == 200 else r2.text)
        r_lista = requests.get('127.0.0.1:5000/professor/listar')
        print("GET /professores antes da deleção:", r_lista.status_code, r_lista.json() if r_lista.status_code == 200 else r_lista.text)
        self.assertEqual(len(r_lista.json()), 2)
        r_delete = requests.delete('http://127.0.0.1:5000/professor/28')
        print("DELETE /professores/28:", r_delete.status_code, r_delete.json() if r_delete.status_code == 200 else r_delete.text)
        r_lista = requests.get('http://127.0.0.1:5000/professor/listar')
        print("GET /professores depois da deleção:", r_lista.status_code, r_lista.json() if r_lista.status_code == 200 else r_lista.text)
        self.assertEqual(len(r_lista.json()), 1)

    def test_105_edita(self):
        r_reset = requests.post('http://127.0.0.1:5000/professor/reseta')
        print("Resposta do reset:", r_reset.status_code)
        self.assertEqual(r_reset.status_code, 200)
        r_add = requests.post('http://127.0.0.1:5000/professores/criar', json={'nome': 'Vanessa Lima', 'id': 28})
        print("Resposta ao adicionar professor:", r_add.status_code)
        r_antes = requests.get('http://127.0.0.1:5000/professor/filtar/28')
        print("Nome do professor antes da edição:", r_antes.json()['nome'])
        self.assertEqual(r_antes.json()['nome'], 'Vanessa Lima')
        r_edita = requests.put('http://127.0.0.1:5000/professor/atualizar/28', json={'nome': 'Vanessa Lima mendes'})
        print("Resposta ao editar professor:", r_edita.status_code)
        r_depois = requests.get('http://127.0.0.1:5000/professor/filtar/28')
        print("Nome do professor depois da edição:", r_depois.json()['nome'])
        self.assertEqual(r_depois.json()['nome'], 'Vanessa Lima mendes')


    def test_106_id_inexistente(self):
        r_reset = requests.post('http://127.0.0.1:5000/reseta')
        print("Resposta do reset:", r_reset.status_code)
        self.assertEqual(r_reset.status_code, 200)
        r = requests.put('http://127.0.0.1:5000/professor/atualizar/15', json={'nome': 'Luigi Bros', 'id': 15})
        print("Resposta ao tentar editar professor com ID inexistente (PUT):", r.status_code)
        print("Erro ao editar (PUT):", r.json())
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()['erro'], 'professor nao encontrado')
        r = requests.get('http://127.0.0.1:5000/professor/filtar/15')
        print("Resposta ao tentar obter professor com ID inexistente (GET):", r.status_code)
        print("Erro ao obter (GET):", r.json())
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()['erro'], 'professor nao encontrado')
        r = requests.delete('http://127.0.0.1:5000/professor/15')
        print("Resposta ao tentar deletar professor com ID inexistente (DELETE):", r.status_code)
        print("Erro ao deletar (DELETE):", r.json())
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()['erro'], 'professor nao encontrado')


    def test_107_criar_com_id_ja_existente(self):
        r_reset = requests.post('http://127.0.0.1:5000/professor/reseta')
        print("Resposta do reset:", r_reset.status_code)
        self.assertEqual(r_reset.status_code, 200)
        r = requests.post('http://127.0.0.1:5000/professor/criar', json={'nome': 'Márcio', 'id': 7})
        print("Resposta ao criar o primeiro professor (Márcio):", r.status_code)
        self.assertEqual(r.status_code, 200)
        r = requests.post('http://127.0.0.1:5000/professor/criar', json={'nome': 'Ferreira', 'id': 7})
        print("Resposta ao tentar criar o segundo professor com ID já existente (Ferreira):", r.status_code)
        print("Erro ao tentar criar (Ferreira):", r.json())
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()['erro'], 'id ja utilizada')

    def test_108_post_ou_put_sem_nome(self):
        r_reset = requests.post('http://127.0.0.1:5000/professor/reseta')
        print("Resposta do reset:", r_reset.status_code)
        self.assertEqual(r_reset.status_code, 200)
        r = requests.post('http://127.0.0.1:5000/professor/criar', json={'id': 8})
        print("Resposta ao tentar criar professor sem nome (POST):", r.status_code)
        print("Erro ao criar professor sem nome (POST):", r.json())
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()['erro'], 'professor sem nome')
        r = requests.post('http://127.0.0.1:5000/professor/criar', json={'nome': 'maximus', 'id': 7})
        print("Resposta ao criar professor com nome válido (POST):", r.status_code)
        self.assertEqual(r.status_code, 200)
        r = requests.put('http://127.0.0.1:5000/professor/atualizar/7', json={'id': 7})
        print("Resposta ao tentar editar professor sem nome (PUT):", r.status_code)
        print("Erro ao editar professor sem nome (PUT):", r.json())
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()['erro'], 'professor sem nome')

    def test_109_nao_confundir_professor_e_aluno(self):
        r_reset = requests.post('http://127.0.0.1:5000/professor/reseta')
        print("Resposta do reset:", r_reset.status_code) 
        r = requests.post('http://127.0.0.1:5000/professor/criar', json={'nome': 'Yuri Tito', 'id': 1})
        print("Resposta ao criar professor Yuri Tito:", r.status_code)
        self.assertEqual(r.status_code, 200)
        r = requests.post('http://127.0.0.1:5000/professor/criar', json={'nome': 'Luiz Queiroz', 'id': 2})
        print("Resposta ao criar professor Luiz Queiroz:", r.status_code)
        self.assertEqual(r.status_code, 200)
        r_lista = requests.get('http://127.0.0.1:5000/professor/listar')
        print("Resposta ao listar professores:", r_lista.status_code)
        print("Quantidade de professores:", len(r_lista.json()))
        self.assertEqual(len(r_lista.json()), 2)
        r_lista_alunos = requests.get('http://127.0.0.1:5000/alunos/listar')
        print("Resposta ao listar alunos:", r_lista_alunos.status_code)
        print("Quantidade de alunos:", len(r_lista_alunos.json()))
        self.assertEqual(len(r_lista_alunos.json()), 0)'''




     
        
def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(ProfessoresTestCase)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()


#  python teste_professor.py