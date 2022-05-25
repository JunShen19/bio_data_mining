import numpy as np
import pandas as pd

label_dict = {'Antibacterial':0, 'Antimicrobial':1, 'AntiHIV':2, 'Antifungal':3, 'Antiviral':4, 'Anticancer':5}


def main():
    data_path = "./data/dbamp_90_act.csv"
    df = pd.read_csv(data_path)

    act_list = []
    for act in df['activities']:
        label_list = [0, 0, 0, 0, 0, 0]
        for a in act.split(','):

            cleaned_a = a.replace('[', '').replace('"', '').replace(']', '').replace("'","").replace(' ','')

            if cleaned_a in label_dict.keys():
                label_list[label_dict[cleaned_a]] = 1

        act_list.append(label_list)


    tmp_df = pd.DataFrame(act_list, columns=['Antibacterial', 'Antimicrobial', 'AntiHIV', 'Antifungal', 'Antiviral', 'Anticancer'])
    print(tmp_df)
    df = pd.concat([df, tmp_df], axis=1)
    print(df)

    df.to_csv("./data/dbamp_90_act_label.csv")


    return


if __name__ == "__main__":
    main()