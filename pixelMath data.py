import pandas as pd
import plotly.express as px

df = pd.read_csv("C:\\Users\\Dhairya\\Desktop\\python\\c 107\\project\\c 107 project\\data.csv")
fig = px.scatter(df, x="student_id", y="level", color="attempt")

fig.show()

print("opening")