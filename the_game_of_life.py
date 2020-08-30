print("""
Welcome to The Game of Life
Author- Yash Jaiswal, ig- @bitorsic
(Choices in this game define your character's personality)
Enter the number in front of the option to choose

Enter 'E' to Start
Enter 'Q' to Quit
""")


def starter():
    menu = input("> ")

    if menu == 'e' or menu == 'E':
        start()
    elif menu == 'q' or menu == 'Q':
        exit(0)
    else:
        error("strtr")


def start():
    print("You take birth in a pretty nice family. You're the only child.")

    cont("kndrgrtn")


def cont(sit):
    pin = sit

    print("\nEnter 'E' to continue")

    con = input("> ")

    if con == 'e' or 'E':
        if sit == "kndrgrtn":
            kindergarten()
        elif sit == "thrdgrd":
            third_grade()
        elif sit == "ffthgrd":
            fifth_grade()
        elif sit == "tnthgrd":
            tenth_grade()
        elif sit == "strm":
            stream()
        elif sit == "bsnsspprtnty":
            business_opportunity()
        elif sit == "sclsklls":
            social_skills()
        elif sit == "brn":
            brain()
        elif sit == "slfdfns":
            self_defense()
        elif sit == "stbbng":
            stabbing()
        elif sit == "fnl":
            finale()
        else:
            print("Continue function error; argument: ", sit)
            exit(0)
    else:
        print("I didn't quite get that. Please try again")

        cont(pin)


def error(sit):
    print("I didn't quite get that. Please try again\n")
    if sit == "strtr":
        starter()
    elif sit == "kndrgrtn":
        kindergarten()
    elif sit == "thrdgrd":
        third_grade()
    elif sit == "ffthgrd":
        fifth_grade()
    elif sit == "tnthgrd":
        tenth_grade()
    elif sit == "bsnsspprtnty":
        business_opportunity()
    elif sit == "sclsklls":
        social_skills()
    elif sit == "brn":
        brain()
    elif sit == "slfdfns":
        self_defense()
    else:
        print("Error handler crashed; argument: ", sit)


def end(ending):
    print(ending)
    print("The End\n")
    print("Enter 'E' to Restart")
    print("Enter 'Q' to Quit")

    starter()

s_skills = 0

def kindergarten():
    global s_skills

    print("It's your first day at pre-school. You're in Junior KG now.")
    print("""
A kid walks up to you and says hi. What do you do?
1. Say hi back
2. Ignore him
3. Punch him in the face
    """)

    kid = input("> ")

    if kid == "1":
        print("He becomes your very first friend and you enter the same school eventually.")
        print("Turns out, he's a pretty nice guy")

        s_skills = 1
    elif kid == "2":
        print("He seems pretty embarrassed but you carry on with your day.")

        s_skills = 0
    elif kid == "3":
        print("You broke a kid's nose on your very first day.")
        print("Eventually, your parents give up hope on you.")

        end("\nYou get caught for stabbing a person, and a few violent crimes in your adulthood and get sentenced for life\n")
    else:
        error("kndrgrtn")

    cont("thrdgrd")

strength = 0
intelligence = 0

def third_grade():
    global strength, intelligence

    print("You're now in 3rd grade (or 3rd standard as you'd like to say).")
    print("""
One fine evening, your friends call you to play football with them
But you have some homework pending
What do you do?
1. Play with them until dinner time
2. Deny and finish your homework
3. Play with them for an hour and return to finish my homework
    """)

    football = input("> ")

    if football == "1":
        print("You have a lot of fun with them")
        print("But you get punished the next day because of incomplete homework.")
        print("Such behavior ends up getting you bad grades at school")
        print("But multiple awards at sports")

        strength = 2
        intelligence = 0
    elif football == "2":
        print("Your friends continue their game without you")
        print("But you sit all evening and finish your homework.")
        print("Such behavior gets you the top rank in your class")
        print("But renders you physically very weak")

        strength = 0
        intelligence = 2
    elif football == "3":
        print("You play with them for a real nice hour")
        print("But get back to complete your homework.")
        print("Turns out the homework would've required more than the time you had after the game")
        print("So you get punished the next day for leaving it incomplete.")
        print("A few years down the line, you have a very balanced lifestyle")
        print("With pretty good grades and a few sports awards under your sleeves.")

        strength = 1
        intelligence = 1
    else:
        error("thrdgrd")

    cont("ffthgrd")


