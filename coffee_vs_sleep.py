import plotly.express as px
import csv

with open("cups_of_coffee_vs_hours_of_sleep.csv") as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
    fig.show()