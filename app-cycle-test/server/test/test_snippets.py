#!/usr/bin/env python3

# testing global variable
init_state = False

def change_state():
    global init_state
    init_state = not(init_state)
    return

def get_status():
    global init_state
    print(init_state)
