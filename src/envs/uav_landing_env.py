import gymnasium as gym
from gymnasium import spaces
import numpy as np


class LandingEnv(gym.Env):
    """
    Esqueleto del entorno en Gymnasium para el TFG.
    Aquí implementarás tu propia física, dinámica y recompensas.
    """
    metadata = {"render_modes": ["human"], "render_fps": 30}

    def __init__(self, render_mode=None):
        super().__init__()
        self.render_mode = render_mode

        # TODO: Define tu espacio de acción (ej. spaces.Box o spaces.Discrete)
        self.action_space = None

        # TODO: Define tu espacio de observación (ej. spaces.Box con tus sensores/estados)
        self.observation_space = None

        # Variables de estado que quieras inicializar
        self.state = None

    def reset(self, seed=None, options=None):
        """Reinicia el entorno al inicio de cada episodio."""
        super().reset(seed=seed)

        # TODO: Tu lógica para reiniciar el estado inicial del dron y del entorno
        # obs = ...
        # info = ...

        obs = np.zeros(1, dtype=np.float32)
        info = {}
        return obs, info

    def step(self, action):
        """Aplica la acción y avanza un paso en el entorno."""
        # TODO: Tu lógica de actualización de físicas según la acción
        # self.state = ...

        # TODO: Tu función de recompensa
        reward = 0.0

        # TODO: Condiciones de parada (aterrizó o chocó)
        terminated = False

        # TODO: Límite de tiempo/pasos máximos del episodio
        truncated = False

        # TODO: Información adicional (telemetría, logs, métricas)
        info = {}

        obs = np.zeros(1, dtype=np.float32)
        return obs, reward, terminated, truncated, info

    def render(self):
        """Visualización opcional (PyBullet, Pygame, etc.)."""
        pass

    def close(self):
        """Limpieza al cerrar la simulación."""
        pass

