from ursina import * 
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina() 

# Земля
ground = Entity(
    model='plane', 
    scale =(50, 1, 50), 
    color=color.gray, 
    texture='white_cube', 
    collider="box"

) 

# Игрок от первого лица
player = FirstPersonController()

# Прицел
crosshair = Entity(
    parent=camera.ui, 
    model='quad', 
    color=color.red, 
    scale=0.01 

) 

# Оружие 

weapon = Entity(
    parent=camera,
    model='cube', 
    color=color.dark_gray, 
    scale=(0.1, 0.1, 0.5), 
    position=(0.5, -0.25, 0.5) 

) 

# Враги или мишени для теста 
target = Entity(model='cube', color=color.orange, position=(0, 1, 5), collider='box')

# Логика стрельбы 

def input(key): 
    if key == 'left mouse down': 
        hit_info = raycast(camera.world_position, camera.forward, distance=30)

        if hit_info.hit: 
            print("Попадание в противника:", hit_info.entity)
            if hit_info.entity == target: 
                hit_info.entity.color = color.red

# Небо

Sky()

# Солдат 



# Включаем свет, чтобы убрать серый оттенок
DirectionalLight(y=2, z=-3, rotation=(45, 45, 0))

# Вылет пуль

cartridge_ejection = 20

app.run()