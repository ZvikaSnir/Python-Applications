from bokeh.plotting import figure, output_file, show
import pandas

df=pandas.read_excel("data.xlsx",sheetname=0)
df["Temperature"]/=10
df["Pressure"]/=10

p=figure(plot_width=500,plot_height=400,tools='pan,resize',logo=None)

p.title.text="Temp vs Air Pressure"
p.xaxis.axis_label="Temperature"
p.yaxis.axis_label="Pressure"

p.circle(df["Temperature"],df["Pressure"],size=0.5)
output_file("Temp.html")
show(p)
