from snake_env import SnakeEnv
from q_learning_agent import QLearningAgent
import pickle
import time

def play_snake():
    env = SnakeEnv()
    agent = QLearningAgent(epsilon=0)  # no random moves

    with open("snake_q_table.pkl", "rb") as f:
        agent.q_table = pickle.load(f)

    state = env.reset()
    env.render = lambda: print(f"Snake Head: {state[0]}, Food: {state[1]}, Direction: {state[2]}")  # simple print

    done = False
    while not done:
        env.render()
        action = agent.choose_action(state)
        state, reward, done = env.step(action)
        time.sleep(0.5)

    print("Game Over!")

if __name__ == "__main__":
    play_snake()
