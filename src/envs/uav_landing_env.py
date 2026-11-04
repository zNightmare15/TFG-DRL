import gymnasium as gym
from gymnasium import spaces
import numpy as np
from stable_baselines3.common.env_checker import check_env


class LandingEnv(gym.Env):
    """
    Esqueleto del entorno en Gymnasium para el TFG.
    Aquí implementarás tu propia física, dinámica y recompensas.
    """
    metadata = {"render_modes": ["human"], "render_fps": 30}

    def __init__(self, render_mode=None):
        super().__init__()
        self.render_mode = render_mode

        # Definimos un espacio continuo de 4 motores
        self.action_space = spaces.Box( #con Box, los numeros pueden variar con decimales entre un minimo y un máximo
            low = -1.0, #asignamos los valores entre -1 y 1
            high = 1.0,
            shape = (4,), # indicamos que existen 4 motores 
            dtype = np.float32 # tipo de dato que vamos a usar para los motores
        )


        self.observation_space = spaces.Box(
            low = -np.inf,
            high = np.inf,
            shape = (21,), #definimos 19 variables, explicadas una por una en mi word
            dtype = np.float32
        )

        # Variables de estado que quieras inicializar
        self.state = None

    def reset(self, seed=None, options=None):
        """Reinicia el entorno al inicio de cada episodio."""
        super().reset(seed=seed)
        # TODO: Inicializar las posiciones iniciales del dron y del barco
        obs = np.zeros(self.observation_space.shape, dtype=np.float32) #Construir  la observación inicial con 21 sensores
        info = { "estado": "INICIALIZADO"} #Creamos un diccionario con informacion adicional
        return obs, info

    def step(self, action):
        """Aplica la acción y avanza un paso en el entorno."""
        # TODO: Empuje de los 4 rotores
        # self.physics.apply(action)

        # TODO: Calcular funcion de recompensa
        reward = 0.0

        # TODO: Ha aterrizado en el barco o se ha estrellado?
        terminated = False

        # TODO: Hemos alcanzado el número máximo de pasos?
        truncated = False

        # TODO: Diccionario de telemetría (info adicional)
        info = {
            "distancia_barco": 0.0,
            "impacto": False
        }

        obs = np.zeros(self.observation_space.shape, dtype=np.float32)
        return obs, float(reward), terminated, truncated, info

    def render(self):
        """Visualización opcional (PyBullet, Pygame, etc.)."""
        pass

    def close(self):
        """Limpieza al cerrar la simulación."""
        pass

if __name__ == "__main__": 
    #comprobamos que funciona el esqueleto
    print("Probando el entorno de aterrizaje UAV")

    #instanciamos el entorno
    env = LandingEnv()

    check_env(env)
    print("Stable-Baselines3 checkeo")

    print(f"Miramos espacio de acciones y de observaciones {env.action_space}, {env.observation_space}")

    #Probamos el reset
    obs, info = env.reset() 
    print(f"Aqui ya hice el reset. Longitud del vector observacion: {len(obs)}. Info: {info}")

    #Probamos una accion aleatoria de ejemplo para ir probando cosas
    accion_aleatoria = env.action_space.sample()
    print(f"Accion aleatoria: {accion_aleatoria}")

    #Ahora probamos un step

    obs, reward, terminated, truncated, info = env.step(accion_aleatoria)
    print(f"Recompensa del step. {reward}")

    #Ahora, cerramos el entorno
    env.close()
    print("Cerrando el entorno")

    #Ejecución: python src/envs/uav_landing_env.py
    #Env: .\venv\Scripts\Activate.ps1
