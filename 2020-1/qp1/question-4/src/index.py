from controllers.window import Window

if __name__ == '__main__':
    # Possibilities: cube, triangle and quad
    win = Window(550, 550, 'Testing', 'cube')
    win.main_loop()
