import gymnasium as gym

env = gym.make(
    "InvertedPendulum-v5",
    render_mode='human'
)

observation, info = env.reset()

print(f'Oberservation: {observation}')
print(f'Oberservation space: {env.observation_space}')
print(f'Action space: {env.action_space}')

for step in range(1000):
    
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)

    if step % 100 == 0:
        print(f'Step: {step}')
        print(f'Observation: {observation}')
        print(f'Reward: {reward}')

    if terminated or truncated:
        print('Episode ended')
        observation, info = env.reset()
env.close()