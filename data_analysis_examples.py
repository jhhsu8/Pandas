# create regression plots
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
df = pd.read_csv('/Users/johhsu/desktop/wt_change/k2p2la/all_wts.csv')
for i, group in df.groupby('Mouse'):
    sns_plot = sns.lmplot(x="Age", y="Weight", col="Mouse", data=group).set(xlim=(4,18),ylim=(15,40))

# calculate percentage change between body weights
import pandas as pd
df = pd.read_csv('/Users/johhsu/desktop/wt_change/k2p2la/all_wts.csv')
df = df.sort_values(['Mouse','Age'])
df['pct_ch'] = df.groupby(['Mouse'])['Weight'].pct_change()
df.to_csv('/Users/johhsu/desktop/wt_change/k2p2la/wts_pctchange.csv')

# calculate rsquared values
import pandas as pd
from sklearn.linear_model import LinearRegression
df = pd.read_csv('/Users/johhsu/desktop/wt_change/k2p2la/all_wts.csv')

def rsquared(df):
    x = df[['Age']]
    y = df['Weight']
    lm = LinearRegression()
    lm.fit(x, y)
    return lm.score(x,y)

rq = df.groupby('Mouse').apply(rsquared)
rq.to_csv('/Users/johhsu/desktop/csv/all_wts_rsquared.csv')

# calculate age difference
import pandas as pd
df = pd.read_csv('/Users/johhsu/desktop/wt_change/k2p2la/all_wts.csv')
df = df.sort_values(['Mouse','Age'])
df['diff'] = df.groupby(['Mouse'])['Age'].diff()
df.to_csv('/Users/johhsu/desktop/wt_change/k2p2la/all_wts_diff.csv')
