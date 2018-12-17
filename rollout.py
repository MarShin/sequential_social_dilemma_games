"""Defines a multi-agent controller to rollout environment episodes w/
   agent policies."""

from social_dilemmas.envs.harvest import HarvestEnv
import utility_funcs
import numpy as np
import os
import sys
import shutil

# TODO: Agents incorporated and controlled from here. 

VID_PATH = "/Users/natasha/Dropbox (MIT)/Projects/AgentEmpathy/vids/"

class Controller:

    def __init__(self):
        self.env = HarvestEnv(num_agents=1, render=True)
        self.env.reset()

        # TODO: initialize agents here

    def rollout_and_render(self, horizon=50, render_frames=False, 
                           render_full_vid=True, vid_path=VID_PATH):
        actions = []
        rewards = []
        observations = []

        if render_full_vid:
            shape = self.env.map.shape
            full_obs = [np.zeros((shape[0],shape[1],3), dtype=np.uint8) for i in range(horizon)]
        
        for i in range(horizon):
            # TODO: use agent policy not just random actions
            rand_action = np.random.randint(8)
            obs, rew, dones, info, = self.env.step({'agent-0': rand_action})

            print("timestep", i, "action", rand_action, "reward", rew['agent-0'])
            sys.stdout.flush()

            if render_frames:
                self.env.render_map()

            if render_full_vid:
                rgb_arr = self.env.map_to_colors()
                full_obs[i] = rgb_arr.astype(np.uint8)

            observations.append(obs['agent-0'])
            rewards.append(rew['agent-0'])

        if render_full_vid:
            utility_funcs.make_video_from_rgb_imgs(full_obs, vid_path)


if __name__=='__main__':
    if len(sys.argv) > 1:
        vid_path = sys.argv[1]
    else:
        vid_path = VID_PATH

    c = Controller()
    c.rollout_and_render(vid_path=vid_path)
    
