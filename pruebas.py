import gymnasium as gym
import torch
import torch.nn as nn

# Esta clase es el agente, al utilizar herencia de nn.Module básicamente
# le estamos diciendo PyTorch que esta clase contiene operaciones
# matemáticas con parámetros ajustables (red neuronal)

#Gymnasium entrega posicion, velocidad, angulo
#y velocidad angular, en ese orden 
class CerebroPrueba(nn.Module): # red neuronal

    def __init__(self):
        super().__init__()

        # 4 sensores (posicion, velocidad, angulo y velocidad angular)
        # 2 acciones posibles (empujar a la izquierda o a la derecha)
        self.capa_decision = nn.Linear(4, 2) 
    def forward(self, x):
        return self.capa_decision(x)

# Instanciamos la red
# Al instanciar la red le aigno valores aleatorios a los pesos
red_neuronal = CerebroPrueba()


env = gym.make("CartPole-v1", render_mode="human") # Cargar entorno en gymnasium
estado_numpy, info = env.reset() # entrega la primera lectura para que pueda iniciar el bucle

print("Ejecutando entrenamiento")

for _ in range(2000):
    #Gymnasium te da los datos en formato NumPy, hay que pasarlos
    #a tensores.
    estado_tensor = torch.tensor(estado_numpy, dtype=torch.float32) 


    # Conectamos el tensor con los 4 datos a la red neuronal, la red
    # los procesa y devuelve dos Q-Values
    valores_accion = red_neuronal(estado_tensor)

    
    # Mira los valores y extrae el índice más alto, si tienes [0.8,0.4]
    #deduce que la acción ganadora es el 0 (empujar a la izquierda)
    #con .item obtenemos ese 0 del pytorch y lo convertimos en un entero
    accion_elegida = torch.argmax(valores_accion).item()
    
    # Enviamos con .step ese 0 al simulador, aplica lo que deba aplicar
    #y devuelve los nuevos datos para poder iterar una vez más
    #además, añadi la variable terminado en caso de que el palo esté caido
    estado_numpy, recompensa, terminado, truncado, info = env.step(accion_elegida)

    # Si determina que esta a punto de caerse, resetea
    if terminado or truncado:
        estado_numpy, info = env.reset()

env.close()