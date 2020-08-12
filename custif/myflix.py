#!/usr/bin/env python3

print("\n* * * THE MYERS-BRIGGS TYPE INDICATOR * * *")

result = [1, 2, 3, 4]
counter = 0

while counter < 4:
    counter += 1
    if counter == 1:
        print("\n1.\tYou are totally exhausted because your week was endless and less than great. How are you going to spend your weekend? ")
        question1 = input("\t E.   Comedy is playing in the cinemas  there are big discounts at the paintball club. We should all go out together. \n\t I.   I'll switch on the 'Don't disturb' mode on my phone and stay at home. I'll watch a new episode of my favorite TV show, do a puzzle, and take a long bath with a book.")
        if question1.capitalize() == "E":
            result[0] = "E"
        elif question1.capitalize() == "I":
            result[0] = "I"
        else:
            print("\n!!!Invalid input. Enter E or I!!!")
            counter -= 1
    if counter == 2:
        print("\n2. Which of these 2 descriptions suits you more?")
        question2 = input("\t S.   The most important thing for me is what's happening here and now. I assess real situations and pay attention to details. \n\t N.   Facts are boring. I love to dream and play over upcoming events in my mind. I rely more on intuition than information.")
        if question2.capitalize() == "S":
            result[1] = "S"
        elif question2.capitalize() == "N":
            result[1] = "N"
        else:
            print("\n!!!Invalid input. Enter S or N!!!")
            counter -= 1
    if counter == 3:
        print("\n3. A competitor of your current employer is trying to entice you. You have doubts because the salary is much higher there, but the staff here is great. Moreover, the head of your department hinted that he will recommend you to the bosses when he retires. How are you going to make a decision?")
        question3 = input("\tT.   I'll learn all the available information about the competitor, ask my HR manager for advice, and draw a chart with all the pros and cons. In such cases, it's important to weigh up all the arguments and assess the situation with a cold mind.\n\tF.    I'll listen to my feelings. I always try to follow my heart.")
        if question3.capitalize() == "T":
            result[2] = "T"
        elif question3.capitalize() == "F":
            result[2] = "F"
        else:
            print("\n!!!Invalid input. Enter T or F!!!")
            counter -= 1
    if counter == 4:
        print("\n4. Only 2 weeks are left before your close friends' wedding. How are the preparations going?")
        question4 = input("\tJ.   One month ago, I chose the saxophonist who will play a medley of our school songs / collected the couple's photo love story / composed a poem / pressed my suit / made appointments with the stylist and makeup master. I prefer to be fully armed.\n\tP. Why prepare? I'll be having fun and enjoying myself at the party. I'll improvise my wedding speech. The best things happen spontaneously.")
        if question4.capitalize() == "J":
            result[3] = "J"
        elif question4.capitalize() == "P":
            result[3] = "P"
        else:
            print("\n!!!Invalid input. Enter J or P!!!")
            counter -= 1

print(result)
if ''.join(result) == 'ESTJ':
    print("\nMANAGER. Practical and consistent, you like to have order everywhere by planning and organizing everything. But most of all, you like to convince people of your rightness and make them think the way you think. You look at life soberly and, above all, trust facts. \nYou are open for communication, meeting new people, and spending time at parties. You never forget to take care of your close ones and can express your love very well. \n11% men, 6% women")
if ''.join(result) == 'ENTJ':
    print("\nCOMMANDER. Life for you is a struggle and extreme. This is how you know yourself and others. Being risky and brave, you are easily inspired to start something new. At the same time, you assess your abilities, both strengths and weaknesses, quite adequately. \nYou feel new tendencies very well and are open to new ideas. You think positively and adore sport and everything connected to it. \n3% men, 1% women")
if ''.join(result) == 'ESFJ':
    print("\nTEACHER. You get along with people very well, and you are the life of any party. You are attentive, caring, and always ready to help, even if you have to sacrifice your personal interests for others. \nYet you are very independent in your deals and, as a rule, you get everything without any side help. You only wait for emotional support from your close ones.\n17% women, 8% men")
if ''.join(result) == 'ESTP':
    print("\nMARSHAL. Participation is more important than victory. This is not about you. You strive to reach your goals by any means, even if you have to use physical strength. You stick to an exact plan, and you can't stand dependence and compromises.\nYou're a born fighter, very active and self-organized. You can objectively evaluate even the most stressful situation and give a quick and exact response.\n6% men, 3% women")
if ''.join(result) == 'ENFJ':
    print("\nMENTOR. You are emotional and talkative with rich facial expressions and gesticulations. You are very empathetic to other people's emotions, and you can spot even the tiniest insincerity. You are very jealous and distrustful in love relationships.\nVery often, you are ready to face upcoming events because of your ability to feel them in advance.\n3% women, 2% men")
