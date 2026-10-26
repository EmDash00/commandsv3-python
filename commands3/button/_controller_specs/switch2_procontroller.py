from commands3.button._controller_specs.controller_spec import ControllerSpec


spec = ControllerSpec(
    filename="command_switch2procontroller.py",
    wrapper_class="CommandSwitch2ProController",
    controller_class="Switch2ProController",
    buttons=(
        ButtonSpec("A", "a", "a_button", "A button"),
        ButtonSpec("B", "b", "b_button", "B button"),
        ButtonSpec("X", "x", "x_button", "X button"),
        ButtonSpec("Y", "y", "y_button", "Y button"),
        ButtonSpec("MINUS", "minus", "minus_button", "Minus button"),
        ButtonSpec("HOME", "home", "home_button", "Home button"),
        ButtonSpec("PLUS", "plus", "plus_button", "Plus button"),
        ButtonSpec(
            "LEFT_STICK", "left_stick", "left_stick_button", "Left stick button"
        ),
        ButtonSpec(
            "RIGHT_STICK", "right_stick", "right_stick_button", "Right stick button"
        ),
        ButtonSpec("L", "l", "l_button", "L button"),
        ButtonSpec("R", "r", "r_button", "R button"),
        ButtonSpec("DPAD_UP", "dpad_up", "dpad_up_button", "D-pad up button"),
        ButtonSpec(
            "DPAD_DOWN", "dpad_down", "dpad_down_button", "D-pad down button"
        ),
        ButtonSpec(
            "DPAD_LEFT", "dpad_left", "dpad_left_button", "D-pad left button"
        ),
        ButtonSpec(
            "DPAD_RIGHT", "dpad_right", "dpad_right_button", "D-pad right button"
        ),
        ButtonSpec("CAPTURE", "capture", "capture_button", "Capture button"),
        ButtonSpec("GR", "gr", "gr_button", "GR button"),
        ButtonSpec("GL", "gl", "gl_button", "GL button"),
        ButtonSpec("C", "c", "c_button", "C button"),
    ),
    axes=(
        AxisSpec(
            "LEFT_X",
            "left_x",
            "left X axis",
            "get_left_x",
            "set_left_x_deadband",
            "Right",
        ),
        AxisSpec(
            "LEFT_Y",
            "left_y",
            "left Y axis",
            "get_left_y",
            "set_left_y_deadband",
            "Up",
        ),
        AxisSpec(
            "RIGHT_X",
            "right_x",
            "right X axis",
            "get_right_x",
            "set_right_x_deadband",
            "Right",
        ),
        AxisSpec(
            "RIGHT_Y",
            "right_y",
            "right Y axis",
            "get_right_y",
            "set_right_y_deadband",
            "Up",
        ),
        AxisSpec(
            "ZL",
            "zl",
            "ZL axis",
            "get_zl",
            "set_zl_deadband",
            "Pressed down",
        ),
        AxisSpec(
            "ZR",
            "zr",
            "ZR axis",
            "get_zr",
            "set_zr_deadband",
            "Pressed down",
        ),
    ),
),
