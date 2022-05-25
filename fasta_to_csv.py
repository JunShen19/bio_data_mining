import numpy as np
import pandas as pd


def main():
    file_path = f'./data/cdhit/dbamp_90.fasta'
    #id_list = []
    seq_list = []
    with open(file_path, 'r') as f:
        while True:
            line1 = f.readline()
            line2 = f.readline()
            if not line1:
                break
            #id_list.append(line1)
            seq_list.append(line2)

    id = []
    seq = []
    seq_len = []
    '''
    for i in id_list:
        i = i.replace('>', '')
        i = i.replace('\n', '')
        id.append(i)
    '''
        
    for j in seq_list:
        seq.append(j.replace('\n', ''))
        seq_len.append(len(j.replace('\n', '')))
    #print(seq)

    data_dict = {'sequence': seq, 'length':seq_len}
    df = pd.DataFrame(data_dict)
    print(df)
    df.to_csv(f'./data/dbamp_90.csv')

    return


if __name__ == "__main__":
    main()