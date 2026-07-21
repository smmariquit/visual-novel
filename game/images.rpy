# Explicit background definitions, photos live in images/bg/ (Wikimedia Commons).

image bg carabao_milk = "bg/carabao_milk.jpg"
image bg carillon = "bg/carillon.jpg"
image bg cem_monopteros = "bg/cem_monopteros.jpg"
image bg fertility_tree = "bg/fertility_tree.jpg"
image bg freedom_park = "bg/freedom_park.jpg"
image bg gate = "bg/gate.jpg"
image bg mariang_makiling = "bg/mariang_makiling.jpg"
image bg marya_fountain = "bg/marya_fountain.jpg"
image bg palma_bridge = "bg/palma_bridge.jpg"
image bg rainbow_lane = "bg/rainbow_lane.jpg"
image bg signage = "bg/signage.jpg"
image bg student_union = "bg/student_union.jpg"
image bg umali_hall = "bg/umali_hall.jpg"

# Dimmed variants for menus (bright Commons photos need a scrim).
image bg menu freedom_park = Composite(
    (1280, 720),
    (0, 0), "bg freedom_park",
    (0, 0), Solid("#000000c0"),
)

image bg menu student_union = Composite(
    (1280, 720),
    (0, 0), "bg student_union",
    (0, 0), Solid("#000000c0"),
)
