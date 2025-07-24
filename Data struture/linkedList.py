# Classe que representa um nó da lista
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Classe da Lista Encadeada
class LinkedList:
    def __init__(self):
        self.head = None

    # Adicionar elemento no início (cabeça)
    def insert_front(self, data):
        new_node = Node(data)          # Cria novo nó
        new_node.next = self.head      # Aponta para o antigo primeiro nó
        self.head = new_node           # Atualiza a cabeça para o novo nó

    # Imprimir a lista
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

# Bloco principal, executado somente se rodar este arquivo diretamente
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_front(30)
    ll.insert_front(20)
    ll.insert_front(10)

    ll.print_list()

#Doubly LinkedList

class DNode: 
    def __init__(self, data):
        self.data = data #Value stored in the node
        self.prev = None # pointer to the previous node
        self.next= None


#Node holds
# - Data = value (e.g 10, aple, x)
# - Next = pointer that points to the next Node in the list

# Example 
# [10/ Next] --> [20/next] --> [30/ next] -- None

# class LinkedList:
#     def __init__(self):
#         self.head =  # Start of the list   

