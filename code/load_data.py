"""
Load training data into dataframes.
"""

import pandas as pd

class LoadData(object):
    """A class to load and hold the training data.
    """
    def __init__(self,
                 A375_expression_path='CMap_Drug_Safety_2019/data/gct/chunked_data/A375_expression.csv',
                 A375_info_path='CMap_Drug_Safety_2019/data/gct/chunked_data/A375_info.csv',
                 A549_path='CMap_Drug_Safety_2019/data/gct/chunked_data/A549_cultures_data.csv',
                 ASC_path='CMap_Drug_Safety_2019/data/gct/chunked_data/ASC_cultures_data.csv',
                 HA1E_path='CMap_Drug_Safety_2019/data/gct/chunked_data/HA1E_cultures_data.csv',
                 HCC515_path='CMap_Drug_Safety_2019/data/gct/chunked_data/HCC515_cultures_data.csv',
                 HEPG2_path='CMap_Drug_Safety_2019/data/gct/chunked_data/HEPG2_cultures_data.csv',
                 HT29_path='CMap_Drug_Safety_2019/data/gct/chunked_data/HT29_cultures_data.csv',
                 MCF7_path='CMap_Drug_Safety_2019/data/gct/chunked_data/MCF7_cultures_data.csv',
                 NPC_path='CMap_Drug_Safety_2019/data/gct/chunked_data/NPC_cultures_data.csv',
                 PC3_path='CMap_Drug_Safety_2019/data/gct/chunked_data/PC3_cultures_data.csv',
                 PHH_path='CMap_Drug_Safety_2019/data/gct/chunked_data/PHH_cultures_data.csv',
                 SKB_path='CMap_Drug_Safety_2019/data/gct/chunked_data/SKB_cultures_data.csv',
                 VCAP_path='CMap_Drug_Safety_2019/data/gct/chunked_data/VCAP_cultures_data.csv'):


        #don't think we want to preprocess data, so all of these are filled in raw
        self.A375_expression = pd.read_csv(A375_expression_path, index_col=0)
        self.A375_info = pd.read_csv(A375_info_path, index_col=0)
        self.A549 = pd.read_csv(A549_path, index_col=0)
        self.ASC = pd.read_csv(ASC_path, index_col=0)
        self.HA1E = pd.read_csv(HA1E_path, index_col=0)
        self.HCC515 = pd.read_csv(HCC515_path, index_col=0)
        self.HEPG2 = pd.read_csv(HEPG2_path, index_col=0)
        self.HT29 = pd.read_csv(HT29_path, index_col=0)
        self.MCF7 = pd.read_csv(MCF7_path, index_col=0)
        self.NPC = pd.read_csv(NPC_path, index_col=0)
        self.PC3 = pd.read_csv(PC3_path, index_col=0)
        self.PHH = pd.read_csv(PHH_path, index_col=0)
        self.SKB = pd.read_csv(SKB_path, index_col=0)
        self.VCAP = pd.read_csv(VCAP_path, index_col=0)

        #aligning below w/correct labels for CMAP
        self.A375_expression = self.preprocess(
            pd.read_csv(A375_expression_path, index_col=0)
        )
        self.A375_info = pd.read_csv(A375_info_path, index_col=0)



        # create training labels for if a sample has been mislabeled
        self.mislabel_labels = []
        for i in range(0, len(self.mislabel.index)):
            if self.mislabel.iloc[i, 0] == self.mislabel.iloc[i, 1] and self.mislabel.iloc[i, 1] == self.mislabel.iloc[i, 2]:
                self.mislabel_labels.append(0)
            else:
                self.mislabel_labels.append(1)


    def preprocess(self, df):
        return self.normalize(self.fix_data(df))

    def normalize(self, df):
        """Normalize each column into roughly [-1.0, 1.0] centered around 0.0.

        Arguments:
            df {pandas.DataFrame} -- The data to normalize. Each column
                must be quantitative.

        Returns:
            pandas.DataFrame -- The normalized data.
        """
        return (df - df.mean()) / (df.max() - df.min())

    def fix_data(self, df):
        """Preprocess dataframe to fill NaNs with 0s and remove bad
        columns.

        Arguments:
            df {pandas.DataFrame} -- DataFrame to be processed.

        Returns:
            pandas.DataFrame -- Processed dataframe. Note that some columns
                may be removed.
        """
        return df.dropna(axis='columns', how='all').fillna(0.0)

if __name__ == "__main__":
    data = LoadData()
    #print(data.rna)
