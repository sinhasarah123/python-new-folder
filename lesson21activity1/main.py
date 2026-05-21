import pandas as pd
 
examdata={'name':['ana','bob','cathy','dave'],
          'score':[85,90,78,92],
          'attempts':[1,2,3,1],
            'qualify':['yes','yes','no','yes']}
            
labels=['a','b','c','d']
df=pd.DataFrame(examdata,index=labels)
print("summary of the dataframe:")
print(df.info())
print(df)