def fifth_grade():
    global s_skills, strength

    print("Well, you're in 5th grade now.")
    print("""
It's break time and you see a classmate being bullied by someone
Looks like an 8th grader at least
What do you do?
1. Intervene
2. Walk away
3. Join the bully
    """)

    bully = input("> ")

    if bully == "1":
        if strength == 0:
            print("Oof. The bully beat you both guys up pretty good.")
            print("But the classmate appreciates your intervention and becomes a good friend.")
        elif strength == 1:
            print("The bully thinks of getting physical with you.")
            print("You had a rough fight, you have a few bruises now.")
            print("After a lot of time in the principal's office, he takes your side and outright expels the bully.")
            print("You have a brave image in front of your school now.")
        elif strength == 2:
            print("The bully tried punching you as well, but you dodge it and land him a KO punch.")
            print("But you have a new friend and the bully gets suspended after some explanation.")
            print("Your school now understands that despite being bad at studies, you're good at heart.")
        else:
            print("5th std 1st choice error")
            exit(0)

        s_skills = 1
    elif bully == "2":
        print("You plain ignore the event.")
        if s_skills == 1:
            print("Your childhood friend sees you walking away and steps in by himself instead.")
            print("He gets mad at you for being such a coward.")
        else:
            print("Poor guy gets beat up for no reason at all.")

        s_skills = 0
    elif bully == "3":
        print("You humiliate the classmate and you get caught by a teacher.")
        print("The principal expels both you and the bully.")
        print("The bully befriends you and you get involved in criminal stuff in your adulthood.")

        end("\nYou eventually get arrested for serial killings and are sentenced for life.\n")
    else:
        error("ffthgrd")

    cont("tnthgrd")

boards = 0

def tenth_grade():
    global intelligence, strength, boards

    print("You're in 10th standard now. The turning point of your life, they say.")
    if intelligence == 0:
        print("""
Your school's football team desperately needs you this year.
What do you do?
1. Deny and focus on my boards
2. Join in. This is our year at the nationals
        """)
    elif intelligence == 1:
        print("""
Your parents ask you if you wanna attempt for a scholarship examination
Which would require you to study stuff not in your boards syllabus
While your school's football team asks you to play goalie.
What do you do?
1. Deny both and just focus on my boards
2. Play goalie for my school's team. I'm the best they've got. I guess?
3. Take the scholarship exam. No harm attempting
        """)
    elif intelligence == 2:
        print("""
Your parents urge you to participate in a scholarship examination
Which would require you to study stuff not in your boards syllabus
What do you do?
1. Deny and focus on the boards
3. The scholarship examination should be a breeze
        """)

    tenth = input("> ")

    if tenth == "1":
        if intelligence == 0:
            print("You pass the boards with average marks. Good job!")

            boards = 1
        elif intelligence == 1:
            print("You pass the boards with pretty good marks. Nicely done!")

            boards = 2
        elif intelligence == 2:
            print("Woah! You topped throughout the state. The media's all over you.")

            boards = 2
        else:
            print("10th std 1st choice error")
            exit(0)

        print("\nIt's now been a month and everyone's stopped caring about your boards results.")
    elif tenth == "2":
        if intelligence == 0:
            print("Your school gets the gold medal at the nationals this year. Great job!")
            print("You earned your school and yourself an excellent reputation.")
            print("You pass your boards, but really bad scores.")

            boards = 0
        elif intelligence == 1:
            print("Your team lands 3rd place, gets a bronze. Well played!")
            print("You earned your school and yourself a decent reputation.")
            print("You pass boards with average marks. Nice!")

            boards = 1
        elif intelligence == 2:
            error("tnthgrd")
        else:
            print("10th std 2nd choice error")
            exit(0)

        print("\nIt's now been a month and everyone's stopped caring about your boards results.")
    elif tenth == "3":
        if intelligence == 0:
            error("tnthgrd")
        elif intelligence == 1:
            print("Well, nothing fancy but you earned yourself a bit of scholarship. Good job!")
            print("You received sorta average scores in the board examinations.")

            boards = 1
        elif intelligence == 2:
            print("Oh look at you. You're the district topper for both")
            print("The scholarship exam as well as your boards.")

            boards = 2
        else:
            print("10th std 3rd choice error")
            exit(0)

        print("\nIt's now been a month and everyone's stopped caring about your boards results.")
    else:
        error("tnthgrd")

    cont("strm")


