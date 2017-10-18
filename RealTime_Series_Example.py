##plotly.tools.set_credentials_file(username='ahmedch411',
##                                  api_key='A51EIyB82da1aaOZLQRL',
##                                  stream_ids=['nt951t6t3p',
##                                              's0qb0o2vzp',
##                                              'rsu12bcw9a',
##                                              'gmmg21y7h0'])

import numpy as np
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
import pandas as pd

import datetime
import time


stream_ids = tls.get_credentials_file()['stream_ids']
print stream_ids

# Make instance of stream id object 
stream_1 = go.Stream(
    token=stream_ids[0],  # link stream id to 'token' key
    maxpoints=80      # keep a max of 80 pts on screen
)
# Make instance of stream id object 
stream_2 = go.Stream(
    token=stream_ids[1],  # link stream id to 'token' key
    maxpoints=80      # keep a max of 80 pts on screen
)
# Make instance of stream id object 
stream_3 = go.Stream(
    token=stream_ids[2],  # link stream id to 'token' key
    maxpoints=80      # keep a max of 80 pts on screen
)
# Make instance of stream id object 
stream_4 = go.Stream(
    token=stream_ids[3],  # link stream id to 'token' key
    maxpoints=80      # keep a max of 80 pts on screen
)

# Initialize trace of streaming plot by embedding the unique stream_id
trace1 = go.Scatter(
    x=[],
    y=[],
    mode='lines',
    stream=stream_1         # (!) embed stream id, 1 per trace
)
trace2 = go.Scatter(
    x=[],
    y=[],
    mode='lines',
    stream=stream_2         # (!) embed stream id, 1 per trace
)
trace3 = go.Scatter(
    x=[],
    y=[],
    mode='markers',
    stream=stream_3         # (!) embed stream id, 1 per trace
)
trace4 = go.Scatter(
    x=[],
    y=[],
    mode='markers',
    stream=stream_4         # (!) embed stream id, 1 per trace
)


data = go.Data([trace1,trace2,trace3,trace4])

# Add title to layout object
layout = go.Layout(title='Time Series')

# Make a figure object
fig = go.Figure(data=data, layout=layout)

# Send fig to Plotly, initialize streaming plot, open new tab
py.plot(fig, filename='python-streaming')

# We will provide the stream link object the same token that's associated with the trace we wish to stream to
s1 = py.Stream(stream_ids[0])
s2 = py.Stream(stream_ids[1])
s3 = py.Stream(stream_ids[2])
s4 = py.Stream(stream_ids[3])

# We then open a connection
s1.open()
s2.open()
s3.open()
s4.open()

df = pd.read_csv("techknow_data.csv")

for i in range(0,len(df)):
    x = df.Date[i]
    y1 = df['puck1'][i]
    y2 = df['puck2'][i]
    y3 = df.msgs1[i]
    y4 = df.msgs2[i]

    print x
    print y1
    print y2
    print y3
    print y4
    
    s1.write(dict(x=x, y=y1))
    s2.write(dict(x=x, y=y2))
    s3.write(dict(x=x, y=y3))
    s4.write(dict(x=x, y=y4))
    time.sleep(0.5)  # plot a point every second
    
# Close the stream when done plotting
s1.close()
s2.close()
s3.close()
s4.close()



