from pythonwhat.State import State
from pythonwhat.Reporter import Reporter

from IPython.core.interactiveshell import InteractiveShell

class MockProcess:
    """Mock the processes used in pythonbackend to evaluate code."""
    def __init__(self, **kwargs):
        self.shell = InteractiveShell(user_ns = kwargs)

    def executeTask(self, task):
        return task(self.shell)

def create_state(solution_code="", student_code="", pre_exercise_code="",
                 student_process = None, solution_process = None,
                 raw_student_output="",
                 reporter = None):
    """Create a state for testing SCTs. 
    
    Custom processes are required for SCTs that execute code (e.g. has_equal_value).
    See MockProcess above.
    """
    if reporter is None: reporter = Reporter()
    Reporter.active_reporter = reporter
    state =  State(full_student_code = student_code,
                   full_solution_code = solution_code,
                   **locals())

    # only used to get converters :/
    State.root_state = state

    return state

def create_x_state(stu_val, sol_val, **kwargs):
    s = create_state(student_process = MockProcess(x = stu_val),
                     solution_process = MockProcess(x = sol_val), 
                     **kwargs)

    return s
