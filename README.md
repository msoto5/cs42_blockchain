# cs42_blockchain
El objetivo de este proyecto es crear una blockchain basada en una prueba de trabajo. Se ha implementado la lógica de la cadena de bloques, así como un servidor a través del cual se pueda interactuar con la misma.

- [blockchain.py](blockchain.py): has the implementation of the blockchain and runs the server.
- [blockchainSender.py](blockchainSender.py): interacts with the blockchain through the server by requests.post and requests.get 

## Getting started
Before running [blockchainSender.py](blockchainSender.py) or [blockchain.py](blockchain.py) the requests library has to be installed:
```bash
pip install requests
```

The server is run in port 8080 so this port has to be previously unused.

## Usage
1. Run [blockchain.py](blockchain.py)
2. At the same time run [blockchainSender.py](blockchainSender.py) in another terminal.
3. Interact with the blockchain through [blockchainSender.py](blockchainSender.py):
```
Escoge una opción:
    1.- Envía una nueva transacción para añadir al próximo bloque
    2.- Ejecuta la prueba de trabajo y crea un nuevo bloque
    3.- Devuelve la información sobre la cadena de bloques
    4.- Salir
```

- With **1**: you can create a new transaction with emisor, receptor and amount, and send it to the blockchain
- With **2**: you execute the proof of work and create the new block in the blockchain
- With **3**: the blockchain is shown in terminal
- With **4**: the programs ends