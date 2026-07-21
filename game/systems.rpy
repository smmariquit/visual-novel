# Affection and calendar state for the Elbi dating loop.

default day = 0
default week_label = "Welcome Week"

default aff_rafa = 0
default aff_jules = 0
default aff_sam = 0
default aff_thea = 0

default met_rafa = False
default met_jules = False
default met_sam = False
default met_thea = False

default player_major = "undeclared"
default last_hangout = ""

init python:
    AFFECTION_WIN = 5

    def top_crush():
        scores = [
            ("rafa", aff_rafa),
            ("jules", aff_jules),
            ("sam", aff_sam),
            ("thea", aff_thea),
        ]
        scores.sort(key=lambda pair: pair[1], reverse=True)
        return scores[0]

    def bump_affection(who, amount=1):
        store = renpy.store
        var = "aff_" + who
        if hasattr(store, var):
            setattr(store, var, getattr(store, var) + amount)
