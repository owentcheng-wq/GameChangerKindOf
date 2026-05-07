# Variables go here
# Home team
HomeTeam = []
CatcherH = []
PitcherH = []
FirstBaseH = []
SecondBaseH = []
ShortStopH = []
ThirdBaseH = []
LeftFieldH = []
CenterFieldH = []
RightFieldH = []
# Away team
AwayTeam = []
CatcherA = []
PitcherA = []
FirstBaseA = []
SecondBaseA = []
ShortStopA = []
ThirdBaseA = []
LeftFieldA = []
CenterFieldA = []
RightFieldA = []
# The changing stuff
Balls = 0
Strikes = 0
Outs = 0
ScoreH = 0
ScoreA = 0
# Bases
base1 = 0
base2 = 0
base3 = 0
base4 = 0
# Functions
def Walk():
    global Balls, Strikes
    if Balls == 4:
        Balls = 0
        Strikes = 0
        print("Walk!")
def StrikeOut():
    global Balls, Strikes, Outs
    if Strikes == 3:
        Outs = Outs + 1
        Strikes = 0
        Balls = 0
        print("Out")
def Ball():
    global Balls        
    Balls = Balls + 1
    print("Ball!")
def Strike():
    global Strikes
    Strikes = Strikes + 1
    print("Strike!")
def Foul():
    global Strikes
    if Strikes < 2:
        Strikes = Strikes + 1
    print("Foul!")
def bases
    global base1, base2, base3, base4
    BaseRunners = input("How far did the runner go?(single, double, triple, home run)")
def PlayersNamesH():
    global FirstBaseH, SecondBaseH, ThirdBaseH, PitcherH, ShortStopH, CenterFieldH, RightFieldH, LeftFieldH
    place = input("Please enter a place on the field (first base, second base, etc.)")
    if place.lower().startswith("fi"):
        print(f"Hit to {FirstBaseH[0]}")
    if place.lower().startswith("se"):
        print(f"Hit to {SecondBaseH[0]}")
    if place.lower().startswith("sh"):
        print(f"Hit to {ShortStopH[0]}")
    if place.lower().startswith("th"):
        print(f"Hit to {ThirdBaseH[0]}")
    if place.lower().startswith("pi"):
        print(f"Hit to {PitcherH[0]}")
    if place.lower().startswith("le"):
        print(f"Hit to {LeftFieldH[0]}")
    if place.lower().startswith("ri"):
        print(f"Hit to {RightFieldH[0]}")
    if place.lower().startswith("ce"):
        print(f"Hit to {CenterFieldH[0]}")
def Hit():
    global Outs, Balls, Strikes
    SafeOrOut = input("Safe or Out?")
    SafeOrOut = SafeOrOut.lower()
    if SafeOrOut == "safe":
        print("Where did it go?\t")
        PlayersNamesH()
    else:
        print("Out!")
        Outs = Outs +1
        Strikes = 0
        Balls = 0
def PossiblePlays():
        global Balls, Strikes, Outs
        NextPlay = input("What happens next?\t")
        NextPlay = NextPlay.lower()
        if NextPlay == "ball":
            Ball()
        elif NextPlay == "strike":
            Strike()
        elif NextPlay == "foul":
                Foul()
        elif NextPlay == "hit":
            Hit()
    
        else:
            print("Enter a valid command")
# Home team
InputHome = input("Who is the home team?\t")
HomeTeam.append(InputHome)
InputCatcherH = input("Who is your catcher?\t")
CatcherH.append(InputCatcherH)
InputPitcherH = input("Who is your pitcher?\t")
PitcherH.append(InputPitcherH)
InputFirstH = input("Who is your first baseman?\t")
FirstBaseH.append(InputFirstH)
InputSecondH = input("Who is you second baseman\t")
SecondBaseH.append(InputSecondH)
InputShortH = input("Who is your shortstop?\t")
ShortStopH.append(InputShortH)
InputThirdH = input("Who is your third baseman?\t")
ThirdBaseH.append(InputThirdH)
InputLeftH = input("Who is your left fielder?\t")
LeftFieldH.append(InputLeftH)
InputCenterH = input("Who is your center fielder?\t")
CenterFieldH.append(InputCenterH)
InputRightH = input("Who is your right fielder?\t")
RightFieldH.append(InputRightH)
# Away team
InputAway = input("Who is the away team?\t")
AwayTeam.append(InputAway)
InputCatcherA = input("Who is your catcher?\t")
CatcherA.append(InputCatcherA)
InputPitcherA = input("Who is your pitcher?\t")
PitcherA.append(InputPitcherA)
InputFirstA = input("Who is your first baseman?\t")
FirstBaseA.append(InputFirstA)
InputSecondA = input("Who is you second baseman\t")
SecondBaseA.append(InputSecondA)
InputShortA = input("Who is your shortstop?\t")
ShortStopA.append(InputShortA)
InputThirdA = input("Who is your third baseman?\t")
ThirdBaseA.append(InputThirdA)
InputLeftA= input("Who is your left fielder?\t")
LeftFieldA.append(InputLeftA)
InputCenterA = input("Who is your center fielder?\t")
CenterFieldA.append(InputCenterA)
InputRightA = input("Who is your right fielder?\t")
RightFieldA.append(InputRightA)

print("Valid commands you can give are: ball, strike, foul, and hit")




while True:
    # Calling Functions
    Walk()
    StrikeOut()
    PossiblePlays()
    print(f"There are {Balls} balls and {Strikes} strikes")
    print(f"There are {Outs} outs.")

    if Outs == 3:
        print("Half-inning over!")
        
        break
if Outs == 3:
    Outs = 0
    Strikes = 0
    Balls = 0
