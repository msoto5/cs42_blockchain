from hashlib import sha256
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

class BloqueBlockchain:
    number_blocks = 0
    proof_bytes = 256
    prize = 1
    number_of_zeros = 1
    hash_sistema = sha256("Sistema".encode())   # Hash que será el emisor del envio al minero

    def __init__(self,hash_bloque_anterior,transacciones):
        BloqueBlockchain.number_blocks += 1
        self.index = BloqueBlockchain.number_blocks

        self.hash_bloque_anterior = hash_bloque_anterior
        self.transacciones = transacciones

        self.ts = datetime.timestamp(datetime.now())
        self.proof_of_work = ""

    def to_str(self):
        return "index: "+str(self.index)+"\ntimestamp: " + str(self.ts) + \
            "\nPrevious hash: " + str(self.hash_bloque_anterior.hexdigest()) + \
            "\n\nTransactions:\n" + "\n".join([transaccion.to_str() for transaccion \
                in self.transacciones]) + "\n\nProof of work: " + self.proof_of_work

    def block_data_with_miner_prize(self,hash_minero):
        self.transacciones.append(Transaccion(BloqueBlockchain.hash_sistema,\
            hash_minero,BloqueBlockchain.prize))
        return_str = self.to_str()
        self.transacciones = self.transacciones[:-1]
        return return_str


    def validate_proof_of_work(self,proof,hash_minero):
        
        self.transacciones.append(Transaccion(BloqueBlockchain.hash_sistema,\
                hash_minero,BloqueBlockchain.prize))

        block_data = self.to_str()
        total_data = block_data + proof
        encoded_data = total_data.encode()
        block_hash = sha256(encoded_data)
        str_block_hash = block_hash.hexdigest()

        if str_block_hash[0:BloqueBlockchain.number_of_zeros] != "0"*BloqueBlockchain.number_of_zeros:
            self.transacciones = self.transacciones[:-1]
            return False
        else:
            self.proof_of_work = proof
            self.block_hash = block_hash
            return True


class Transaccion:

    def __init__(self,hash_emisor,hash_receptor,cantidad):
        self.hash_emisor = hash_emisor
        self.hash_receptor = hash_receptor
        self.cantidad = cantidad
    
    def to_str(self):
        return "sender: "+str(self.hash_emisor.hexdigest())+", receiver: "+ \
            str(self.hash_receptor.hexdigest())+ ", amount: " + str(self.cantidad)


class Minero:

    def __init__(self,hash_minero):
        self.hash_minero = hash_minero


    def proof_of_work(self,block):
        block_data = block.block_data_with_miner_prize(self.hash_minero)
        
        number = 0
        number_str = str(number).zfill(BloqueBlockchain.proof_bytes)

        total_data = block_data + number_str
        encoded_data = total_data.encode()
        block_hash = sha256(encoded_data)
        str_block_hash = block_hash.hexdigest()

        while(str_block_hash[0:BloqueBlockchain.number_of_zeros] != "0"*BloqueBlockchain.number_of_zeros):
            number += 1

            number_str = str(number).zfill(BloqueBlockchain.proof_bytes)

            total_data = block_data + number_str
            encoded_data = total_data.encode()
            block_hash = sha256(encoded_data)
            str_block_hash = block_hash.hexdigest()
        
        return number_str


class Listener(BaseHTTPRequestHandler):
    def do_GET(self):
        global blockchain 
        global transacciones

        if "/mine" == self.path:
            if transacciones:
                if blockchain:
                    ultimo_bloque = BloqueBlockchain(blockchain[-1].block_hash,transacciones)
                else:
                    ultimo_bloque = BloqueBlockchain(sha256("Initial Block".encode()),transacciones)
                minero = Minero(sha256("Miguel".encode()))
                proof = minero.proof_of_work(ultimo_bloque)
                if ultimo_bloque.validate_proof_of_work(proof,minero.hash_minero):
                    transacciones = []
                    blockchain.append(ultimo_bloque)
                    self.send_response(200)
                    self.end_headers()
                else:
                    self.send_response(400)  
                    self.end_headers()
            else:
                self.send_response(400)
                self.end_headers()

        elif "/chain" == self.path:
            self.send_response(200)
            self.send_header("Content-type", "text/str")
            self.end_headers()
            self.wfile.write(bytes("\n\nNew Block:\n\n".join(block.to_str() for block in blockchain), "utf-8"))
        else:
            print("Error")
            self.send_response(404)
            self.end_headers()

    def do_POST(self):

        if "/transactions/new" == self.path:
            
            sender = sha256(self.headers.get("Sender").encode())
            receiver = sha256(self.headers.get("Receiver").encode())
            amount = int(self.headers.get("Amount"))
            transacciones.append(Transaccion(sender,receiver,amount))
            self.send_response(200)
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()


hostName = "localhost"
serverPort = 8080

blockchain = []
transacciones = []
webServer = HTTPServer((hostName, serverPort), Listener)
print("Server started http://%s:%s" % (hostName, serverPort))

try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass

webServer.server_close()
print("Server stopped.")