if ''.join(result) == 'ENTP':
    print("\nINVENTOR. The generator of ideas, you are always seeking to create something new. You adapt easily to nonfamiliar environments and master different methods of work easily.\nDue to your dislike of traditions and routine, you very often change your professional spheres and hobbies, becoming an innovator and a pioneer. What is important about you is that not only can you create new ideas but you are also able to convey them to others and make them come true.\n4% men, 2% women")
if ''.join(result) == 'ESFP':
    print("\nPOLITICIAN. You can professionally determine the opportunities of your surroundings, and very often you use this skill to manipulate people. In communication with people, you primarily follow your personal interests. However, you try to impress everybody and create the image of a simple person.\nYou stand firmly in the present moment, and you don't like to waste time. You want quick results, disliking bureaucracy and red tape.\n10% women, 7% men")
if ''.join(result) == 'ENFP':
    print("\nCHAMPION. You are energetic and inquisitive, with very clear creative skills. You combine the features of both introverts and extroverts, which is why not only do you get along with people easily but you also empathize well. You are very good at advising.\nYou perceive life with all the diversity of its possibilities. You have a very rich imagination and a very high IQ. You're a very harmonious person, able to keep the balance even in a very quickly changing environment.\n10% women, 6% men")

if ''.join(result) == 'INFP':
    print("\nHEALER. A lyricist and dreamer, your inner harmony and self-agreement are always in first place. Most of your thinking happens deep inside of you. Nevertheless, you are able to foresee events and understand people well.\nYou like to dress up and try to look good in all circumstances. You can't be called thrifty, and you often lose sense of time and reality.\n5% women, 4% men")
if ''.join(result) == 'ISFP':
    print("\nCOMPOSER. You can find joy in simple things, handling routine and monotony easily. You like to feel needed, which is why you always help other people but never interfere with their comfort zone. You can't stand conflicts, and you can always entertain people and make them laugh.\nYou're a very down-to-earth, practical, caring, tender, reliable, and faithful partner. You take this world as it is, never trying to lead and manipulate.\n10% women, 8% men")
if ''.join(result) == 'INTP':
    print("\nARCHITECT. An egghead and philosopher, you don't like too much expressiveness. You always seek calm emotions and comfort. You're very careful when making decisions, preferring to analyze and find connections between the past, present, and future.\nYou are very sensitive to changes, and you don't handle them easily. You always try to collect all of your facts, thoughts, and ideas, and that's why you are very often tense.\n5% men, 2% women")
if ''.join(result) == 'INFJ':
    print("\nADVISOR. You are perfect at sensing people and their relationships. You can easily identify moods and hidden talents, which is why people seek advice from you. However, you are very vulnerable and can't stand aggression and lack of love.\nYour driving force is intuition, aimed not outside but inside. This type of person never stops learning, considering self-development to be a main priority. By getting to know yourself, you help others.\n2% women, 1% men")
if ''.join(result) == 'INTJ':
    print("\nINSPIRER. You have the richest inner world from where you get your incredible ideas. You strive for excellence and want to improve everything and everybody.\nHowever, you have some difficulties in relationships with people, very often distancing yourself intentionally to demonstrate your independence. You can set priorities and trust your intuition.\n3% men, 1% women")
if ''.join(result) == 'ISFJ':
    print("\nPROTECTOR. You can't stand falseness and insincerity in relationships. You distinguish 'strangers' and keep them at a distance right away. For the people 'inside your circle,' you do anything and never ask for anything in return.\nYou are observant and very careful with words and deeds. Kind and caring, you see your main goal as helping people and making them happier.\n19% women, 8% men")
if ''.join(result) == 'ISTP':
    print("\nHANDYMAN. The handyman, as a rule, has a technical mindset and likes to make things by hand. You don't hurry with taking decisions and think that it is better twice measured than once wrong. However, you always meet deadlines and you are very punctual by nature. You perceive this world through feelings, and your opinion of things happening around you is very objective and specific. By nature, you are communicative, but you will refuse communication once you feel insincerity.\n9% men, 2% women")
if ''.join(result) == 'ISTJ':
    print("\nINSPECTOR. Thoughtful, pensive, responsible. You are trustworthy, but you never take things as they are, always analyzing the incoming information. You are not interested in long-term communication and prefer official communication only during companionship. You are aimed at the final result.\nYou like strictness and order, and very often you are pedantic. You don't live in your dreams, only in the 'here and now.'\n15% men, 7% women")

