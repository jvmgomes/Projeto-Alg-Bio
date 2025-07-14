import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('frequencies.csv')
df['Abbreviated_ID'] = df['ID'].apply(lambda x: x.split()[0])

df.set_index('Abbreviated_ID')[['A','C','G','T']].plot(kind='bar')
plt.ylabel('Frequência (%)')
plt.title('Frequência relativa dos nucleotídeos de cada sequência')
plt.legend(title='Nucleotídeo')
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.tight_layout()
plt.show()