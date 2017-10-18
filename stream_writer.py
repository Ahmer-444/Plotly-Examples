import numpy as np
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go


stream_ids = tls.get_credentials_file()['stream_ids']
print stream_ids

# Get stream id from stream id list 
stream_id = stream_ids[0]

# We will provide the stream link object the same token that's associated with the trace we wish to stream to
s = py.Stream(stream_id)

# We then open a connection
s.open()

# (*) Import module keep track and format current time
import datetime
import time

i = 0    # a counter
k = 5    # some shape parameter

# Delay start of stream by 5 sec (time to switch tabs)
time.sleep(5)

while True:

    #, random numbers on y-axis
    x_data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    y_data = (np.cos(k*i/50.)*np.cos(i/50.)+np.random.randn(1))[0]

    # Send data to your plot
    data = {'x':x_data,'y':y_data}
    s.write(data)

    #     Write numbers to stream to append current data on plot,
    #     write lists to overwrite existing data on plot

    time.sleep(1)  # plot a point every second    
# Close the stream when done plotting
s.close()

# Embed never-ending time series streaming plot
tls.embed('streaming-demos','12')
