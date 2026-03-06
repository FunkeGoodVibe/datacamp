
# 0) Introduction
import plotly.express as px 
import pandas as pd
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]       

temperatures = [11, 3, 45, 34, 22, -3, 8]

fig = px.bar(
                x=days, 
                y=temperatures, 
                title="Temperatures of the week")

fig.show()



# 1) create_bar_chart

import plotly.express as px 

# Define the x and y axis columns
x_column = "month"
y_column = "sales"

# Define the chart title
chart_title = "Sales for Jan-Mar 2025"

# Create a bar plot
fig = px.bar(
            data_frame=monthly_sales, 
            x=x_column, 
            y=y_column, 
            title=chart_title)

fig.show()




# 3) Histogram 
#https://campus.datacamp.com/courses/introduction-to-data-visualization-with-plotly-in-python/introduction-to-plotly-1?ex=4

import plotly.express as px 
import pandas as pd 

penguins = pd.DataFrame(data)

fig = px.histogram(
                data_frame=penguins, 
                x = "Body Mass (g)",
                nbins = 10)

fig.show()


# 4) Student bar chart 
#https://campus.datacamp.com/courses/introduction-to-data-visualization-with-plotly-in-python/introduction-to-plotly-1?ex=5

"""
  student_name  score
0         John     80
1        Julia     97
2         Xuan     90
3        Harry     85

"""

#Examine the head of the student_scores DataFrame that has been printed for you.
#Create a bar plot, setting the y-axis to be the score and the x-axis to be the student name.
#Add a title to the plot: call it "Student Scores by Student".

import plotly.express as px  

# Create the bar plot
fig = px.bar(data_frame=student_scores, 
             x="student_name", 
             y="score", 
             title="Student Scores by Student")

# Show the plot
fig.show()
