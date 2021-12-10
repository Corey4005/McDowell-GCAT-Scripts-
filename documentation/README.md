## Function 
```COUNT_SAT_BY_OWNER()``` 
```Python
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
    #get launch date for each satelite and set to index
    df['LDate'] = pd.to_datetime(df['LDate'], errors='coerce')
    df.set_index(df['LDate'], inplace=True)
    SATS_BY_DATE = df[['LDate', 'Owner']]
    
    Year = []
    Owner_Count = []
    d = {}
    
    #grab each unique year, create a dataframe representing the owner you wish to analyze. 
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
    
    #plot
    fig, ax = plt.subplots(figsize=(8,7))
    plot = ax.plot(NEW_DF)
    ax.set_title(owner + ' ' + 'GCAT Reported Sattelite Ownership Count by Year')
    ax.set_ylabel('Count')
    ax.set_xlabel('Year')
    return plot
```
## Usage
Step 1. Bring in supplementary modules and grab function from repo.
```Python 
import pandas as pd
import matplotlib.pyplot as plt
from functions import COUNT_SAT_BY_OWNER
```
Step 2. Use the function on previously imported dataframe and grab owner (in this case we use 'GSFC')
```Python
data = '.\data\satcat.csv'
DF = pd.read_csv(data, low_memory=False)
SAT = COUNT_SAT_BY_OWNER(DF, 'GSFC')
```
RETURNS [plot](/repo-images/GSFC_SATS.png)