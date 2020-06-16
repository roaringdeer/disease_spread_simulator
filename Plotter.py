import matplotlib.pyplot as plt


def plot(scenarioCounter, values):

    sim_name = ['Scenario 1', 'Scenario 2', 'Scenario 3', 'Scenario 4', 'Scenario 5', 'Scenario 6', 'Scenario 7', 'Scenario 8']

    plt.grid('on')
    plt.subplot(211)
    s, = plt.plot(values["susceptible_count"], label='Susceptible')
    i, = plt.plot(values["infectious_count"], label='Infectious')
    d, = plt.plot(values["recovered_count"], label='Recovered')
    r, = plt.plot(values["deceased_count"], label='Deceased')
    plt.xticks([])
    plt.title(sim_name[scenarioCounter])

    plt.annotate(str(max(values["susceptible_count"])), xy=(
        values["susceptible_count"].index(max(values["susceptible_count"])), max(values["susceptible_count"])),
                 xytext=(0, 15), textcoords='offset pixels')
    plt.annotate(str(values["susceptible_count"][-1]),
                 xy=(values["susceptible_count"][-1], values["susceptible_count"][-1]), xytext=(-10, 15),
                 textcoords='offset pixels')

    plt.annotate(str(max(values["infectious_count"])), xy=(
        values["infectious_count"].index(max(values["infectious_count"])), max(values["infectious_count"])),
                 xytext=(0, 15), textcoords='offset pixels')
    plt.annotate(str(values["infectious_count"][-1]),
                 xy=(values["infectious_count"][-1], values["infectious_count"][-1]), xytext=(-10, 15),
                 textcoords='offset pixels')

    plt.annotate(str(max(values["recovered_count"])), xy=(
        values["recovered_count"].index(max(values["recovered_count"])), max(values["recovered_count"])),
                 xytext=(0, 15), textcoords='offset pixels')
    plt.annotate(str(values["recovered_count"][-1]),
                 xy=(values["recovered_count"][-1], values["recovered_count"][-1]), xytext=(-10, 15),
                 textcoords='offset pixels')

    plt.annotate(str(max(values["deceased_count"])), xy=(
        values["deceased_count"].index(max(values["deceased_count"])), max(values["deceased_count"])),
                 xytext=(0, 15), textcoords='offset pixels')
    plt.annotate(str(values["deceased_count"][-1]),
                 xy=(values["deceased_count"][-1], values["deceased_count"][-1]), xytext=(-10, 15),
                 textcoords='offset pixels')

    plt.legend(handles = [s, i, d, r])
    plt.subplot(212)
    f, = plt.plot(values["free"], label = 'Free')
    q, = plt.plot(values["quarantined"], label = 'Quarantined')
    plt.xticks(range(int(len(values["time"])/24)), values["time"], rotation="vertical")
    plt.legend(handles=[f, q])
    plt.show()
