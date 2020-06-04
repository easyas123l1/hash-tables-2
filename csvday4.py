"""
Read the CSV file
Build various indexes
* What are all the city names in a particular state
Have a repl to query cities per state
"""
import csv

cities_per_state = {}
states_per_city = {}

population_buckets = {}


def read_csv_data():
    with open('cities.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['state_id'] not in cities_per_state:
                cities_per_state[row['state_id']] = []
            cities_per_state[row['state_id']].append(row['city'])

            if row['city'] not in states_per_city:
                states_per_city[row['city']] = []
            states_per_city[row['city']].append(row['state_id'])

            population = int(float(row['population']))
            city_info = f"{row['city']} {row['state_id']} ({population})"

            if population < 10:
                population_buckets[10].append(city_info)
            elif population < 100:
                population_buckets[100].append(city_info)
            elif population < 1000:
                population_buckets[1000].append(city_info)
            elif population < 10000:
                population_buckets[10000].append(city_info)
            elif population < 100000:
                population_buckets[100000].append(city_info)
            elif population < 1000000:
                population_buckets[1000000].append(city_info)
            elif population < 10000000:
                population_buckets[10000000].append(city_info)
            elif population < 100000000:
                population_buckets[100000000].append(city_info)


def main():
    read_csv_data()

    population_buckets[10] = []
    population_buckets[100] = []
    population_buckets[1000] = []
    population_buckets[10000] = []
    population_buckets[100000] = []
    population_buckets[1000000] = []
    population_buckets[10000000] = []
    population_buckets[100000000] = []

    while True:
        state_id = input("Enter a state: ")
        print(states_per_city[state_id])


if __name__ == "__main__":
    main()
