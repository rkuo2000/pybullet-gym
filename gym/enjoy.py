# Env names: Ant, Altas, HalfCheetah, Hopper, Humanoid, HumanoidFlagrun, HumanoidFlagrunHarder, 
#            InvertedPendulum, InvertedDoublePendulum, InvertedPendulumSwingup, Reacher, Walker2D
import sys
import gymnasium as gym
import pybullet
import pybulletgym.envs
from stable_baselines3 import A2C

env_name = sys.argv[1]

env = gym.make(env_name+"PyBulletEnv-v0")
env.render(mode="human")

model = A2C.load(env_name) 

obs = env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()
