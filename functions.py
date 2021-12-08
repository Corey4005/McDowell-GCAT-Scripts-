# this module will contain the functions developed for analysis of GCAT

#importing other packages for testing
import pandas as pd
import matplotlib.pyplot as plt

#filepath for test
data = '.\data\satcat.csv'
DF = pd.read_csv(data, low_memory=False)

def COUNT_SAT_BY_OWNER(df, owner):
    """
    

    Parameters
    ----------
    df : Pandas DataFrame
        Dataframe containing the satcat data.
    owner : STR
        Owner code. Codes listed 

    Returns
    -------
    PLOT : matplotlib plot
        Takes in dataframe for satcat and looks for all rows representing 
        owner str and returns a plot of sattelites they maintained over time.

    """
    df['LDate'] = pd.to_datetime(df['LDate'], errors='coerce')
    df.set_index(df['LDate'], inplace=True)
    SATS_BY_DATE = df[['LDate', 'Owner']]
    
    Year = []
    Owner_Count = []
    d = {}
    for i in SATS_BY_DATE.index.year.unique():
        DF = SATS_BY_DATE[SATS_BY_DATE.index.year == i]
        OWNER = DF[DF['Owner'] == owner]
        COUNT = OWNER.shape[0]
        Year.append(i)
        Owner_Count.append(COUNT)
    
    d[owner] = {'Year': Year, 'Count': Owner_Count}
    NEW_DF = pd.DataFrame(d[owner])
    NEW_DF.set_index('Year', inplace=True)
    NEW_DF.sort_index(inplace=True)
    
    fig, ax = plt.subplots(figsize=(8,7))
    plot = ax.plot(NEW_DF)
    ax.set_title(owner + ' ' + 'GCAT Reported Sattelite Ownership Count by Year')
    ax.set_ylabel('Count')
    ax.set_xlabel('Year')
    return plot
