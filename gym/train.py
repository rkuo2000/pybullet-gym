# Env names: # Ant, Atlas, HalfCheetah, Hopper, Humanoid, HumanoidFlagrun, HumanoidFlagrunHarder, 
#              InvertedPendulum, InvertedDoublePendulum, InvertedPendulumSwingup, Reacher, Walker2D
import sys
import gym
import pybullet
import pybulletgym.envs
from stable_baselines3 import DQN, A2C, PPO, SAC, DDPG, TD3

env_name = sys.argv[1]
timesteps = sys.argv[2]
env = gym.make(env_name+"PyBulletEnv-v0")
env.render(mode="human")

model = DQN('MlpPolicy', env)

model.learn(total_timesteps=int(timesteps))

model.save(env_name)
