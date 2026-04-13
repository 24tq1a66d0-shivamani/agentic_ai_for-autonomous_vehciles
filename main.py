from agent import AutonomousAgent

def main():
    agent = AutonomousAgent()

    # Simulated environment inputs
    environment_data = [
        {"obstacle": False, "traffic_light": "green"},
        {"obstacle": True, "traffic_light": "green"},
        {"obstacle": False, "traffic_light": "red"},
    ]

    for data in environment_data:
        action = agent.act(data)
        print(f"Input: {data} -> Action: {action}")

if __name__ == "__main__":
    main()
