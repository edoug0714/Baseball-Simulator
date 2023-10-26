import random as rand

def adjust_score(runners, result):
    rand.seed()
    #Dropped Third Strike
    if result == 'Strikeout' and runners[0] == 0:
        num = rand.randint(1, 100)
        if num < 3:
            batter = 'Batter reaches base on dropped third strike. '
            runners[0] = 1
            if runners[1] == 1:
                if runners[2] == 1:
                    second = ''
                else:
                    second = 'Runner on second advances to third. '
                    runners[2] = 1
            else:
                second = ''
            print(batter + second)
        else:
            runners[4] += 1

        return runners

    #Strikeout
    elif result == 'Strikeout':
        runners[4] += 1
        return runners

    #Walk
    elif result == 'Walk':
        runners[0] += 1
        for i in range(3):
            if runners[i] == 2:
                runners[i+1] += 1
                runners[i] = 1
        return runners

    #Single
    elif result == 'Single':
        if runners[2] == 1:
            third = 'Runner scores from third. '
            runners[2] = 0
            runners[3] += 1
        else:
            third = ''
        
        if runners[1] == 1:
            num = rand.randint(1, 100)
            if(num < 50):
                second = 'Runner scores from second. '
                runners[3] += 1
            else:
                second = 'Runner on second advances to third. '
                runners[2] = 1
                runners[1] = 0
        else:
            second = ''

        if runners[0] == 1:
            num = rand.randint(1, 100)
            if (num < 60) or (runners[2] == 1):
                first = 'Runner on first advances to second. '
                runners[1] = 1
            else:
                first = 'Runner on first advances to third. '
                runners[2] = 1
        else:
            first = ''

        runners[0] = 1
        if third + second + first != '':
            print(third + second + first)
        return runners

    #Double
    elif result == 'Double':
        if runners[2] == 1:
            third = 'Runner scores from third. '
            runners[2] = 0
            runners[3] += 1
        else:
            third = ''

        if runners[1] == 1:
            second = 'Runner scores from second. '
            runners[1] = 0
            runners[3] += 1
        else:
            second = ''

        if runners[0] == 1:
            num = rand.randint(1, 100)
            if num < 40:
                first = 'Runner scores from first. '
                runners[0] = 0
                runners[3] += 1
            else:
                first = 'Runner from first advances to third. '
                runners[0] = 0
                runners[2] = 1
        else:
            first = ''

        runners[1] = 1
        if third + second + first != '':
            print(third + second + first)
        return runners

    #Triple
    elif result == 'Triple':
        if runners[2] == 1:
            third = 'Runner scores from third. '
            runners[2] = 0 
            runners[3] += 1
        else:
            third = ''

        if runners[1] == 1:
            second = 'Runner scores from second. '
            runners[1] = 0
            runners[3] += 1
        else:
            second = ''

        if runners[0] == 1:
            first = 'Runner scores from first. '
            runners[0] = 0
            runners[3] += 1
        else:
            first = ''

        runners[2] = 1
        if third + second + first != '':
            print(third + second + first)
        return runners

    #Home Run
    elif result == 'Home Run':
        if runners[2] == 1:
            third = 'Runner scores from third. '
            runners[2] = 0
            runners[3] += 1
        else:
            third = ''

        if runners[1] == 1:
            second = 'Runner scores from second. '
            runners[1] = 0
            runners[3] += 1
        else:
            second = ''

        if runners[0] == 1:
            first = 'Runner scores from first. '
            runners[0] = 0
            runners[3] += 1
        else:
            first = ''

        runners[3] += 1

        if third + second + first != '':
            print(third + second + first)
        return runners

    #Fly Out
    elif result == 'Fly Out':
        first = ''
        second = ''
        third = ''
        batter = 'Batter flies out. '
        special = ''
        init_runs = runners[4]
        runners[4] += 1
        if runners[4] < 3:
            num = rand.randint(1, 100)
            if num < 30 and runners[2] == 1: #runner on 3rd advances
                runners[2] = 0
                third = 'Runner on third tags up. '
                if num < 3:
                    runners[4] += 1
                    third = third + 'Runner on third out at home. '
                else:
                    runners[3] += 1
                    third = third + 'Runner scores from third. '
                if runners[4] < 3:
                    if num < 20 and runners[1] == 1: #runner on 2nd advances
                        runners[1] = 0
                        second = 'Runner on second tags up. '
                        if third == 'Runner scores from third. ' and num < 3:
                            runners[4] += 1
                            second = second + 'Runner on second thrown out at third. '
                        else:
                            runners[2] = 1
                            second = second + 'Runner on second advances to third. '
        if runners[4] - init_runs == 2:
            special = 'Double play. '
        if special != '':
            print(special + '\n' + third + second + first + batter)
        else:
            print(third + second + first + batter)
        return runners
    
    #Ground Out
    elif result == 'Ground Out':
        runners[4] += 1

        return runners
        

        
        


    
                        

                                


                       
                        
                        
                        



    
    print('I reached the end :(')
    return runners
