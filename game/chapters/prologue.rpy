# Arrival week, meet the campus before the dating loop.

label prologue:

  scene bg gate
  with dissolve

  "Jeepney fumes, merkado bags, and someone yelling {i}Sa LB po!{/i}"
  "You step down at the gate with a schedule you haven't memorized yet."

  menu:
    "Why did you come to Elbi, anyway?"

    "Agriculture runs in the family.":
      $ player_major = "agriculture"
      "Fields, labs, and the smell of rain on Molave. You can work with that."

    "Business orgs and spreadsheets.":
      $ player_major = "management"
      "You already downloaded three org fair flyers before unpacking."

    "Code, coffee, and all-nighters.":
      $ player_major = "computer science"
      "Your laptop is heavier than your reading load. For now."

    "Forestry. Trees over traffic.":
      $ player_major = "forestry"
      "Makiling is right there. That felt like a sign."

  scene bg freedom_park
  with fade

  "Freedom Park opens up past the crowd, Carillon in the distance, students on the grass like it's always been afternoon."

  show text "Day 1: Welcome Week" at truecenter with dissolve
  pause 1.5
  hide text with dissolve

  scene bg student_union
  with dissolve

  org_tita "Org fair! Sign up, get a free fan, regret nothing!"

  jules "If you take every flyer, you'll need a second backpack."
  $ met_jules = True

  player "You sound like you've seen casualties."

  jules "I'm Jules. CEM. I map org schedules so I only commit to {i}structured{/i} chaos."

  menu:
    "Jules hands you a color-coded campus map."

    "This is insanely helpful.":
      $ aff_jules += 2
      jules "Structured chaos is still chaos. But at least it's on time."

    "I'll wander and get lost on purpose.":
      $ aff_jules += 1
      jules "Classic freshie energy. Text me before you miss the last jeep."

  scene bg carabao_milk
  with fade

  rafa "First time trying carabao choco milk?"
  $ met_rafa = True

  player "Is there a wrong way?"

  rafa "Only if you skip it. I'm Rafa, CAFS. This line is basically orientation."

  menu:
    "The cup is cold and stupidly good."

    "Sit with Rafa and trade major horror stories.":
      $ aff_rafa += 2
      rafa "My prof asked for soil samples and I brought {i}feelings.{/i} We recovered."

    "Take a photo for the group chat.":
      $ aff_rafa += 1
      rafa "Post it with #Elbi, the algorithm already knows you're new."

  scene bg umali_hall
  with dissolve

  "DL Umali Hall looms like every program rally happened here at once."

  sam "If you're here for the free wifi, join the club."
  $ met_sam = True

  player "Is the wifi the club?"

  sam "Sam. ICS crowd. We pretend it's about the talks."

  menu:
    "Someone on stage tests the mic, feedback squeals."

    "Stay for the talk.":
      $ aff_sam += 2
      sam "Respect. Most people only come for the raffle."

    "Help Sam fix the livestream link.":
      $ aff_sam += 1
      sam "You just saved three group chats from panic."

  scene bg mariang_makiling
  with fade

  thea "You can hear the mountain if you stop talking."
  $ met_thea = True

  player "That's… actually true."

  thea "Thea. CFNR. Mariang Makiling isn't a backdrop, she's a reminder to look up."

  menu:
    "Wind through the trees."

    "Ask about the trails.":
      $ aff_thea += 2
      thea "Start easy. The mountain doesn't grade on a curve."

    "Admit you're scared of wrong turns.":
      $ aff_thea += 1
      thea "Then walk with someone who reads moss. You'll be fine."

  scene bg rainbow_lane
  with fade

  "On the way back you cross the rainbow pedestrian lane, small, loud, unmistakably Elbi."

  narrator "Three days of classes start tomorrow. Where you spend your afternoons is up to you."

  $ day = 1
  jump week_one_hub
