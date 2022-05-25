import numpy as np
import pandas as pd

def main():
    path = "./data/dbamp_raw.csv"
    df = pd.read_csv(path)

    seq = df['sequence']


    with open("./data/dbamp_raw.fasta", 'a') as f:
        for i in range(len(seq)):
            f.write('>'+str(i)+'\n')
            f.write(str(seq[i])+'\n')


    return


if __name__ == '__main__':
    main()