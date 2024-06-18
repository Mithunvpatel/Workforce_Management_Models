class IntervalSet:
    def __init__(self):
        self.intervals = []

    def add_interval(self, start, end):
        self.intervals.append((start, end))

    def remove_interval(self, start, end):
        self.intervals = [(s, e) for s, e in self.intervals if e < start or s > end]

    def is_in_interval_set(self, value):
        for start, end in self.intervals:
            if start <= value <= end:
                return True
        return False

def main():
    interval_set = IntervalSet()

    while True:
        print("\nInterval Set Management")
        print("1. Add Interval")
        print("2. Remove Interval")
        print("3. Check if Value is in Interval Set")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            start = float(input("Enter start of interval: "))
            end = float(input("Enter end of interval: "))
            interval_set.add_interval(start, end)
            print("Interval added successfully.")

        elif choice == "2":
            start = float(input("Enter start of interval to remove: "))
            end = float(input("Enter end of interval to remove: "))
            interval_set.remove_interval(start, end)
            print("Interval removed successfully.")

        elif choice == "3":
            value = float(input("Enter value to check: "))
            if interval_set.is_in_interval_set(value):
                print("Value is in the interval set.")
            else:
                print("Value is not in the interval set.")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
