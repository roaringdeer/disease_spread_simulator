import matplotlib.pyplot as plt


def plot(values):
    plt.grid('on')
    plt.subplot(211)
    plt.plot(values["susceptible_count"])
    plt.plot(values["infectious_count"])
    plt.plot(values["recovered_count"])
    plt.plot(values["deceased_count"])
    plt.xticks([])
    plt.subplot(212)
    plt.plot(values["free"])
    plt.plot(values["quarantined"])
    plt.plot(values["deceased_count"])
    plt.xticks(range(len(values["time"])), values["time"], rotation="vertical")
    plt.show()
