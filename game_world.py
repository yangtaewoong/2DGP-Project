from itertools import filterfalse

world = [[] for _ in range(4)]
collision_pairs = {} # 빈 딕셔너리

def add_collision_pair(group, a, b):
    if group not in collision_pairs:
        collision_pairs[group] = [[], []]
    # a와 b가 리스트인지 확인하고 개별 객체를 추가
    if isinstance(a, list):
        collision_pairs[group][0].extend(a)
    elif a:
        collision_pairs[group][0].append(a)

    if isinstance(b, list):
        collision_pairs[group][1].extend(b)
    elif b:
        collision_pairs[group][1].append(b)


def add_object(o, depth = 0):
    world[depth].append(o)

def add_objects(ol, depth = 0):
    world[depth] += ol


def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()
def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)

def remove_object(o):
 # 게임 월드에서 객체를 제거
    for layer in world:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            return

    raise ValueError('Cannot delete non existing object')


def clear():
    for layer in world:
        layer.clear()

# fill here
def collide(a, b):
    al,ab,ar,at = a.get_bb()
    bl,bb,br,bt = b.get_bb()

    if ar < bl: return False
    if al > br: return False
    if at < bb: return False
    if ab > bt: return False

    return True
    pass


def handle_collisions():
    # 게임 월드에 등록된 충돌 정보를 바탕으로, 실제 충돌 검사를 수행
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a, b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)

    return None