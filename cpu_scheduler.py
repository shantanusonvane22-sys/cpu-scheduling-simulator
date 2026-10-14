# CPU Scheduling Simulator
# Operating Systems Mini Project

def display_results(processes, burst, waiting, turnaround):
    print("\n" + "-" * 65)
    print(f"{'Process':<12}{'Burst Time':<15}{'Waiting Time':<18}{'Turnaround':<15}")
    print("-" * 65)

    for i in range(len(processes)):
        print(
            f"{processes[i]:<12}"
            f"{burst[i]:<15}"
            f"{waiting[i]:<18}"
            f"{turnaround[i]:<15}"
        )

    print("-" * 65)
    print(f"Average Waiting Time: {sum(waiting) / len(processes):.2f}")
    print(f"Average Turnaround Time: {sum(turnaround) / len(processes):.2f}")


def fcfs(processes, burst):
    waiting = [0] * len(processes)
    turnaround = [0] * len(processes)

    for i in range(1, len(processes)):
        waiting[i] = waiting[i - 1] + burst[i - 1]

    for i in range(len(processes)):
        turnaround[i] = waiting[i] + burst[i]

    print("\nFCFS Scheduling")
    print("Order:", " -> ".join(processes))
    display_results(processes, burst, waiting, turnaround)


def sjf(processes, burst):
    order = sorted(range(len(processes)), key=lambda i: (burst[i], i))

    p = [processes[i] for i in order]
    b = [burst[i] for i in order]

    waiting = [0] * len(p)
    turnaround = [0] * len(p)

    for i in range(1, len(p)):
        waiting[i] = waiting[i - 1] + b[i - 1]

    for i in range(len(p)):
        turnaround[i] = waiting[i] + b[i]

    print("\nSJF Scheduling")
    print("Order:", " -> ".join(p))
    display_results(p, b, waiting, turnaround)


def round_robin(processes, burst, quantum):
    remaining = burst.copy()
    completion = [0] * len(processes)
    current_time = 0

    while any(t > 0 for t in remaining):
        for i in range(len(processes)):
            if remaining[i] > 0:
                run_time = min(quantum, remaining[i])
                current_time += run_time
                remaining[i] -= run_time

                if remaining[i] == 0:
                    completion[i] = current_time

    turnaround = completion
    waiting = [
        turnaround[i] - burst[i]
        for i in range(len(processes))
    ]

    print("\nRound Robin Scheduling")
    print("Time Quantum:", quantum)
    display_results(processes, burst, waiting, turnaround)


def main():
    print("=" * 45)
    print("       CPU SCHEDULING SIMULATOR")
    print("=" * 45)

    while True:
        try:
            n = int(input("Enter number of processes (1-20): "))
            if 1 <= n <= 20:
                break
            print("Enter a number between 1 and 20.")
        except ValueError:
            print("Please enter a valid integer.")

    processes = [f"P{i + 1}" for i in range(n)]
    burst = []

    for p in processes:
        while True:
            try:
                b = int(input(f"Enter burst time for {p}: "))
                if b > 0:
                    burst.append(b)
                    break
                print("Burst time must be positive.")
            except ValueError:
                print("Please enter a valid integer.")

    while True:
        print("\n1. FCFS")
        print("2. SJF")
        print("3. Round Robin")
        print("4. Run All")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            fcfs(processes, burst)

        elif choice == "2":
            sjf(processes, burst)

        elif choice == "3":
            while True:
                try:
                    q = int(input("Enter time quantum: "))
                    if q > 0:
                        break
                    print("Enter a positive time quantum.")
                except ValueError:
                    print("Please enter a valid integer.")

            round_robin(processes, burst, q)

        elif choice == "4":
            fcfs(processes, burst)
            sjf(processes, burst)

            while True:
                try:
                    q = int(input("Enter time quantum for Round Robin: "))
                    if q > 0:
                        break
                    print("Enter a positive time quantum.")
                except ValueError:
                    print("Please enter a valid integer.")

            round_robin(processes, burst, q)

        elif choice == "5":
            print("Thank you for using the simulator!")
            break

        else:
            print("Invalid choice. Enter 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()