# from pprintpp import pprint as pp
from db.database import Graph
from helper.write_a_json import write_a_json as wj
from pprintpp import pprint as pp

db = Graph(uri='bolt://3.239.219.127:7687 ', user='neo4j', password='tides-toolboxes-knife')

# Questão 01
def LetraA1(teacher):
    aux = db.execute_query('MATCH (t:Teacher{name:$name}) RETURN t.ano_nasc, t.cpf',
                            {'name':teacher['name']})
    wj(aux, '1A')
    return aux

name = 'Renzo'
professor = {
    'name': name
}

res = LetraA1(professor)
pp(res)
print('')
# B

def LetraB1():
    aux = db.execute_query("MATCH(t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name, t.cpf")
    wj(aux, '1B')
    return aux 

res = LetraB1()
pp(res)

# C
def LetraC1():
    aux = db.execute_query('MATCH (c:City) RETURN c')
    wj(aux, '1C')
    return aux

res = LetraC1()
pp(res)
print('')
# D
def LetraD1():
    aux = db.execute_query('MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name, s.address, s.number')
    wj(aux, '1D')
    return aux

res = LetraD1()
pp(res)

# Questão 02
# A
def LetraA2_Novo():
    aux = db.execute_query('MATCH (t:Teacher) RETURN t.ano_nasc ORDER BY t.ano_nasc DESC LIMIT 1 ')
    wj(aux, '2A')
    return aux

def LetraA2_Velho():
    aux = db.execute_query('MATCH (t:Teacher) RETURN t.ano_nasc ORDER BY t.ano_nasc LIMIT 1 ')
    wj(aux, '2A')
    return aux

res1 = LetraA2_Novo()
pp(res1)

res2 = LetraA2_Velho()
pp(res2)

print('')
# B

def LetraB2():
    aux = db.execute_query("MATCH(c:City) RETURN AVG(c.population)")
    wj(aux, '2B')
    return aux

res1 = LetraB2()
pp(res1)
print('')
# C
def LetraC2():
    aux = db.execute_query("MATCH(c:City) WHERE c.cep = '37540-000' RETURN REPLACE(c.name, 'a', 'A')")
    wj(aux, '2C')
    return aux

res = LetraC2()
pp(res)

# D
def LetraD2():
    aux = db.execute_query("MATCH(p:Teacher) RETURN SUBSTRING(p.name, 3, 1)")
    wj(aux, '2D')
    return aux

res = LetraD2()
pp(res)

# Questão 03
class TeacherCRUD():
# A
    def create(self, person):
        aux = self.db.execute_query('CREATE (n:Person {name:$name, ano_nasc:$ano_nasc, cpf:$cpf}) return n',
                                     {'name': person['name'], 'ano_nasc': person['ano_nasc'], 'cpf':person['cpf']})
        wj(aux, '3A')
        return aux

    def read_by_name(self, person):
        aux = self.db.execute_query('MATCH (n:Person {name:$name}) RETURN n',
                                     {'name': person['name']})
        wj(aux, '3B')
        return aux

    def delete(self, person):
        aux = self.db.execute_query('MATCH (n:Person {name:$name}) DELETE n',
                                     {'name': person['name']})
        wj(aux, '3C')
        return aux

    def update_cpf(self, person):
        aux = self.db.execute_query('MATCH (t:Teacher {name:$name}) SET t.cpf = $cpf RETURN t',
                                     {'name': person['name'], 'cpf': person['cpf'] })
        wj(aux, '3D')
        return aux
# B
crud = TeacherCRUD()
name = 'Chris Lima',
ano_nasc = 1956,
cpf = '189.052.396-66'
professor = {
    name: name,
    ano_nasc:ano_nasc,
    cpf: cpf
}

aux = crud.create(professor)
pp(aux)
# C
name = 'Chris Lima',
cpf = '162.052.777-77'
professor = {
    name: name,
    cpf: cpf
}

aux = crud.create(professor)
pp(aux)

# D

