from Search import execution_time_gathering

if __name__ == "__main__":
    minimum_size = 1000000
    maximum_size = 10000000
    step = 1000000
    samples_by_size = 7

    table = execution_time_gathering.take_execution_time(
        minimum_size, maximum_size, step, samples_by_size
    )

    print("Size | LinealSearch | Search In | Binary Search | Ternary Search")
    for row in table:
        print(row)
