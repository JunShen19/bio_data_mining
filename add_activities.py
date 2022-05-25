from tabnanny import check
import numpy as np
import pandas as pd


def main():
    df_path = './data/dbamp_90.csv'
    label_df_path = './data/dbamp_label.csv'

    df = pd.read_csv(df_path)
    label_df = pd.read_csv(label_df_path)


    activities_list = []
    for seq in df['sequence']:

        for l_seq in label_df['sequence']:

            if seq == l_seq:
                tmp = label_df[label_df['sequence']==l_seq].head(1)
                #print(tmp['activities'].values)
                activities_list.append(tmp['activities'].values)
                break

    act_dict = {'activities' : activities_list}
    act_df = pd.DataFrame(act_dict)            
    df = df.merge(act_df, how='inner', left_index=True, right_index=True)
    df.to_csv('./data/dbamp_90_act.csv')




    return


if __name__ == "__main__":
    main()