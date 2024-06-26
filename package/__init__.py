from package import cheetah
from package import walker
from package import hopper
from package import quadruped
from package import jaco
from package import point_mass_maze


def make(domain, task,
         task_kwargs=None,
         environment_kwargs=None,
         visualize_reward=False):
    
    if domain == 'cheetah':
        return cheetah.make(task,
                            task_kwargs=task_kwargs,
                            environment_kwargs=environment_kwargs,
                            visualize_reward=visualize_reward)
    elif domain == 'walker':
        return walker.make(task,
                           task_kwargs=task_kwargs,
                           environment_kwargs=environment_kwargs,
                           visualize_reward=visualize_reward)
    elif domain == 'point_mass_maze':
        return point_mass_maze.make(task,
                           task_kwargs=task_kwargs,
                           environment_kwargs=environment_kwargs,
                           visualize_reward=visualize_reward)
    elif domain == 'hopper':
        return hopper.make(task,
                           task_kwargs=task_kwargs,
                           environment_kwargs=environment_kwargs,
                           visualize_reward=visualize_reward)
    elif domain == 'quadruped':
        return quadruped.make(task,
                           task_kwargs=task_kwargs,
                           environment_kwargs=environment_kwargs,
                           visualize_reward=visualize_reward)
    else:
        raise f'{task} not found'

    assert None
    
    
def make_jaco(task, obs_type, seed):
    return jaco.make(task, obs_type, seed)