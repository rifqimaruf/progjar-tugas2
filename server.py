import socket
import threading
import logging
from datetime import datetime

class ClientThread(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        logging.info(f"Thread untuk {self.address} dimulai.")
        try:
            while True:
                # Menerima data dari client
                data = self.connection.recv(1024)
                if not data:
                    break  

        
                command = data.decode('utf-8').strip()
                logging.info(f"[{self.address}] Menerima: '{command}'")

                if command == "TIME":
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    response = f"JAM {current_time}\r\n"
                    self.connection.sendall(response.encode('utf-8'))
                    logging.info(f"[{self.address}] Mengirim: {response.strip()}")
                
                elif command == "QUIT":
                    break 

                else:
                    response = "Perintah tidak valid. Gunakan TIME atau QUIT.\r\n"
                    self.connection.sendall(response.encode('utf-8'))

        except Exception as e:
            logging.error(f"Error pada koneksi {self.address}: {e}")
        finally:
            logging.warning(f"Koneksi dengan {self.address} ditutup.")
            self.connection.close()


class TimeServer(threading.Thread):
    def __init__(self, port):
        self.port = port
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('0.0.0.0', self.port))
        self.my_socket.listen(5)
        logging.info(f"Server berjalan di port {self.port}, siap menerima koneksi...")

        while True:
            # Terima koneksi baru
            connection, client_address = self.my_socket.accept()
            logging.warning(f"Koneksi baru dari {client_address}")

            # Buat thread baru untuk client ini
            client_handler = ClientThread(connection, client_address)
            client_handler.start()
            self.the_clients.append(client_handler)
            logging.info(f"Jumlah koneksi aktif: {threading.active_count() - 2}") 

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    server = TimeServer(45000)
    server.start()

if __name__ == "__main__":
    main()