import socket
import logging

def run_client():
    server_address = ('172.16.16.101', 45000)
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Menghubungkan soket ke port tempat server mendengarkan
        logging.info(f"Menghubungkan ke server di {server_address[0]} port {server_address[1]}")
        sock.connect(server_address)

        # Loop untuk mengirim perintah ke server
        while True:
            message = input("Ketik 'TIME' untuk meminta waktu, atau 'QUIT' untuk keluar: ").upper()

            if not message:
                continue
            
            # Pesan di-encode ke UTF-8 dan diakhiri dengan '\r\n' sesuai protokol yang ditentukan.
            logging.info(f"Mengirim perintah: '{message}'")
            sock.sendall(f"{message}\r\n".encode('utf-8'))

            # Jika perintahnya adalah 'QUIT', keluar dari loop setelah mengirim
            if message == 'QUIT':
                logging.info("Perintah QUIT dikirim, memutuskan koneksi.")
                break
            
            response = sock.recv(1024)
            print(f"\nJawaban dari Server: {response.decode('utf-8').strip()}\n")
    
    except ConnectionRefusedError:
        logging.error("Koneksi ditolak. Pastikan server sudah berjalan dan alamat/port sudah benar.")
    except Exception as e:
        logging.error(f"Terjadi error: {e}")
    finally:
        logging.info("Menutup koneksi soket.")
        sock.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    run_client()