def stream():
    global boards

    print("Now you gotta pick the stream for 11th and 12th:")

    if boards == 0:
        print("\n1. Arts")
    elif boards == 1:
        print("""
1. Arts
2. Commerce
        """)
    elif boards == 2:
        print("""
1. Arts
2. Commerce
3. Science
        """)
    else:
        print("Stream choice error")

    path = input("> ")

    if path == "1":
        print("You choose a field you like in the arts stream and graduate in it.")
        print("Your parents seem disappointed, but whatever.")
    elif path == "2":
        if boards > 0:
            print("You choose a field you like in the commerce stream and graduate in it.")
        elif boards == 0:
            error("strm")
        else:
            print("Stream 2nd choice error")
            exit(0)

        print("Your parents seem a bit disappointed, but it's your choice.")
    elif path == "3":
        if boards > 1:
            print("You chose a field you like in the science stream and graduate in it.")
        elif boards < 2:
            error("strm")
        else:
            print("Stream 3rd choice error")
            exit(0)

        print("Exactly like your parents wanted.")

    print("\nYou finish the course(s) you wanted to and landed an awesome job.")
    print("You get married to the person you liked.")
    print("You're so good at your job that you rapidly climb the ladder of promotions.")

    cont("bsnsspprtnty")


def business_opportunity():
    print("A fine day, your boss calls you in his office.")
    print("He says he recognizes a huge potential in you.")
    print("Being a businessman himself, he offers to provide you with mentorship to turn your job/hobby into a business")
    print("Which means you would have to leave your job, which you're doing very good at, eventually.")
    print("""
What do you do?
1. Agree
2. Deny
    """)

    offer = input("> ")

    if offer == "1":
        print("You, under his mentorship, establish a successful startup.")
        print("Watching it become successful, you leave your job to go full time on it.")
    elif offer == "2":
        print("You deny the offer and decide to work hard at your job.")
        print("Years down the line, you finally acquire the topmost position at your job")
        print("And earn yourself a huge salary.")
        print("You retire in your old age.")
        end("""
Fast forward, you're in your deathbed.
You've earned everything an ordinary person would've thought of.
You die peacefully.
        """)
    else:
        error("bsnsspprtnty")

    cont("sclsklls")


def social_skills():
    global s_skills

    if s_skills == 0:
        print("Your boss, now mentor, notices your way with other people.")
        print("He notices you lack social skills a lot.")
        print("""
He offers to train you to gain some communication skills
And explains how important they would be as a businessman.
What do you do?
1. Agree
2. Deny
        """)

        train = input("> ")

        if train == "1":
            print("He gives you lessons, hooks you up with other businessmen/women")
            print("So you could communicate and learn from them.")
            print("This potentially improves your interaction with clients.")

            s_skills = 1
        elif train == "2":
            print("Even after an half hour long explanation")
            print("On how this would improve you as a person, you deny the offer.")
            end("""
Eventually, you lose a majority of your clients.
Your business slowly goes bankrupt.
You had to shut it down and join for a job somewhere.

Decades later, you're on your deathbed, had most of the things an ordinary person wants
But die with a small regret of denying your mentor.
            """)
        else:
            error("sclsklls")
    elif s_skills == 1:
        print("Having the social skills, you form healthy relations with your clients,")
        print("Befriend a lot of fellow businessmen/women which eventually help you on your way to success.")
    else:
        print("Social skills error")
        exit(0)

    cont("brn")


def brain():
    global intelligence

    if intelligence < 2:
        print("You notice that you're not smart enough to gather knowledge on your own from various sources on business.")
        if intelligence == 0:
            print("""
What do you do?
1. Take a detailed, long duration course on business education
2. Contact my mentor to teach me more about business as fast as possible
3. Continue reading from various sources
            """)
        elif intelligence == 1:
            print("""
What do you do?
1. Take a detailed, long duration course on business education
3. Continue reading from various sources
            """)
        else:
            print("Business education options error")
            exit(0)

        knowledge = input("> ")

        if knowledge == "1":
            print("It takes you years to finish the course but at the end,")
            print("But now you have formal education and the confidence to run your business efficiently.")

            intelligence = 2
        elif knowledge == "2":
            if intelligence == 0:
                print("Your mentor teaches you the advanced terminology of business as fast as possible")
                print("He's done with all he could do. That should be enough for you to survive in your business.")

                intelligence = 1
            else:
                error("brn")
        elif knowledge == "3":
            print("You try gathering as much knowledge in the way you did before.")
            print("Unfortunately, doing that is not enough.")
            end("""
Your business slowly goes bankrupt.
You had to shut it down and join for a job somewhere.

Decades later, you're on your deathbed, had most of the things an ordinary person wants
But die with a small regret of not seeking proper education.
            """)
        else:
            error("brn")
    elif intelligence == 2:
        print("Being an intelligent person, you know what courses to take and what to ask your mentor")
        print("In order to keep your knowledge sufficient enough to run the business efficiently")
        print("And you do the same.")
    else:
        print("Business education error")
        exit(0)

    cont("slfdfns")


