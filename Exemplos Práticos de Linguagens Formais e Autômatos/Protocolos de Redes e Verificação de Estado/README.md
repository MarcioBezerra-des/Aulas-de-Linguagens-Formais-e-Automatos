# **Documentação do Script: `TCPHandshakeSimulator`**

## **1. Visão Geral**

  O protocolo TCP (Transmission Control Protocol) garante uma comunicação confiável entre dois dispositivos em uma rede. Antes que a troca de dados possa começar, o cliente e o servidor devem estabelecer uma conexão através de um processo de três etapas. Este código modela esse processo de forma didática, mostrando as mudanças de estado tanto no cliente quanto no servidor a cada passo.
  A classe TCPHandshakeSimulator encapsula a lógica, os estados e as ações de um cliente e de um servidor durante o handshake, imprimindo no console cada etapa do processo.
  
## **2. Requisitos para Desenvolvimento**

* **Sistema Operacional:** Windows 11
* **Versão Python:**
* **Aplicativo utilizado:** Visual Studio

## **3. A Classe `TCPHandshakeSimulator`**
Esta classe simula a máquina de estados de um cliente e um servidor durante o estabelecimento de uma conexão TCP.

## **4. Atributos**

* `self.cliente_estado (str)`: Armazena o estado atual do cliente. Inicia como `"CLOSED"`.
* `self.servidor_estado (str)`: Armazena o estado atual do servidor. Inicia como `"LISTEN"`, indicando que está pronto para aceitar conexões.

## **5. Métodos da Classe**

## **5.1 `__init__(self)`**
* **Descrição:** O construtor da classe. Ele inicializa os estados do cliente e do servidor para seus valores iniciais padrão no processo de conexão TCP.
* **Ações:**
  * Define `self.cliente_estado` para `"CLOSED"`.
  * Define `self.servidor_estado` para `"LISTEN"`.

## **5.2 `simular(self)`**
Descrição: O método principal que orquestra a simulação completa do handshake de três vias. Ele chama os métodos auxiliares na ordem correta para simular o fluxo de pacotes.
* **Ações:**
  * Imprime uma mensagem inicial informando o começo da simulação e os estados iniciais.
  * Chama `_cliente_envia_syn()` para simular o Passo 1.
  * Chama `_servidor_recebe_syn_envia_syn_ack()` para simular o Passo 2.
  * Chama `_cliente_recebe_syn_ack_envia_ack()` para simular o Passo 3.
  * Imprime uma mensagem final confirmando que a conexão foi estabelecida com sucesso.

## **5.3 `_cliente_envia_syn(self)` (Método Privado)**
Descrição: Simula o Passo 1 do handshake. O cliente inicia a comunicação enviando um pacote SYN (Synchronize).
* **Ações:**
  * Imprime um cabeçalho para o Passo 1.
  * Informa que o cliente está enviando o pacote SYN.
  * Muda o estado do cliente de `"CLOSED"` para `"SYN_SENT"`.
  * Imprime os novos estados do cliente e do servidor.

## **5.4 `_servidor_recebe_syn_envia_syn_ack(self)` (Método Privado)**
Descrição: Simula o Passo 2 do handshake. O servidor, que estava escutando (LISTEN), recebe o SYN do cliente e responde com um pacote SYN-ACK (Synchronize-Acknowledge).
* **Ações:**
  * Imprime um cabeçalho para o Passo 2.
  * Verifica se o servidor está no estado `"LISTEN"`.
  * Informa que o servidor recebeu o pacote SYN.
  * Informa que o servidor está enviando sua resposta, o pacote SYN-ACK.
  * Muda o estado do servidor de `"LISTEN"` para `"SYN_RECEIVED"`.
  * Imprime os novos estados.

## **5.5 `_cliente_recebe_syn_ack_envia_ack(self)` (Método Privado)**
Descrição: Simula o Passo 3 e final do handshake. O cliente recebe o SYN-ACK do servidor e finaliza a conexão enviando um pacote ACK (Acknowledge).
* **Ações:**
   * Imprime um cabeçalho para o Passo 3.
   * Verifica se o cliente está no estado `"SYN_SENT"`.
   * Informa que o cliente recebeu o pacote SYN-ACK.
   * Informa que o cliente está enviando o pacote ACK final.
   * Muda o estado do cliente para `"ESTABLISHED"`.
   * Muda o estado do servidor também para `"ESTABLISHED"`, pois ao receber o ACK, o servidor também considera a conexão estabelecida.
   * Imprime os estados finais.

## **6. Execução da Simulação**
A parte final do script:

~~~py
# Executa a simulação
simulador = TCPHandshakeSimulator()
simulador.simular()
Cria uma instância da classe TCPHandshakeSimulator.
~~~
Chama o método simular() nessa instância, que dispara toda a sequência de eventos descrita acima.

## **7. Conclusão**
Este código oferece uma representação clara e passo a passo do "Three-Way Handshake" do TCP. Ao abstrair a complexidade das redes e focar nas mudanças de estado, ele serve como uma excelente ferramenta educacional para entender como as conexões TCP são iniciadas de maneira confiável, garantindo que ambos os lados estejam prontos para a comunicação antes que qualquer dado real seja transmitido.
