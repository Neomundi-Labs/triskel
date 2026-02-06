import numpy as np

def triskel_trajectory(
    steps=1000,
    radius=1.0,
    rotation_rate=0.02,
    phase_shift=2 * np.pi / 3
):
    """
    Generates a minimal triskel-like cyclic trajectory.

    The trajectory is composed of three rotating arms phase-shifted by 120 degrees.
    This function encodes no objective, feedback, or control logic.

    Parameters
    ----------
    steps : int
        Number of points in the trajectory.
    radius : float
        Base radius of circulation.
    rotation_rate : float
        Angular increment per step.
    phase_shift : float
        Phase offset between arms (default = 120 degrees).

    Returns
    -------
    trajectory : np.ndarray
        Array of shape (steps, 2) representing a 2D path.
    """

    t = np.arange(steps) * rotation_rate

    x = (
        np.cos(t) +
        np.cos(t + phase_shift) +
        np.cos(t + 2 * phase_shift)
    )

    y = (
        np.sin(t) +
        np.sin(t + phase_shift) +
        np.sin(t + 2 * phase_shift)
    )

    trajectory = radius * np.stack([x, y], axis=1)
    return trajectory
