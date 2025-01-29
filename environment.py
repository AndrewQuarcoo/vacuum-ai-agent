import random

# Playground1: Create two containers with a shit emoji
class Playground1:
    def __init__(self):
        # Create two containers that are randomly dirty or clean
        self.containers = ['💩' if random.choice([True, False]) else '✅' for _ in range(2)]

    def display(self):
        for i in range(2):
            status = "Dirty" if self.containers[i] == '💩' else "Clean"
            print(f"Container {i + 1}: {self.containers[i]} - {status}")
            

# Playground2: Create n number of containers
class Playground2:
    def __init__(self, n):
        if n >= 100:
            raise ValueError("n must be less than 100")
        self.containers = []
        for i in range(n):
            emoji = '💩' if i % 2 == 0 else '✅'  # Even index is dirty, odd index is clean
            self.containers.append(emoji)

    def display(self):
        for i, emoji in enumerate(self.containers):
            status = "Dirty" if emoji == '💩' else "Clean"
            print(f"Container {i + 1}: {emoji} - {status}")

# Example usage
if __name__ == "__main__":
    playground1 = Playground1()
    print("Playground 1:")
    playground1.display()

    # Get the number of containers for Playground2
    try:
        n = int(input("Enter the number of containers for Playground 2 (less than 100): "))  # Get user input
        playground2 = Playground2(n)  # Pass n to Playground2
        print("\nPlayground 2:")
        playground2.display()
    except ValueError:
        print("Invalid input. Please enter a valid integer less than 100.")
