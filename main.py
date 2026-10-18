from ursina import * 
from ursina.prefabs.first_person_controller import FirstPersonController
import random
import sys 
from pathlib import Path 
"""from pathlib import Path 
from panda3d.core import NodePath 
from direct.actor.Actor import Actor 
import gltf"""
 
"""class Character(Entity): 
    def _init_(self, path, anims=('idle', 'walk'), **kwags): 
        super.__init__(**kwags) 
        settings = gltf.GltfSettings()
        settings.no_srgb = True 
        self.actor = Actor(NodePath(gltf.load_model(path, gltf_settings=settings))) 
        self.actor.reparentTo(self) 
        self.actor.SetH(180) 
        self.actor.enableBlend()
        for name in anims: 
            self.actor.loop(name)
        self.weights = {n: 0.0 for n in anims}
        self.target = anims[0]
        self.weights[self.target] = 1.0 

    def update(self): 
        for name in self.weights: 
            goal = 1.0 if name == self.target else 0.0 
            self.weights[name] = lerp(self.weights[name], goal, 6 * time.dt) 
            self.actor.setControlEffect(name, self.weights[name])



app = Ursina() 
npc = Character('soldier.glb')
npc.target = 'walk'"""

app = Ursina() 
if getattr(sys, 'frozen', False): 
    application.asset_folder = Path(sys._MEIPASS) 

# Земля
ground = Entity(
    model='plane', 
    scale =(3000, 1, 3000), 
    color=color.gray, 
    texture='white_cube', 
    collider='box'

) 

# Игрок от первого лица
player = FirstPersonController(position=(30, 0, 0))

NORMAL_SPEED = 5
SHIFT_SPEED = 10 

player.speed = NORMAL_SPEED 

def update(): 
    if held_keys['left shfit'] or held_keys['right shift']: 
        player.speed = SHIFT_SPEED
    else: 
        player.speed = NORMAL_SPEED 

# Прицел
crosshair = Entity(
    parent=camera.ui, 
    model='quad', 
    color=color.red, 
    scale=0.01 

) 

""" # Оружие 

weapon = Entity(
    parent=camera,
    model='cube', 
    color=color.dark_gray, 
    scale=(0.1, 0.1, 0.5), 
    position=(0.5, -0.25, 0.5) 

) """

# Враги или мишени для теста 
target = Entity(model='cube', color=color.orange, position=(0, 1, 5), collider='box')

 



"""# ПТРК
weapon_color = color.rgb(50, 50, 50)

ptrk_launcher = Entity(
    parent=camera.ui, 
    model='cylinders', 
    color=weapon_color, 
    scale=(0.15, 0.15, 1.2),
    rotation=(10, -10, 90)
) 

# Блок управления/прицеливания на трубу 
ptrk_block = Entity(
    parent=ptrk_launcher, 
    model='cube', 
    scale=(1.5, 1.2, 0.3), 
    position=(0, 0.6, -0.2)

)"""

# Небо

Sky()

# Солдат 

soldier = Entity( 
    model='soldier.glb',
    scale=.02,
    position=(10, 0, 9), 
    rotation=(0, 90, 0),
    collider='box'
)




"""# --- Логика и физика NPC противника ---
    
if soldier and soldier.enabled and player.health > 0:
        ground_ray = raycast(soldier.position + Vec3(0, 0.1, 0), Vec3(0, -1, 0), distance=0.2, ignore=(soldier, player))
        if ground_ray.hit:
            soldier.velocity_y = 0
            soldier.y = ground_ray.world_point.y
        else:
            soldier.velocity_y -= soldier.gravity * time.dt
            soldier.y += soldier.velocity_y * time.dt

        soldier.look_at_2d(player.position, 'y')

        origin_pos = soldier.position + Vec3(0, 0.5, 0)
        hit_info = raycast(origin_pos, soldier.forward, distance=0.8, ignore=(soldier, player))

        if not hit_info.hit:
            soldier.position += soldier.forward * soldier.speed * time.dt
        else:
            high_origin = soldier.position + Vec3(0, 1.5, 0)
            high_hit = raycast(high_origin, soldier.forward, distance=0.8, ignore=(soldier, player))
            if not high_hit.hit and ground_ray.hit:
                soldier.velocity_y = 8

if soldier.y < -15:
            destroy(soldier)
            enemy = None
            invoke(spawn_sordier, delay=2)"""
            

