def write_to_file(file_name, data):
    f = open(file_name, "w+")
    for i in range(len(data["time"])):
        f.write("{},{},{},{},{},{},{},{},{}\n".format(
            data["time"][i],
            data["susceptible_count"][i],
            data["infectious_count"][i],
            data["recovered_count"][i],
            data["deceased_count"][i],
            data["free"][i],
            data["quarantined"][i],
            data["param_hygiene"][i],
            data["param_quarantine_prob"][i]
        ))
    f.close()
