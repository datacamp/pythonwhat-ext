__version__ = '0.0.1'

# Import only from pythonwhat.check_syntax for extensions, as they contain
# the correctly decorated SCTs, used on DataCamp.
from pythonwhat.check_syntax import state_dec, Ex
import numpy as np

@state_dec
def check_numpy_array(name, state = None):
    """Test a numpy array object. Return that object.
    
    Args:
        name: name of the object to be tested.

    """
    # is defined
    obj = Ex(state).check_object(name)

    # is a numpy array
    obj.is_instance(np.ndarray)

    # same shape
    obj.has_equal_value(expr_code = '{:s}.shape'.format(name))

    # equal contents
    obj.has_equal_value()

    # return object state for chaining
    return obj
