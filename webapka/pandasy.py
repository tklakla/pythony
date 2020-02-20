# import pandas as pd
# s = {"col1": [1, 2], "col2": [3, 4]}
# df = pd.DataFrame(s)
# OutputDataSet = df
# print(3+4)
# print(OutputDataSet)

# c = 1/2
# d = 1*2
# s = pd.Series([c,d])
# df = pd.DataFrame(s)
# OutputDataSet = df

#input_data_1_name = 'MyInput'
#input_data_1 =
#SELECT 1 AS foo, 2 AS bar

# liczby = [1, 2, 3, 4, 5]
# potegi_dwojki = [2**n for n in liczby]
# print(potegi_dwojki)

#print((lambda x: x*21) (8))

collapse = "kla"
s = "this   is\na\ttest"
#print(s)
#print(s.split())
#print(" ".join(s.split()))
processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
print(processFunc(s))