# Дрон камикадзе 

dron_kamikadze = Entity( 
    parent=camera.ui, 
    model='dron_kamikadze', 
    color=color.black, 
    scale=(1.5, 0.1, 0.2), 
    position=(5, 5, -5)

)


# Истребитель

fighter_plane = Entity(
    model='f-38_next_generation_stealth_fighter_jet.glb',  
    scale=1.9, 
    position=(5, 30, -55),
    rotation=(0, 180, 0),
    collider='box'
)

fighter_speed = 40

def update():
    fighter_plane.x += fighter_speed * time.dt 
    drone.x += drone_speed * time.dt 
    bomber.x += bomber_speed * time.dt 
    drone2.x += drone2_speed * time.dt 
    missile.x += missile_speed * time.dt
    transport_plane.x += trandsport_speed * time.dt

    if fighter_plane.x > 700: 
        fighter_plane.x = -700
        
    if drone.x > 500: 
        drone.x = -500

    if pvo_missile.active: 
        pvo_missile.look_at(drone)

    if drone2.x > 1500:
        drone2.x = -1500

    if missile.x > 1500: 
        missile.x = -1500 

    if transport_plane.x > 3000: 
        transport_plane.x = -3000

    pvo_missile.position += pvo_missile.forward * pvo_missile.speed * time.dt 

    """drone12.look_at(camera)
    drone12.position += drone12.forward * drone12.speed * time.dt"""

    if bomber.x > 700: 
        bomber.x = -700 

    if not hasattr(bomber, 'bomb_cooldown'): 
        bomber.bomb_cooldown = 0

    bomber.bomb_cooldown -= time.dt 

    for e in scene.entities: 
        if 'bomb' in str(e.name).lower(): 

            if hasattr(e, 'parent') and e.parent == bomber: 

                if bomber.bomb_cooldown <= 0 and -700 < bomber.x < 700: 
                    e.parent = scene 
                    e.fall_speed = 15
                    bomber.bomb = 2.0 
                    break 

            elif hasattr(e, 'fall_speed'): 
                e.y -= e.fall_speed * time.dt 

                if e.y <= 0: 

                    explosion = Entity(
                        model='sphere',
                        color=color.yellow, 
                        position=e.position,
                        scale=4

                    ) 
                    destroy(explosion, delay=0.5)
                    destroy(e)

    if distance(pvo_missile, drone) < 2:
        drone.enabled = False
        pvo_missile.active = False 

        explosion = Entity(
            model='sphere', 
            color=color.yellow, 
            position=pvo_missile.position, 
            scale=4)




# Включаем свет, чтобы убрать серый оттенок
DirectionalLight(y=2, z=-3, rotation=(45, 45, 0))

# Вылет пуль

cartridge_ejection = 20


# Автомат
avtomat_model = Entity(
    model='gun.glb',
    color=color.dark_gray, 
    scale=0.15,
    parent=camera,
    position=(0.5, -0.4, 1),
    rotation=(0, 90, 0),
    collider='box'

)

    
# Стрельба

def input(key):
    if key == 'left mouse down':
        # Создаем пулю перед автоматом
        bullet = Entity(
            model='sphere',
            color=color.yellow,
            scale=0.15,
            position=camera.world_position + camera.forward * 1.5,
            collider='box'
        )
        #  Запускаем пулю вперед в бесконечность!
        bullet.animate_position(bullet.position + camera.forward * 40, duration=0.3, curve=curve.linear)
        #  Удаляем пулю через секунду, чтобы игра не лагала
        destroy(bullet, delay=1)

