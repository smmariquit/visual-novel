# Three-afternoon dating loop around real campus spots.

label week_one_hub:

  if day > 3:
    jump endings_router

  scene expression "bg freedom_park"
  with fade

  "Day [day], after class. Pick a spot on campus."

  menu:
    "Where to?"

    "Freedom Park (Carillon)" if day < 3:
      $ last_hangout = "freedom_park"
      jump scene_freedom_park

    "Student Union (org fair chaos)" if day < 3:
      $ last_hangout = "student_union"
      jump scene_student_union

    "Carabao milk stall" if day < 3:
      $ last_hangout = "carabao_milk"
      jump scene_carabao_milk

    "DL Umali Hall" if day < 3:
      $ last_hangout = "umali_hall"
      jump scene_umali_hall

    "Mariang Makiling statue" if day < 3:
      $ last_hangout = "mariang_makiling"
      jump scene_mariang_makiling

    "Fertility Tree (don't laugh)" if day < 3:
      $ last_hangout = "fertility_tree"
      jump scene_fertility_tree

    "Palma Bridge at golden hour" if day == 3:
      $ last_hangout = "palma_bridge"
      jump scene_palma_bridge


label scene_freedom_park:

  scene bg carillon
  with dissolve

  "The bells don't ring on command, but the lawn is full anyway."

  menu:
    "Who do you look for?"

    "Jules, picnic spreadsheet in hand.":
      jules "I brought pandan bars and a ranked list of orgs by snack quality."
      menu:
        "How do you reply?"
        "Snack ranking is valid research.":
          $ aff_jules += 2
          jules "Peer-reviewed by my stomach."
        "Let's just lie on the grass.":
          $ aff_jules += 1
          jules "…Fine. Unscheduled joy. Don't tell my calendar."

    "Rafa, debating grass vs. lab soil.":
      rafa "Out here the soil is {i}resting.{/i} In the lab it's {i}judging.{/i}"
      menu:
        "Your take?"
        "Grass wins today.":
          $ aff_rafa += 2
          rafa "Truce accepted."
        "Lab soil is honest.":
          $ aff_rafa += 1
          rafa "Honest and passive-aggressive."

    "Thea, sketching leaves.":
      thea "Same tree, different light. Elbi teaches you to notice."
      $ aff_thea += 1
      menu:
        "Compliment the sketch.":
          $ aff_thea += 1
          thea "Keep that eye. The mountain likes patience."
        "Ask to walk to Marya Fountain after.":
          $ aff_thea += 2
          thea "Deal. Fountain mist is underrated."

  $ day += 1
  jump week_one_hub


label scene_student_union:

  scene bg student_union
  with dissolve

  org_tita "Another org fair day! Sign or perish!"

  jules "I told you they'd add a second booth for the same club."

  menu:
    "Today's move?"

    "Help Jules run the sign-up sheet.":
      $ aff_jules += 2
      jules "You prevented a pen shortage crisis."

    "Drag Sam into volunteering for AV.":
      sam "I fixed one cable and became 'the tech person' forever."
      $ aff_sam += 2

    "Escape with Rafa for merienda.":
      rafa "Union noise gives me hunger. Strategic retreat."
      $ aff_rafa += 2

  $ day += 1
  jump week_one_hub


label scene_carabao_milk:

  scene bg carabao_milk
  with dissolve

  rafa "Second cup? No judgment."

  menu:
    "While the line moves…"

    "Trade farm lab stories with Rafa.":
      $ aff_rafa += 2
      rafa "One carabao looked at my notebook like it owed money."

    "Text Sam to leave the server room.":
      sam "I brought my laptop. Don't tell anyone."
      $ aff_sam += 1
      menu:
        "Buy Sam a cup too.":
          $ aff_sam += 1
          sam "Bribery accepted."
        "Roast Sam's sleep schedule.":
          $ aff_sam += 2
          sam "Rude. Accurate."

    "Invite Thea to people-watch.":
      thea "Everyone's rushing. The milk line is the only honest queue."
      $ aff_thea += 2

  $ day += 1
  jump week_one_hub


label scene_umali_hall:

  scene bg umali_hall
  with dissolve

  "Umali's steps echo like every program rally happened here at once."

  menu:
    "Tonight's event?"

    "Sit with Sam, livestream duty.":
      $ aff_sam += 2
      sam "You muted the feedback loop. Hero behavior."

    "Jules is hosting, cheer embarrassingly.":
      $ aff_jules += 2
      jules "I will deny knowing you. affectionately."

    "Walk Thea home past the fountain.":
      scene bg marya_fountain
      with dissolve
      thea "Water sound beats jeepney horns. Thanks for the quiet."
      $ aff_thea += 2

  $ day += 1
  jump week_one_hub


label scene_mariang_makiling:

  scene bg mariang_makiling
  with dissolve

  thea "Mariang Makiling doesn't swipe right. She watches if you're kind."

  menu:
    "You…"

    "Leave a flower, not plucked, bought.":
      $ aff_thea += 2
      thea "Respect. The mountain remembers manners."

    "Invite Rafa to talk ag myths.":
      rafa "Makiling and farmers, old stories, still true enough."
      $ aff_rafa += 1
      $ aff_thea += 1

    "Challenge Sam to a photo pun contest.":
      sam "Mariang Makiling HDR when?"
      $ aff_sam += 1

  $ day += 1
  jump week_one_hub


label scene_fertility_tree:

  scene bg fertility_tree
  with dissolve

  "Students pretend not to stare at the Fertility Tree. Everyone stares."

  menu:
    "This is awkward. You…"

    "Make a tasteful joke with Jules.":
      jules "If legends raised GPAs, this campus would be undefeated."
      $ aff_jules += 2

    "Ask Thea for the botany facts.":
      thea "Samanea saman. Pretty crown. The myths are… louder than the science."
      $ aff_thea += 2

    "Dare Rafa to explain it to a tourist.":
      rafa "I chose agriculture, not tour guiding,  fine, I'll be professional."
      $ aff_rafa += 1

  $ day += 1
  jump week_one_hub


label scene_palma_bridge:

  scene bg palma_bridge
  with fade

  "Day 3 ends at Palma Bridge. Golden hour makes Elbi look like it planned this."

  $ crush, score = top_crush()

  if score < AFFECTION_WIN:
    jump ending_solo_study

  menu:
    "Your chest is loud. Who do you walk toward?"

    "Rafa" if aff_rafa >= AFFECTION_WIN:
      jump ending_rafa

    "Jules" if aff_jules >= AFFECTION_WIN:
      jump ending_jules

    "Sam" if aff_sam >= AFFECTION_WIN:
      jump ending_sam

    "Thea" if aff_thea >= AFFECTION_WIN:
      jump ending_thea

    "Keep it platonic for now":
      jump ending_solo_study
