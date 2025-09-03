class TCPHandshakeSimulator:
   
    def __init__(self):
        # Estados possíveis para cliente e servidor
        self.cliente_estado = "CLOSED"
        self.servidor_estado = "LISTEN"

    def simular(self):
        
        print("Iniciando simulação do TCP 3-Way Handshake...")
        print(f"Estado Inicial: Cliente='{self.cliente_estado}', Servidor='{self.servidor_estado}'\n")

        # Passo 1: Cliente envia SYN
        self._cliente_envia_syn()

        # Passo 2: Servidor recebe SYN e envia SYN-ACK
        self._servidor_recebe_syn_envia_syn_ack()

        # Passo 3: Cliente recebe SYN-ACK e envia ACK
        self._cliente_recebe_syn_ack_envia_ack()

        print("\nConexão estabelecida com sucesso!")

    def _cliente_envia_syn(self):
        print("--- Passo 1: Cliente inicia a conexão ---")
        print("Cliente: Enviando pacote SYN...")
        self.cliente_estado = "SYN_SENT"
        print(f"Novo Estado: Cliente='{self.cliente_estado}', Servidor='{self.servidor_estado}'")

    def _servidor_recebe_syn_envia_syn_ack(self):
        print("\n--- Passo 2: Servidor responde ---")
        if self.servidor_estado == "LISTEN":
            print("Servidor: Pacote SYN recebido.")
            print("Servidor: Enviando pacote SYN-ACK...")
            self.servidor_estado = "SYN_RECEIVED"
            print(f"Novo Estado: Cliente='{self.cliente_estado}', Servidor='{self.servidor_estado}'")

    def _cliente_recebe_syn_ack_envia_ack(self):
        print("\n--- Passo 3: Cliente finaliza o handshake ---")
        if self.cliente_estado == "SYN_SENT":
            print("Cliente: Pacote SYN-ACK recebido.")
            print("Cliente: Enviando pacote ACK...")
            self.cliente_estado = "ESTABLISHED"
            # O servidor também entra no estado ESTABLISHED ao receber o ACK
            self.servidor_estado = "ESTABLISHED"
            print(f"Novo Estado: Cliente='{self.cliente_estado}', Servidor='{self.servidor_estado}'")

# Executa a simulação
simulador = TCPHandshakeSimulator()
simulador.simular()