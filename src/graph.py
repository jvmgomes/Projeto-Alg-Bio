import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('frequencies.csv')

df.set_index('ID')[['A','C','G','T']].plot(kind='bar')
plt.ylabel('Frequência (%)')
plt.title('Frequência relativa dos nucleotídeos de cada sequência')
plt.legend(title='Nucleotídeo')
plt.tight_layout()
plt.show()