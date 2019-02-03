import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
web_status = {'Day':[1,2,3,4,5,6],
              'Visitors':[45,51,61,34,52,34],
              'Bounce rate':[65,72,62,64,54,66]}

df = pd.DataFrame(web_status)
df = df.set_index('Day')
print(df)
