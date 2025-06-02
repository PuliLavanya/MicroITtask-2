from collections import defaultdict
import random

def default_q_values():
    return [0, 0, 0]  # three actions: straight, right, left

class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=1.0, epsilon_decay=0.995, epsilon_min=0.01):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        self.q_table = defaultdict(default_q_values)

    def get_state_key(self, state):
        # Simplify state for Q-table key (you can improve this)
        head, food, direction = state
        dx = food[0] - head[0]
        dy = food[1] - head[1]
        return (dx, dy, direction)

    def choose_action(self, state):
        key = self.get_state_key(state)
        if random.random() < self.epsilon:
            return random.choice([0, 1, 2])
        else:
            q_values = self.q_table[key]
            max_q = max(q_values)
            return q_values.index(max_q)

    def learn(self, state, action, reward, next_state, done):
        key = self.get_state_key(state)
        next_key = self.get_state_key(next_state)

        q_predict = self.q_table[key][action]
        q_target = reward
        if not done:
            q_target += self.gamma * max(self.q_table[next_key])

        self.q_table[key][action] += self.alpha * (q_target - q_predict)

        if done:
            self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)