def self_defense():
    global strength

    if strength < 2:
        if strength == 0:
            print("You're getting fat with all the inactivity since childhood.")
            print("""
Your spouse suggests you pay attention towards your health and diet
What do you do?
1. Agree and join a self-defense class
2. Agree and join a gym
3. Ignore
            """)
        elif strength == 1:
            print("Even though you work out, you feel it ain't enough to defend yourself in a tense situation.")
            print("""
Your spouse suggests you join some self-defense classes
What do you do?
1. Agree
3. Ignore
            """)
        else:
            print("Self defense choices error")

        health = input("> ")

        if health == "1":
            print("You lose your weight, are shredded af, and your reflexes are on point.")
            print("Working throughout the days is much easier now.")

            strength = 2
        elif health == "2":
            if strength == 0:
                print("You lose your weight, are shredded, but feels like you're missing the flexibility.")

                strength = 1
            else:
                error("slfdfns")
        elif health == "3":
            print("You ignore your spouse and yourself, add up a few more kilograms to your weight,")
            print("a few more calories in your diet. You're fat(ter) and miserable.")

            strength = 0
        else:
            error("slfdfns")
    elif strength == 2:
        print("Being involved in sports and fitness since childhood, you know how important it is to keep yourself fit and sharp.")
        print("Hence, you join a self defense class. So you're fit, and always on your toes.")
    else:
        print("Self defense error")

    cont("stbbng")


def stabbing():
    global strength

    print("You're walking back home from your establishment as usual.")
    print("It's dark and spooky.")
    print("You run into a person. He seems sketchy.")
    print("He recognizes you as your business is very successful by now")
    print("But he pulls out a knife. He's about to stab you.")

    if strength == 0:
        end("""
Unfortunately, your reflexes kick in way too late, after you're stabbed
The knife makes contact with your heart, leaving you to the ground
He runs away. You call for help but no one's in your vicinity
You lose a lot of blood and drift into unconsciousness
        """)
    elif strength == 1:
        print("""
Your reflexes kick in at about the right time.
You don't know what to do so you punch and try to maintain distance.
He closes in on you quick.
You get stabbed a few times from the side, but a few punches in his face and he's down.
You call emergency services ASAP.
The man gets arrested and gets jailed with a long history.
A few weeks in the hospital and you're good to go.
        """)
    elif strength == 2:
        print("""
You were prepared for this as your classes did include defending yourself from an armed person
Your reflexes kick in and exactly as you practiced multiple times,
You put him down for good.
You call the emergency services and turns out he had a long history of crimes.
So he gets sentenced.
Your family's happy to see you safe.
        """)
    else:
        print("Stabbing incident error")

    cont("fnl")


def finale():
    global intelligence

    if intelligence == 1:
        end("""
You give your business all you could. It brings you profits like crazy
But you reach a point, you plateau, where however much you put in, your profits don't increase
You reach your old age. You slowly become unable to manage this business.
Well, you can't get your kids to manage it as they do jobs/businesses they love.

Luckily for you, at the right time,
A giant company decides offers to buy your business for way much more than it's worth.
In your deathbed, you feel you've accomplished a lot in this life.
You die in peace.
        """)
    elif intelligence == 2:
        end("""
Your business is a huge hit. It's all over the world.
Many publishers are restless to interview you.
You hit the Forbes' list of richest people in the world.
Many other companies try buying yours but you know it's true worth.

In your deathbed, you rest with a wide smile,
Knowing you'd accomplished all a human ever could.
You rest in peace.
        """)
    else:
        print("Finale error")
        exit(0)

starter()
