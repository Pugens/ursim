# Script for UR5 with Polyscope controller with user input switch

# Display a popup to get user input
text_input = popup("Enter 'a' for Motion A or 'b' for Motion B:", "User Input", False, False, blocking=True)

# Check the user input
if text_input == 'a':
    # Move to Motion A
    movej(p[0.1, -0.5, 0.3, -1.5, 1.5, 0], a=0.5, v=0.1)

    # Open the gripper
    set_digital_out(2, True)
    sleep(2)

    # Move to a target position for Motion A
    movel(p[0.2, -0.4, 0.2, -1.5, 1.5, 0], a=0.5, v=0.1)

    # Close the gripper
    set_digital_out(2, False)
    sleep(2)

    # Move back to the starting position for Motion A
    movej(p[0.1, -0.5, 0.3, -1.5, 1.5, 0], a=0.5, v=0.1)

elif text_input == 'b':
    # Move to Motion B
    movej(p[-0.5, -0.3, 0.4, -1.5, 1.5, 0], a=0.5, v=0.1)

    # Perform the actions for Motion B (customize as needed)

    # Move back to the starting position for Motion B
    movej(p[-0.5, -0.3, 0.4, -1.5, 1.5, 0], a=0.5, v=0.1)

else:
    # Handle invalid input
    popup("Invalid input. Please enter 'a' or 'b'.", "Error", False, True)
