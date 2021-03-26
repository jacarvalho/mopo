import numpy as np
import tensorflow as tf
import tensorflow_probability as tfp


class SquashBijector(tfp.bijectors.Bijector):
    def __init__(self, validate_args=False, name="tanh", a_scale=1.):
        super(SquashBijector, self).__init__(
            forward_min_event_ndims=0,
            validate_args=validate_args,
            name=name)

        self._a_scale = a_scale

    def _forward(self, x):
        return self._a_scale * tf.nn.tanh(x)

    def _inverse(self, y):
        return 1/self._a_scale * tf.atanh(y)

    def _forward_log_det_jacobian(self, x):
        return 2. * (np.log(2.) - x - tf.nn.softplus(-2. * x))
