import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd


'''
df = pd.read_csv("synch_dump.csv")
data = [go.Scatter(
          x=df.x,
          y=df.y1),
        go.Scatter(
          x=df.x,
          y=df.y2),
        go.Scatter(
          x=df.x,
          y=df.y3,
          mode = 'markers'),
        go.Scatter(
          x=df.x,
          y=df.y4,
          mode = 'markers'),
        go.Scatter(
          x=df.x,
          y=df.y5,
          mode = 'markers'),
        go.Scatter(
          x=df.x,
          y=df.y6,
          mode = 'markers')]

py.plot(data)
'''


df = pd.read_csv("techknow_data.csv")
data = [go.Scatter(
          x=df.Date,
          y=df['puck1']),
        go.Scatter(
          x=df.Date,
          y=df['puck2']),
        go.Scatter(
          x=df.Date,
          y=df.msgs1,
         mode = 'markers'),
        go.Scatter(
          x=df.Date,
          y=df.msgs2,
          mode = 'markers')]

py.plot(data)
