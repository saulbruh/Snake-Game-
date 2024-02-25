import turtle
import random

# Configuración inicial
w = 800  # Ancho de la ventana
h = 600  # Altura de la ventana
food_size = 15  # Tamaño de la comida
delay = 75  # Retraso en milisegundos entre actualizaciones de la pantalla

# Diccionario de desplazamientos para cada dirección
offsets = {
  "up": (0, 20),
  "down": (0, -20),
  "left": (-20, 0),
  "right": (20, 0)
}

# Función para reiniciar el juego
def reset():
  global snake, snake_dir, food_position, pen
  snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0,80]]  # Inicializa la serpiente en el centro de la pantalla
  snake_dir = "up"  # La serpiente comienza moviéndose hacia arriba
  food_position = get_random_food_position()  # Coloca la comida en una posición aleatoria
  food.goto(food_position)  # Mueve la comida a su posición
  move_snake()  # Comienza a mover la serpiente

# Función para mover la serpiente en la pantalla
def move_snake():
  global snake_dir

  new_head = snake[-1].copy()  # Obtiene la última posición de la serpiente (la cabeza)
  new_head[0] = snake[-1][0] + offsets[snake_dir][0]  # Calcula la nueva posición de la cabeza en el eje x
  new_head[1] = snake[-1][1] + offsets[snake_dir][1]  # Calcula la nueva posición de la cabeza en el eje y

  # Si la serpiente choca consigo misma, reinicia el juego
  if new_head in snake[:-1]:
    reset()
  else:
    snake.append(new_head)  # Agrega la nueva cabeza a la serpiente

    # Si no hay colisión con la comida, quita la cola de la serpiente
    if not food_collision():
      snake.pop(0)

    # Si la serpiente se sale de la pantalla, la hace aparecer del otro lado
    if snake[-1][0] > w / 2:
      snake[-1][0] -= w
    elif snake[-1][0] < - w / 2:
      snake[-1][0] += w
    elif snake[-1][1] > h / 2:
      snake[-1][1] -= h
    elif snake [-1][1] < h / 2:
      snake[-1][1] += h

    # Limpia las estampas de la serpiente y las vuelve a dibujar
    pen.clearstamps()

    for segment in snake:
      pen.goto(segment[0], segment[1])
      pen.stamp()

    # Actualiza la pantalla
    screen.update()

    # Llama a la función move_snake después de un retraso
    turtle.ontimer(move_snake, delay)

# Función para verificar si la serpiente ha chocado con la comida
def food_collision():
  global food_position
  if get_distance(snake[-1], food_position) < 20:
    food_position = get_random_food_position()  # Coloca la comida en una nueva posición aleatoria
    food.goto(food_position)  # Mueve la comida a su nueva posición
    return True
  return False

# Función para obtener una posición aleatoria para la comida
def get_random_food_position():
  x = random.randint( - w // 2 + food_size, w // 2 - food_size)
  y = random.randint( - h // 2 + food_size, h // 2 - food_size)
  return(x, y)

# Función para calcular la distancia entre dos puntos
def get_distance(pos1, pos2):
  x1, y1 = pos1
  x2, y2 = pos2
  distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
  return distance

# Funciones para cambiar la dirección de la serpiente
def go_up():
  global snake_dir
  if snake_dir != "down":  # Evita que la serpiente se mueva en la dirección opuesta
    snake_dir = "up"

def go_right():
  global snake_dir
  if snake_dir != "left":
    snake_dir = "right"

def go_down():
  global snake_dir
  if snake_dir != "up":
    snake_dir = "down"

def go_left():
  global snake_dir
  if snake_dir != "right":
    snake_dir = "left"

# Configuración de la pantalla
screen = turtle.Screen()
screen.setup(w, h)
screen.title("Snake")
screen.bgcolor("blue")
screen.setup(800, 600)
screen.tracer(0)

# Configuración de la serpiente
pen = turtle.Turtle("square")
pen.penup()

# Configuración de la comida
food = turtle.Turtle("square")
food.shape("square")
food.color("yellow")
food.shapesize(food_size / 20)
food.penup()

# Configuración de los controles del juego
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

# Inicia el juego
reset()
turtle.done()