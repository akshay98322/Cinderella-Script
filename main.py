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
        if attitude_input == "A":
            print("Cinderella is hesitant and unsure of herself. She doesn't speak up for herself and often lets others walk all over her.")
        if attitude_input == "B":
            print("Cinderella is strong-willed and not afraid to stand up for herself. She speaks her mind and doesn't let others push her around.")
        if attitude_input == "C":
            print("Cinderella is gentle and caring, always putting others' needs before her own. She has a big heart and is beloved by all who know her.")
        break
    else:
        print("=> Please chose from below three options.")

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
        if attitude_input == "A":
            print("The blue dress is elegant and timeless, fitting for a royal ball. It shimmers in the light, catching the attention of all who see it.")
        if attitude_input == "B":
            print("The pink dress is soft and feminine, with delicate details that accentuate Cinderella's natural beauty. It makes her look like a fairy princess.")
        if attitude_input == "C":
            print("The silver dress is sleek and modern, a departure from the traditional ballgowns of the time. It makes Cinderella stand out in a sea of other guests.")
        break
    else:
        print("=> Please chose from below three options.")


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
        if attitude_input == "A":
            print("Cinderella and the prince share a magical moment on the dance floor. They connect on a deep level and sparks fly between them.")
        if attitude_input == "B":
            print("Cinderella is not interested in the prince and decides to steer clear of him for the rest of the night.")
        if attitude_input == "C":
            print("Cinderella strikes up conversations with other guests at the ball, enjoying their company and learning more about their lives.")
        break
    else:
        print("=> Please chose from below three options.")


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
        if attitude_input == "A":
            print("Cinderella decides to call it a night and leaves the ball early, perhaps feeling overwhelmed by the grandeur of it all.")
        if attitude_input == "B":
            print("Cinderella is having too much fun to leave and decides to stay at the ball, dancing and chatting with other guests.")
        break
    else:
        print("=> Please chose from below two options.")


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
        if attitude_input == "A":
            print("Cinderella decides to take a chance and reveal herself to the prince, hoping that he will feel the same connection that she does.")
        if attitude_input == "B":
            print("Cinderella decides to play it cool and not reveal herself to the prince, instead enjoying the mystery of their encounter and leaving him wanting more.")
        break
    else:
        print("=> Please chose from below two options.")

# ending
if character["attitude"] == "Kind and Compassionate" and character["dress"] == "Silver" and \
        character["prince"] == "The prince would like to dance with her" and \
        character["ball"] == "Stay at the Ball" and \
        character["strategy"] == "Cinderella reveal herself to Prince":
    print("Cinderella's heart raced as she stepped onto the ballroom floor in her shimmering silver dress. She felt nervous but determined to make the most of this chance to attend the grand ball. As she danced with the prince, she was struck by his kindness and charm. They talked and laughed throughout the evening, and she found herself drawn to him more and more.")
    print("")
    print("However, as the clock struck midnight, Cinderella knew she had to leave the ball before her magic wore off. She said a hasty goodbye to the prince and ran out of the castle, leaving behind a glass slipper in her haste.")
    print("")
    print("The next day, the prince went on a quest to find the mysterious woman who had captured his heart. He traveled from village to village, searching for the owner of the glass slipper. When he arrived at Cinderella's home, her stepmother and stepsisters tried to claim the slipper as their own. But when the prince saw Cinderella, he knew he had found his true love.")
    print("")
    print("In the end, Cinderella and the prince were married in a grand ceremony. They lived happily ever after, ruling the kingdom together with kindness and grace.")

elif character["attitude"] == "Confrontational" and character["dress"] == "Blue" and \
        character["prince"] == "The prince would like to talk to other guests" and \
        character["ball"] == "Leave the Ball Early" and \
        character["strategy"] == "Cinderella remains elusive":
    print("Cinderella felt out of place at the grand ball, surrounded by people who seemed to have everything she had ever wanted. She tried to talk to the prince, but he seemed more interested in the other guests. Disappointed, Cinderella decided to leave the ball early.")
    print("")
    print("As she walked through the gardens, she realized that she no longer wanted to spend her life trying to fit into someone else's world. Instead, she wanted to pursue her own dreams and find her own path in life.")
    print("")
    print("Cinderella decided to start her own business, making beautiful clothes and accessories for the people in her village. She worked hard and poured her heart and soul into every piece she created. Before long, her business grew and prospered, and she became known throughout the land for her talent and creativity.")
    print("")
    print("Years later, the prince visited Cinderella's shop, amazed by the beautiful creations he saw there. He apologized for overlooking her at the ball and asked for her forgiveness. But Cinderella had already found happiness and fulfillment in her own life, and she politely declined his offer.")
    print("")
    print("In the end, Cinderella continued to run her successful business and lived a joyful and fulfilling life on her own terms.")

else:
    print("Cinderella danced with the prince, but she couldn't shake the feeling that something was missing. He was "
          "charming and handsome, but he didn't quite spark the fire in her heart that she had been searching for.")
    print("")
    print("As the night wore on, Cinderella felt restless and decided to leave the ball early. On her way home, she stumbled upon a young man who was playing guitar and singing by the side of the road. She stopped to listen and was struck by his passion and talent.")
    print("")
    print("They struck up a conversation, and Cinderella learned that the young man was a traveling musician, making his way from town to town. They talked and laughed together, and before long, Cinderella knew that she had found the connection she had been searching for.")
    print("")
    print("Over the next few months, Cinderella and the musician traveled together, performing for crowds all across the land. They fell deeply in love, their passion for music and each other fueling their every moment.")
    print("")
    print("Years later, the prince came to visit Cinderella, hoping to win her heart once again. But when he saw the happiness and love that she had found with the musician, he knew he had lost his chance.")

print("############# THE END #############")
