# Route endings, still no AI portraits, just campus photos and dialogue.

label endings_router:
  jump scene_palma_bridge


label ending_rafa:

  scene bg carabao_milk
  with dissolve

  rafa "You keep showing up where the soil and the snacks are honest."

  player "Is that your way of asking me out?"

  rafa "It's my way of saying tomorrow's line is long. Save me a spot?"

  scene bg freedom_park
  with fade

  "You date in daylight, org fairs, field labs, jeepney debriefs."
  "Elbi stays loud. Somehow you hear each other anyway."

  "Ending: {b}Carabao Milk & Field Notes{/b} (Rafa)"

  return


label ending_jules:

  scene bg cem_monopteros
  with dissolve

  jules "I made a shared calendar. Pink for dates, yellow for exams, green for sleep you'll actually get."

  player "You color-coded romance."

  jules "Romance without logistics is just anxiety."

  scene bg rainbow_lane
  with fade

  "You cross the rainbow lane holding hands like it's the most organized rebellion."

  "Ending: {b}Structured Chaos{/b} (Jules)"

  return


label ending_sam:

  scene bg umali_hall
  with dissolve

  sam "I wrote you into my deploy script. Metaphorically. Mostly."

  player "That's the nerdiest confession I've gotten."

  sam "Wait till you see the git commit message."

  scene bg student_union
  with fade

  "Your dates are half coffee, half fixing AV cables. Somehow that's love."

  "Ending: {b}Patch Notes & Pandesal{/b} (Sam)"

  return


label ending_thea:

  scene bg marya_fountain
  with dissolve

  thea "The mountain doesn't rush. I won't either."

  player "Is that a yes to more walks?"

  thea "It's a yes to listening. The rest follows."

  scene bg mariang_makiling
  with fade

  "You learn trail names, fountain mist, and how to be still between classes."

  "Ending: {b}Mist & Makiling{/b} (Thea)"

  return


label ending_solo_study:

  scene bg freedom_park
  with fade

  "No confession on the bridge. Just you, a reading list, and jeepney fare home."

  "Elbi is still huge. You've got semesters left to figure out the rest."

  "Ending: {b}Solo Grind (for now){/b}"

  return
