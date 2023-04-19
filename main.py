print("############# Welcome to the interactive story of Cinderella.. #############")

character = {}

# cinderella's attitude
while True:
    print("=> Please chose Cinderella's attitude")
    attitude_dict = {"A": "Meek and Submissive", "B": "Confrontational", "C": "Kind and Compassionate"}
    for key, value in attitude_dict.items():
        print(f"{key}. {value}")
    attitude_input = input()
    if attitude_input in ("A", "B", "C"):
        attitude = attitude_dict[attitude_input]
        print(f"--------> Our Cinderella is {attitude}.")
        character["attitude"] = attitude
        break
    else:
        print("=> Please chose from above three options.")

# Godmother's dress
while True:
    print("######################################################")
    print("=> Please chose Fairy Godmother's dress for Cinderella")
    dress_dict = {"A": "Blue", "B": "Pink", "C": "Silver"}
    for key, value in dress_dict.items():
        print(f"{key}. {value}")
    dress_input = input()
    if dress_input in ("A", "B", "C"):
        dress = dress_dict[dress_input]
        print(f"--------> Our Cinderella will wear a {dress} dress.")
        character["dress"] = dress
        break
    else:
        print("=> Please chose from above three options.")


# Prince's behaviour
while True:
    print("######################################################")
    print("=> What Prince would like to do with Cinderella")
    prince_dict = {"A": "The prince would like to dance with her", "B": "The prince will avoid her",
                   "C": "The prince would like to talk to other guests"}
    for key, value in prince_dict.items():
        print(f"{key}. {value}")
    prince_input = input()
    if prince_input in ("A", "B", "C"):
        prince = prince_dict[prince_input]
        print(f"--------> {prince}.")
        character["prince"] = prince
        break
    else:
        print("=> Please chose from above three options.")


# Cinderella's behaviour
while True:
    print("######################################################")
    print("=> Will Cinderella leave the ball early or stay until the end?")
    ball_dict = {"A": "Leave the Ball Early", "B": "Stay at the Ball"}
    for key, value in ball_dict.items():
        print(f"{key}. {value}")
    ball_input = input()
    if ball_input in ("A", "B"):
        ball = ball_dict[ball_input]
        print(f"--------> {ball}.")
        character["ball"] = ball
        break
    else:
        print("=> Please chose from above two options.")


# Cinderella's strategy
while True:
    print("######################################################")
    print("=> Shall Cinderella reveal herself to the prince?")
    strategy_dict = {"A": "Cinderella reveal herself to Prince", "B": "Cinderella remains elusive"}
    for key, value in strategy_dict.items():
        print(f"{key}. {value}")
    strategy_input = input()
    if strategy_input in ("A", "B"):
        strategy = strategy_dict[strategy_input]
        print(f"--------> {strategy}.")
        character["strategy"] = strategy
        break
    else:
        print("=> Please chose from above two options.")

# ending
if character["attitude"] == "Kind and Compassionate" and character["dress"] == "Silver" and \
        character["prince"] == "The prince would like to dance with her" and \
        character["ball"] == "Stay at the Ball" and \
        character["strategy"] == "Cinderella reveal herself to Prince":
    print("Cinderella and the Prince fall in love and get married.")

elif character["attitude"] == "Confrontational" and character["dress"] == "Blue" and \
        character["prince"] == "The prince would like to talk to other guests" and \
        character["ball"] == "Leave the Ball Early" and \
        character["strategy"] == "Cinderella remains elusive":
    print("Cinderella rejects the Prince and pursues her own dreams.")

else:
    print("Cinderella meets someone else at the ball and fall in love with him.")

print("############# THE END #############")
