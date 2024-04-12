# Pandas: Create a Tuple from two DataFrame Columns

import pandas as pd

df = pd.DataFrame({
    'first_name': ['Alice', 'Bobby', 'Carl'],
    'salary': [175.1, 180.2, 190.3],
    'experience': [10, 15, 20]
})

df['stats'] = list(zip(df['salary'], df['experience']))

#   first_name  salary  experience        stats
# 0      Alice   175.1          10  (175.1, 10)
# 1      Bobby   180.2          15  (180.2, 15)
# 2       Carl   190.3          20  (190.3, 20)
print(df)