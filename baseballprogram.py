ball_size = int(input("what is the size of the ball?: "))
ball_color = input("what color is the ball?: ")
ball_weight = int(input("how much does the ball weight?: "))
curve_ball = input("True or False: was it a curveball?: ")
fastball = input("True or False: was it a fastball?: ")
change_up = input("True or False: was it a changeup?: ")
strike = input("True or False: was it a strike?: ")

def regulation():
    if ball_weight == 5:
        print "the ball has a regulation weight."
    elif ball_weight > 5:
        print "the ball is water logged."
    else:
        print "the ball isn't regulation."

regulation()

if ball_color == "white":
    print "you have a pearl!"
else:
    print "that's an old ball :("



if fastball == True and strike == True:
    print "strike!"
elif curve_ball == True and strike == True:
    print "strike!"
elif change_up == True and strike == True:
    print "strike!"
else:
    print "ball"