import pickle
from snake_env import SnakeEnv
from q_learning_agent import QLearningAgent

def train_snake(num_episodes=5000):
    env = SnakeEnv()
    agent = QLearningAgent()

    for episode in range(1, num_episodes + 1):
        state = env.reset()
        total_reward = 0
        done = False

        while not done:
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.learn(state, action, reward, next_state, done)
            state = next_state
            total_reward += reward

        if episode % 500 == 0:
            print(f"Episode {episode}: Total Reward = {total_reward}, Epsilon = {agent.epsilon:.4f}")

    # Save Q-table after training
    with open("snake_q_table.pkl", "wb") as f:
        pickle.dump(agent.q_table, f)

if __name__ == "__main__":
    train_snake()
