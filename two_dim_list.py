def main():
    NUMBER_OF_DAYS = 3
    NUMBER_OF_HOURS = 5

    # Initialize data
    data = []
    for i in range(NUMBER_OF_DAYS):
        data.append([])
        for j in range(NUMBER_OF_HOURS):
            data[i].append([])
            data[i][j].append(0) # Temperature value
            data[i][j].append(0) # Humidity value

    # Read input using input redirection from a file
    for k in range(NUMBER_OF_DAYS * NUMBER_OF_HOURS):
        line = input().strip().split()
        day = int(line[0])
        hour = int(line[1])
        temperature = float(line[2])
        humidity = float(line[3])
        data[day - 1][hour - 1][0] = temperature
        data[day - 1][hour - 1][1] = humidity

    # Find the average daily temperature and humidity
    for i in range(NUMBER_OF_DAYS):
        dailyTemperatureTotal = 0
        dailyHumidityTotal = 0
        for j in range(NUMBER_OF_HOURS):
            dailyTemperatureTotal += data[i][j][0]
            dailyHumidityTotal += data[i][j][1]

        # Display result
        print("Day " + str(i + 1) + "'s average temperature is "
            + str(dailyTemperatureTotal / NUMBER_OF_HOURS))
        print("Day " + str(i + 1) + "'s average humidity is "
            + str(dailyHumidityTotal / NUMBER_OF_HOURS))

main() # Call the main function