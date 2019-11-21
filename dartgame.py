from random import uniform
LEN_SQ = 2


def print_points(rad):
    print("You have hit the circle!")
    print("new radius: {}".format(rad))
    print("")


def is_in_circle(rad, points):
    ''' outputs if the set of points is in the circle '''
    # points: tuple in form (x, y)
    # rad: radius of circle
    # output: bool
    x = points[0]
    y = points[1]
    
    if (x**2 + y**2)**0.5 <= rad:
        return True
    else:
        return False


def next_rad(rad, points):
    ''' outputs the next radius based on the dart coordinates '''
    # rad: radius of current circle
    # points: tuple in form(x, y)
    # output: next radius
    x = points[0]
    y = points[1]
    h = (x**2 + y**2)**0.5
    new_rad = (rad**2 - h**2)**0.5
    return new_rad
    

def new_points():
    ''' Creates a new set of points '''
    x = uniform(-1, 1)
    y = uniform(-1, 1)
    tpl = (x, y)
    return tpl


def main():
    answers = ["yes", "no"] 
    print("DART GAME")
    
    start = input("Throw a dart?: ")
    while start not in answers:
        start = input("Throw a dart? (yes or no): ")

    if start == answers[0]:
        print("Initial radius: 1")
        score = 1
        radius = 1
        tpl = new_points()
        while is_in_circle(radius, tpl):
            score += 1
            radius = next_rad(radius, tpl)
            print_points(radius)
            tpl = new_points()
            
        print("You have missed the circle.")
        print("Score: {}".format(score))
    else:
        score = 0
        print("Exitting dart game.")


if __name__ == "__main__":
    main()

