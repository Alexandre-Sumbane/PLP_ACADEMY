class HashMap: 
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Lista de buckets (listas vazias)

    def put(self, key, value):
        h = hash(key) % self.size  # Índice da tabela
        for pair in self.table[h]:  # Verifica se a chave já existe
            if pair[0] == key:
                pair[1] = value  # Atualiza valor
                return
        self.table[h].append([key, value])  # Adiciona novo par

    def get(self, key):
        h = hash(key) % self.size
        for pair in self.table[h]:
            if pair[0] == key:
                return pair[1]
        return None

    def __str__(self):  # Para imprimir o conteúdo do HashMap
        return str(self.table)

# Testando
hm = HashMap(10)
hm.put("name", "Alexy")
hm.put("email", "alexy@gmail.com")
hm.put("age", 22)

print(hm)
print("Nome:", hm.get("name"))
print("Idade:", hm.get("age"))
