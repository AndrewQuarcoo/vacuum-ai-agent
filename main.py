from environment import Playground1, Playground2
from agents import GodAgent, SimpleAgent, RandomAgent 

def main():
    playground_choice = input("Select Playground (1 or 2): ")
    
    if playground_choice == '1':
        playground = Playground1()
    elif playground_choice == '2':
        n = int(input("Enter the number of containers (less than 100): "))  # Get the number of containers
        playground = Playground2(n)  # Pass n to Playground2
    else:
        print("Invalid choice. Please select 1 or 2.")
        return

    # Display the selected playground
    print(f"\nSelected Playground {playground_choice}:")
    playground.display()

    agent_choice = input("Select Agent (1: GodAgent, 2: SimpleAgent, 3: RandomAgent): ")
    
    # Initialize the selected agent
    if agent_choice == '1' or agent_choice.lower() == 'godagent':
        agent = GodAgent(playground)
    elif agent_choice == '2' or agent_choice.lower() == 'simpleagent':
        agent = SimpleAgent(playground)
    elif agent_choice == '3' or agent_choice.lower() == 'randomagent':
        agent = RandomAgent(playground)
    else:
        print("Invalid agent choice. Please select a valid agent.")
        return

    # Clean the playground using the selected agent
    agent.clean()

    # Display the results
    playground.display()  # Show the state of the playground after cleaning
    print(f"Total containers cleaned: {agent.cleaned_count}")
    print(f"Time taken to clean: {agent.time_taken:.2f} seconds")

# Example usage
if __name__ == "__main__":
    main()
