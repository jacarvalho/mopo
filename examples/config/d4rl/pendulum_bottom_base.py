from .base_mopo import mopo_params, deepcopy

params = deepcopy(mopo_params)
params.update({
    'domain': 'PendulumStartFromBottom',
    'task': 'v0',
    'exp_name': 'pendulum_bottom'
})
params['kwargs'].update({
    'pool_load_path': 'gym/PendulumStartFromBottom-v0',
    'pool_load_max_size': 101000,
    'rollout_length': 5,
    'penalty_coeff': 1.0,

    'number_of_samples': 1000,

    'eval_n_episodes': 10,
    'eval_deterministic': False,
    'eval_every_n_epoch': 50,

    # BNN size of hidden dimensions
    'hidden_dim': 64,
    'bnn_max_epochs': 100,
})
