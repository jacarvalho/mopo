from .cartpole_stabilization_base import params, deepcopy


params = deepcopy(params)
params['kwargs'].update({
    'number_of_samples': 500000,
})