# Новое оружие AKF-91 

mygunnew = Entity(
    model='mygunnew.glb', 
    color=color.dark_gray,
    scale=0.15, 
    position=(1, 1, 1), 
    rotation=(0, 0, 0) 

)

# Дрон 

drone = Entity(
    model='mydrone.glb', 
    color=color.dark_gray, 
    scale=0.29, 
    position=(5, 9, 5),
    rotation=(0, 180, 0),
    collider='box'

) 


drone_speed = 50

# Дрон-81 

drone2 = Entity(
model='drone81.glb',
color=color.dark_gray, 
scale=0.45,
position=(5, 11, 70),
rotation=(0, -100, 0),
collider='box'

)

drone2_speed = 130

# Ракета дальнобойная 

missile = Entity(
    model='missile',
    color=color.green,
    scale=0.55,
    position=(5, 20, 50),
    rotation=(0, -100, 0),
    collider='box'

) 

missile_speed = 200

# Танк(Заброшенный)

tank = Entity(
    model='tank.glb', 
    #color=color.green, 
    scale=2,
    position=(13, 3, 0), 
    rotation=(0, 9, 0),
    collider='box'

)

# Небоскрёб

house = Entity(
    model='house.glb', 
    color=color.gray, 
    scale=0.42, 
    position=(55, 2, 0), 
    rotation=(0, 9, 0),
    collider='box'

)

# Мост 

bridge = Entity(
    model='bridge.glb', 
    color=color.gray, 
    scale=0.55, 
    position=(-80, 11, 0),
    rotation=(0, 9, 0),
    collider='box'

)

# Создание ракеты ПВО 
pvo_missile = Entity(
    model='sphere', 
    color=color.orange,
    scale=0.5,
    visible=False 
)

pvo_missile.active = False
pvo_missile.speed = 80 




def launch_pvo(): 
    if not pvo_missile.active and drone.enabled: 
        pvo_missile.position = (15, 2, 15)
        pvo_missile.visible = True
        pvo_missile.active = True

        invoke(launch_pvo, delay=random.randint(10, 25))

invoke(launch_pvo, delay=5)

def respawn_drone(): 
    drone.enabled = True

    drone.x = random.choice([-700, 700])
    drone.y = 25 
    drone.z = random.randint(-200, 200)


# Дрон12 

"""drone12 = Entity(
    model='drone12.glb', 
    position=(0, 70, 0),
    rotation=(0, 90, 0),
    scale=0.1,
    collider='box'

) 
drone12.speed = 60"""

# Бомбардировщик 

bomber = Entity(
    model='a20_bomber.glb', 
    position=(5, 70, -65),
    rotation=(0, 90, 0), 
    scale=2.5, 
    collider='box'

) 
bomber_speed = 100

# С-17 (военный грузовой самолёт)

transport_plane = Entity(
    model='c17_globemaster_with_animation.glb',
    position=(10, 80, -105), 
    rotation=(0, -90, 0),
    scale=2.5,
    collider='box'

)
trandsport_speed = 150

# Забор 

fence = Entity(
    model='fence.glb',
    color=color.gray,
    position=(165, 0, 0),
    rotation=(0, 0, 0), 
    scale=3.5, 
    collider='box'

) 

"""# Инвентарь

def update():
    global avtomat
    if held_keys['e']:
        if not avtomat:
            avtomat = True
            update_inventory_ui()



avtomat = False
mygunnew = False

inventory_text = Text(
    text='Инвентарь: пусто',
    position=(0, -0.45),
    origin=(0, 0),
    scale=1.3,
    background=True
)

def update_inventory_ui():
    global avtomat, mygunnew  
    items = []
    if avtomat:
        items.append('Автомат')
    if mygunnew:
        items.append('AKF-91')
        
    inventory_text.text = f'Инвентарь: {", ".join(items)}' if items else 'Инвентарь: пусто'

def input(key):
    global avtomat
    if key == '1' and avtomat: """

    
app.run()