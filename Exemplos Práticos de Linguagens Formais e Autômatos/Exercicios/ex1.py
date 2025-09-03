class Automato:
   
    def __init__(self, nome):
        self.nome = nome
        self.estados = set()
        self.alfabeto = set()
        self.estado_inicial = None
        self.estados_finais = set()

    def adicionar_estado(self, estado, final=False):
        
        self.estados.add(estado)
        if final:
            self.estados_finais.add(estado)
        print(f"Estado '{estado}' adicionado ao {self.nome}.")

    def __str__(self):
        return f"Autômato '{self.nome}' com {len(self.estados)} estado(s)."


afd = Automato("Meu AFD")
afd.adicionar_estado("q0", final=False)
afd.adicionar_estado("q1", final=True)

print(afd)