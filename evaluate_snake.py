from snake_env import SnakeEnv
from q_learning_agent import QLearningAgent
import pickle

with open("q_table.pkl", "rb") as f:
    q_table = pickle.load(f)

env = SnakeEnv()
agent = QLearningAgent()
agent.q_table = q_table
agent.epsilon = 0  # No exploration during evaluation

games = 100
scores = []

for _ in range(games):
    state = env.reset()
    done = False
    score = 0
    while not done:
        action = agent.choose_action(state)
        state, reward, done = env.step(action)
        score += reward
    scores.append(score)

print(f"Average score over {games} games: {sum(scores)/len(scores):.2f}")
