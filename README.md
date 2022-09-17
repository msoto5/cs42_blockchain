# cs42_blockchain
The goal of this project is to create a blockchain based on proof of work. The logic of the blockchain has been implemented, as well as a server through which it can be interacted with.

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