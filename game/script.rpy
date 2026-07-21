# Elbi Dating Sim, entry point.

label start:

    scene bg signage
    with fade

    "University of the Philippines Los Baños."
    "They call it Elbi like it's a nickname you earn after your first wrong jeepney stop."

    $ player_name = renpy.input("What should people call you?", default="Isko", length=16)
    $ player_name = player_name.strip() or "Isko"

    jump prologue
