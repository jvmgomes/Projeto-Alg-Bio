# aqui é calculada a frequencia de nucleotideos do arquivo hiv1

def calculo(A, T, C, G, tamanho_arquivo):
    freq_A = A / tamanho_arquivo * 100
    freq_T = T / tamanho_arquivo * 100
    freq_C = C / tamanho_arquivo * 100
    freq_G = G / tamanho_arquivo * 100
    
    return freq_A, freq_T, freq_C, freq_G


def freq(linha, A, T, C, G):
    for letra in linha:
        match letra:
            case 'A': A += 1
            case 'T': T += 1
            case 'C': C += 1
            case 'G': G += 1
    return A, T, C, G

def leitura():
    with open('db/hiv1.fasta') as arquivo:
        A = T = C = G = 0
        tamanho_arquivo = 0
        for linha in arquivo:
            if not linha.startswith('>'):
                A, T, C, G = freq(linha, A, T, C, G)
                tamanho_arquivo += len(linha)
            
        freq_A, freq_T, freq_C, freq_G = calculo(A, T, C, G, tamanho_arquivo)
        
        print('A relação de nucleotídeos é:')
        print(f'A = {freq_A:.2f}%, T = {freq_T:.2f}%, C = {freq_C:.2f}%, G = {freq_G:.2f}%.')
        
if __name__ == "__main__":
    calculo = leitura()