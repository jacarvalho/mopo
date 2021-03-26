from .maze2d_umaze_base import params, deepcopy


params = deepcopy(params)
params['kwargs'].update({
    'number_of_samples': 20000,
})
