from dartgame import is_in_circle, next_rad, new_points


def scoring():
    score = 1
    radius = 1
    tpl = new_points()
    while is_in_circle(radius, tpl):
        score += 1
        radius = next_rad(radius, tpl)
        tpl = new_points()

    return score


def main():
    expected_score = 2.1932800507380152
    lst_scores = [0]
    total_score = 0
    iterations = input("Enter number of iterations: ")
    while not iterations.isdigit():
        iterations = input("Enter number of iterations: ")

    for i in range(int(iterations)):
        inst_score = scoring()
        while inst_score > len(lst_scores):
            lst_scores.append(0)
        lst_scores[inst_score - 1] += 1
        total_score += inst_score

    avg_score = total_score / int(iterations)

    print("Total score: {}".format(total_score))
    print("Average score: {}".format(avg_score))
    print("Expected score: {}".format(expected_score))
    for i, score in enumerate(lst_scores):
        print("Total instances with score {}: {}".format(i+1, score))


if __name__ == "__main__":
    main()

    
