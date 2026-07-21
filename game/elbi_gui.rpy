## Menu readability over bright Wikimedia campus photos.

init 1 python:
    gui.main_menu_background = "bg menu freedom_park"
    gui.game_menu_background = "bg menu student_union"


screen main_menu():

    tag menu

    add gui.main_menu_background

    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style navigation_button:
    properties gui.button_properties("navigation_button")
    background Frame(Solid("#000000dd"), Borders(12, 12, 12, 12))
    padding (28, 14)
    xminimum 240

style navigation_button_text:
    properties gui.text_properties("navigation_button")
    color "#ffffff"
    bold True
    size 34
    outlines [(2, "#000000", 0, 0)]

style main_menu_title:
    properties gui.text_properties("title")
    color "#ffffff"
    bold True
    outlines [(3, "#000000", 0, 0), (1, "#000000", 2, 2)]

style main_menu_version:
    properties gui.text_properties("version")
    color "#e8e8e8"
    outlines [(2, "#000000", 0, 0)]

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 900
    yalign 0.38
    spacing 8
