numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]


def find_min(numbers):
    """Returns the smallest value."""
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


def find_max(numbers):
    """Returns the largest value."""
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


def search(numbers, target):
    """Returns the index of target, or -1 if not found."""
    index = 0
    for num in numbers:
        if num == target:
            return index
        index += 1
    return -1


def bubble_sort(numbers):
    """Returns a new sorted list"""
    sorted_numbers = numbers.copy()
    n = len(sorted_numbers)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                sorted_numbers[j], sorted_numbers[j + 1] = sorted_numbers[j + 1], sorted_numbers[j]
    return sorted_numbers


def show_menu():
    """Shows the menu options and returns the user's choice."""
    print("\n=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search")
    print("4. Sort")
    print("5. Quit")
    answer = input("Enter a choice (1-5): ")
    return answer


def main():
    while True:
        choice = show_menu()

        if choice == '1':
            print(f"\nSmallest Number: {find_min(numbers)}\n")

        elif choice == '2':
            print(f"\nLargest Number: {find_max(numbers)}\n")

        elif choice == '3':
            target = int(input("Enter a number to search for: "))
            result = search(numbers, target)
            if result != -1:
                print(f"Found {target} at index {result}.")
            else:
                print(f"{target} was not found in the list.")

        elif choice == '4':
            sorted_list = bubble_sort(numbers)
            print(f"The sorted list is: {sorted_list}")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()