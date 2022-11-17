# [pybullet-gym](https://github.com/benelot/pybullet-gym)
**Setup**<br>
```
pip install gym
pip install stable-baselines3
git clone https://github.com/rkuo2000/pybullet-gym
export PYTHONPATH=$PATH:/home/yourname/pybullet-gym
```

## gym
**Env names:** *Ant, Atlas, HalfCheetah, Hopper, Humanoid, HumanoidFlagrun, HumanoidFlagrunHarder, InvertedPendulum, InvertedDoublePendulum, InvertedPendulumSwingup, Reacher, Walker2D*<br>

**Train**<br>
`python train.py Ant 10000000`<br>

**Enjoy** with trained-model<br>
`python enjoy.py Ant`<br>

**Enjoy** with pretrained weights<br>
`python enjoy_Ant.py`<br>
`python enjoy_HumanoidFlagrunHarder.py` (copy from pybulletgym/examples/roboschool-weights/enjoy_TF_*.py)<br>

**Status of Gym Implementation:**<br>
Environment Name | Implemented | Similar to Reference Implementation | Pretrained agent available
---------|---------|---------|---------
| **RoboSchool Envs** |
InvertedPendulumPyBulletEnv-v0          | Yes | Yes | No
InvertedDoublePendulumPyBulletEnv-v0    | Yes | Yes | No
InvertedPendulumSwingupPyBulletEnv-v0   | Yes | Yes | No
ReacherPyBulletEnv-v0                   | Yes | Yes | No
Walker2DPyBulletEnv-v0                  | Yes | No | No
HalfCheetahPyBulletEnv-v0               | Yes | No | No
AntPyBulletEnv-v0                       | Yes | Yes | No
HopperPyBulletEnv-v0                    | Yes | Yes | No
HumanoidPyBulletEnv-v0                  | Yes | Yes | No
HumanoidFlagrunPyBulletEnv-v0           | Yes | Yes | No
HumanoidFlagrunHarderPyBulletEnv-v0     | Yes | Yes | No
AtlasPyBulletEnv-v0                     | WIP | No | No
PusherPyBulletEnv-v0                    | WIP | No | No
ThrowerPyBulletEnv-v0                   | WIP | No | No
StrikerPyBulletEnv-v0                   | WIP | No | No
| **MuJoCo Envs** |
InvertedPendulumMuJoCoEnv-v0            | Yes | Yes | Yes
InvertedDoublePendulumMuJoCoEnv-v0      | Yes | Yes | Yes
ReacherMuJoCoEnv-v0                     | No | No | No
Walker2DMuJoCoEnv-v0                    | Yes | No | No
HalfCheetahMuJoCoEnv-v0                 | Yes | No | No
AntMuJoCoEnv-v0                        | Yes | No | No
HopperMuJoCoEnv-v0                      | Yes | No | No
HumanoidMuJoCoEnv-v0                    | Yes | No | No
PusherMuJoCoEnv-v0                      | No | No | No
ThrowerMuJoCoEnv-v0                     | No | No | No
StrikerMuJoCoEnv-v0                     | No | No | No

## [unitree](https://github.com/unitreerobotics/unitree_pybullet)
`python a1.py`<br>
