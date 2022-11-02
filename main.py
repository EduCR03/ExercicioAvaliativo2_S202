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
'''
def LetraB1(teacher):
    aux = db.execute_query('MATCH (t:Teacher) WHERE t.name =~ {name:$name} RETURN t.name, t.cpf', 
                            {'name':teacher['name']})
    wj(aux, '1B')
    return aux 

name = '^M.*$'
professor1 = {
    'name':name
}
res = LetraB1(professor1)
pp(res)
'''
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
def LetraA2_Novo():
    aux = db.execute_query('MATCH (c:City) ')
    wj(aux, '2A')
    return aux

res1 = LetraA2_Novo()
pp(res1)


#wj(aux, '2B')

# C

#wj(aux, '2C')

# D

#wj(aux, '2D')

# Questão 03
# A

# B

# C

# D

