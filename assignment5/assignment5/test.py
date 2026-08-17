import altair as alt
from vega_datasets import data
import pandas as pd





df = pd.DataFrame({'x': [1, 2, 3],
                     'y': [3, 1, 4]})

chart = alt.Chart(df).mark_point().encode(
    x='x:Q',
    y='y:Q',
    color='color:Q'  # <-- this field does not exist in the data!
    )

chart.show()
