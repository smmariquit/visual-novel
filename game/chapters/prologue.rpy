# First playable chapter. Ren'Py loads every .rpy file under game/ automatically.

label prologue:

    scene bg room

    "Morning light filters through the window."

    show eileen happy

    alice "So you're really doing this—a visual novel from scratch."

    bob "One scene at a time. The engine handles the rest."

    menu:
        "Where should we start the story?"

        "Campus mystery":
            jump route_campus

        "Quiet slice-of-life":
            jump route_slice


label route_campus:

    alice "Good. Leave a clue in the first line and pay it off by chapter three."

    jump prologue_end


label route_slice:

    bob "Then keep the cast small and let the mood do the work."

    jump prologue_end


label prologue_end:

    "That's enough scaffolding for now. Edit chapters/prologue.rpy and add images to game/images/."

    return
