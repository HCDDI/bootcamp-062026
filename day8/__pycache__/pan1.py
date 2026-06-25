import pandas as pd
students={
    "name": ["Alice", "Bob", "Charlie"],
    "age": [20, 21, 19],
    "grade": ["A", "B", "C"]
}  
dframe=pd.DataFrame(students)
#piprint(dframe)
print(dframe["grade"])