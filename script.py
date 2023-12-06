import seaborn as sns
import pandas as pd
import numpy as np
import seaborn.objects as so

anscombe = sns.load_dataset('anscombe')
print(anscombe.head())

print(
    anscombe
    .groupby('dataset')
    .agg(['mean', 'std'])
)

(
    so.Plot(anscombe,
            x='x', y='y', color='dataset')
        .add(so.Dot())
        .facet('dataset', wrap=2)
        # .show()
        .save("./figures/plot.png", dpi=200)
)
# print(sns.__version__)