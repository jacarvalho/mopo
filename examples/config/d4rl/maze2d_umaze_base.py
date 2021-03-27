from .base_mopo import mopo_params, deepcopy

params = deepcopy(mopo_params)
params.update({
    'domain': 'maze2d',
    'task': 'umaze-v1',
    'exp_name': 'maze2d_umaze_v1'
})
params['kwargs'].update({
    'pool_load_path': 'd4rl/maze2d-umaze-v1',
    'pool_load_max_size': 101000,
    'rollout_length': 5,
    'penalty_coeff': 1.0,

    'number_of_samples': 1000,

    'eval_n_episodes': 100,
    'eval_deterministic': False,
    'eval_every_n_epoch': 50,

    # BNN size of hidden dimensions
    'hidden_dim': 64,
    'bnn_max_epochs': 100,
})
