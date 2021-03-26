import numpy as np

class StaticFns:

    @staticmethod
    def termination_fn(obs, act, next_obs):
        assert len(obs.shape) == len(next_obs.shape) == len(act.shape) == 2

        done = np.array([False]).repeat(len(obs))
        done = done[:,None]

        stabilization_th = 0.25  # [rad]

        theta = obs[:, 0]
        x_dot = obs[:, 1]
        theta_dot = obs[:, 2]

        done[:, 0] =  np.abs(theta) > stabilization_th

        return done
