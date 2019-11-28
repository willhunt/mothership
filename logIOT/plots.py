from django.shortcuts import get_object_or_404
from .model import Channel


def plotChannelData(request, channel_id):
    ''' Plot data '''
    #import matplotlib
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.dates import DateFormatter

    fig = Figure()
    axes = fig.add_subplot(1,1,1)

    channel = get_object_or_404(Channel, pk=channel_id)
    x_data = [0, 2, 4, 6, 8, 10]
    y_data = x_data**2


