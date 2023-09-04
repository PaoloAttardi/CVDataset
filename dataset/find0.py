import os

# Definisci la cartella in cui si trovano i file TXT
cartella_input = 'C:/Users/sghe9/Desktop/dataset/train/labels'

# Definisci la cartella di destinazione dei file trovati
cartella_output = 'C:/Users/sghe9/Desktop/dataset/train/labels_mod'

# Crea la cartella di destinazione se non esiste già
if not os.path.exists(cartella_output):
    os.makedirs(cartella_output)

# Elencare tutti i file nella cartella di origine con estensione .txt
elenco_file = [f for f in os.listdir(cartella_input) if f.endswith('.txt')]

# Cicla attraverso i file nella lista
for nome_file in elenco_file:
    # Crea il percorso completo del file di origine
    percorso_file_input = os.path.join(cartella_input, nome_file)
    
    # Apri il file di origine in modalità lettura
    with open(percorso_file_input, 'r') as file:

        # Leggi il file riga per riga
        for riga in file:
            # Suddividi la riga in una lista di numeri float utilizzando gli spazi come separatore
            valori = [float(valore) for valore in riga.split()]
            
            # Assicurati che il primo numero sia un intero
            valori[0] = int(valori[0])
            
            # Check se il primo numero della riga è 0
            if valori[0] == 0:
                file.close()
                # Crea il percorso per il file nella cartella di destinazione
                percorso_file_output = os.path.join(cartella_output, nome_file)
                # Sposta il file nella cartella di destinazione
                os.rename(percorso_file_input,percorso_file_output)
                print(f"File '{nome_file}' spostato.")
                break



    

