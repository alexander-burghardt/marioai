
import keyboard

class KeyboardController:
    def __init__(self, env):
        self.env = env
        
    def read(self):
        if keyboard.is_pressed('shift+space+right'):
            return self.env.SPEED_JUMP_RIGHT
        if keyboard.is_pressed('shift+space+left'):
            return self.SPEED_JUMP_LEFT

        elif keyboard.is_pressed('space+right'):
            return self.env.JUMP_RIGHT
        elif keyboard.is_pressed('space+left'):
            return self.env.JUMP_LEFT

        if keyboard.is_pressed('shift+right'):
            return self.env.SPEED_RIGHT
        if keyboard.is_pressed('shift+left'):
            return self.env.SPEED_LEFT

        elif keyboard.is_pressed('right'):
            return self.env.RIGHT
        elif keyboard.is_pressed('left'):
            return self.env.LEFT
        elif keyboard.is_pressed('down'):
            return self.env.DOWN
        elif keyboard.is_pressed('space'):
            return self.env.JUMP
        else:
            return self.env.NOTHING