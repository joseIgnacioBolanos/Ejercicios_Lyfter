class Human():
    def __init__(self, torso):
        self.torso = torso

class Torso():
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head= head
        self.right_arm =  right_arm
        self.left_arm =  left_arm
        self.right_leg = right_leg
        self. left_leg = left_leg


class Head():
    def __init__(self):
        pass


class Arm():
    def __init__(self, hand):
        self.hand = hand


class Hand():
    def __init__(self):
        pass


class Leg():
    def __init__(self, foot):
        self.foot =  foot


class Feet():
    def __init__(self):
        pass
        
        


my_head = Head()
left_hand = Hand()
right_hand = Hand()
left_arm= Arm(left_hand)
right_arm = Arm(right_hand)
left_foot = Feet()
right_foot = Feet()
right_leg = Leg(right_foot)
left_leg = Leg(left_foot)
torso = Torso(my_head, left_arm ,right_arm, right_leg, left_leg )
human = Human(torso)


