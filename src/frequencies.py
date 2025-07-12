# aqui é calculada a frequencia de nucleotideos do arquivo hiv1

def calculo(seq):
    A = seq.count('A')
    C = seq.count('C')
    G = seq.count('G')
    T = seq.count('T')
    total = A + T + C + G
    return {    
        'A': A / total * 100 if total else 0,
        'C': C / total * 100 if total else 0,
        'G': G / total * 100 if total else 0,
        'T': T / total * 100 if total else 0,
    }

def salvar_frequencias_fasta(nome_arquivo, nome_saida):
    with open(nome_arquivo) as fasta, open(nome_saida, 'a') as saida:
        seq_id = None
        seq = ''
        for linha in fasta:
            if linha.startswith('>'):
                if seq_id is not None and seq:
                    freq = calculo(seq)
                    saida.write(f'"{seq_id}",{freq['A']:.2f},{freq['C']:.2f},{freq['G']:.2f},{freq['T']:.2f}\n')
                seq_id = linha[1:].strip()
                seq = ''
            else:
                seq += linha.strip()
        if seq_id is not None and seq:
            freq = calculo(seq)
            saida.write(f'"{seq_id}",{freq['A']:.2f},{freq['C']:.2f},{freq['G']:.2f},{freq['T']:.2f}\n')
                

def leitura():
    arquivos = [
        'db/hiv1.fasta',
        'db/encephalis.fasta',
        'db/hydra.fasta',
        'db/immunodef.fasta',
        'db/immunodef2.fasta',
    ]
    with open('frequencies.csv', 'w') as saida:
        saida.write('ID,A,C,G,T\n')
    for arquivo in arquivos: 
        salvar_frequencias_fasta(arquivo, 'frequencies.csv')
                
        
if __name__ == "__main__":
    leitura()