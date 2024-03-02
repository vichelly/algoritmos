#vamos reproduzir isso:
sequencial = []
sequencial.append(7)


from node_alocacaoEncadeada import Node

class LinedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self,elem):
        if self.head:
            #inserção quando a lista já possui elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)

        else:
            #primeira inserção
            self.head = Node(elem)
        self._size = self.size +1

    def __len__(self):
        """retorna o tamanho da lista"""
        return self._size
    
    def get(self, index):
        pass

    def set(self, index, elem):
        pass

    def __getitem__(self, index):
        # a = lista[6]
        pass

    def __setitem__(self, item, elem):
        # lista[5] = 9


listaex = LinedList()

print("primeiro print: ",listaex.size)

listaex.append(89)

print("segundo print: ",listaex.size)

listaex.append(90)

print("terceiro print: ",listaex.size)