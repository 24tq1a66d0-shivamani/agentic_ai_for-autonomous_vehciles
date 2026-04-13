class AutonomousAgent:
    def __init__(self):
        pass

    def perceive(self, data):
        return data

    def decide(self, perception):
        if perception["traffic_light"] == "red":
            return "STOP"
        elif perception["obstacle"]:
            return "TURN RIGHT"
        else:
            return "MOVE FORWARD"

    def act(self, data):
        perception = self.perceive(data)
        decision = self.decide(perception)
        return decision
