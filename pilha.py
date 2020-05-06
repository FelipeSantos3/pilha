class pilha:
    def __init__(self,tam):
        self.topo=-1
        self.tamanho=tam
        self.elementos=[]

    def empilhar(self,x):
        self.topo+=1
        self.elementos.append(x)

    def desempilhar(self):
        temp=self.elementos[self.topo]
        self.topo-=1
        self.elementos.pop()
        return temp

    def elementodotopo(self):
        return self.elementos[self.topo]

    def pilhacheia(self):
        return self.topo==self.tamanho-1

    def pilhavazia(self):
        return self.topo==-1
    
    def mostrapilha(self):
        print(self.elementos)