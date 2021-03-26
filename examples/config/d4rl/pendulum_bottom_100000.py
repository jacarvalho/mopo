from .pendulum_bottom_base import params, deepcopy


params = deepcopy(params)
params['kwargs'].update({
    'number_of_samples': 100000,
})
