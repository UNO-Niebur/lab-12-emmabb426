# SearchSortLab.py
# Name: Emma Barnes
# Date: 04/23/2026
# Assignment: Lab 13 – Searching and Sorting


def linearSearch(data, target):
    """Return the index of target if found, otherwise return -1."""
    for x in range(len(data)):
        if data[x] == target:
            return x

    # TODO: implement linear search
    
    return -1


def bubbleSort(data):
    """Sort the list using bubble sort and return the sorted list."""
    
    # TODO: implement bubble sort
    n = len(data)
    for x in range(n-1):
        for y in range(n-x-1):
            if data[y] > data[y+1]:
                data[y], data[y + 1] = data[y + 1], data[y]
    return data


def main():
    # Test lists
    sortedList = [1, 2, 3, 4, 5, 6, 8, 10, 12]
    reversedList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    randomList = [3, 1, 4, 2, 5, 10, 15, 6, 8, 9, 7]

    # Test linear search
    print("Search for 4 in randomList:", linearSearch(randomList, 4))
    print("Search for 18 in randomList:", linearSearch(randomList, 18))

    # Test sorting
    print("Sorted list:", bubbleSort(sortedList.copy()))
    print("Reversed list sorted:", bubbleSort(reversedList.copy()))
    print("Random list sorted:", bubbleSort(randomList.copy()))


if __name__ == "__main__":
    main()
