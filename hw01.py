"""
DSC 20 Homework 01 SP21
Name: Weiyue Li
PID: (I did write my PID)
"""


# Question 1
def transcribe_names(coded_name):
    """
    ##############################################################
    # TODO: In this function, it will take in a string and return#
    # a list (two elements). I will first create an empty list,  #
    # which will store the names of player 1 and 2. I will then  #
    # create two string type variables, which will be the names  #
    # of the players. I will define a magic number 2 as "mod" to #
    # check if the index is odd or even in my future for loop.   #
    # After that, I performed a for loop. If the index is even,  #
    # I will add the element of the input string to player 1;    #
    # if the index is odd, I will add the element of the input   #
    # string to player 2. In the end, this function will return  #
    # a list, which contains two elements: name of both player 1 #
    # and player 2 in the order of player 1 and 2.               #
    ##############################################################

    >>> transcribe_names('S1h2r3o4u5d')
    ['Shroud', '12345']
    >>> transcribe_names('X')
    ['X', '']
    >>> transcribe_names('JMooee')
    ['Joe', 'Moe']

    # Add at least 3 doctests below here #
    >>> transcribe_names('')
    ['', '']
    >>> transcribe_names('abcdefg')
    ['aceg', 'bdf']
    >>> transcribe_names('ORGANICS')
    ['OGNC', 'RAIS']
    >>> transcribe_names('LamarJackson')
    ['Lmrako', 'aaJcsn']
    >>> transcribe_names('HoMeWoRkHiHoWaReYoU')
    ['HMWRHHWRYU', 'oeokioaeo']
    >>> transcribe_names('SYcaontgt')
    ['Scott', 'Yang']
    >>> transcribe_names('CWoalnign')
    ['Colin', 'Wang']
    >>> transcribe_names('HSutaenvienng')
    ['Huaning', 'Steven']
    >>> transcribe_names('LJaerrrryy')
    ['Larry', 'Jerry']
    """
    names = []
    player_1_name = ""
    player_2_name = ""
    mod = 2
    length = int(len(coded_name))
    for index in range(length):
        if index % mod == 0:
            player_1_name += str(coded_name[index])
        else:
            player_2_name += str(coded_name[index])
    names = [player_1_name, player_2_name]
    return names


# Question 2
def pick_legend(legend_1, legend_2, legend_3):
    """
    ##############################################################
    # TODO: This function will take in three strings, the longest#
    # of the three will be returned. If there is a tie, the one  #
    # that appears first will be returned.                       #
    # I will first define a variable called longest_name,        #
    # which I will make it ""(a string type) originally. I will  #
    # then create a list names which will have all 3 legends'    #
    # names. I will set up a for loop, if the element of index   #
    # has longer length of the previous longest_name, I will     #
    # replace it as the longest_name. I will return this final   #
    # longest_name as the longest name.                          #
    ##############################################################

    >>> pick_legend('Pathfinder', 'Loba', 'Fuse')
    'Pathfinder'
    >>> pick_legend('Revenant', 'Bangalore', 'Lifeline')
    'Bangalore'

    # Add at least 3 doctests below here #
    >>> pick_legend('', '', '')
    ''
    >>> pick_legend('a', 'b', 'c')
    'a'
    >>> pick_legend('ab', 'abcd', 'ac')
    'abcd'
    >>> pick_legend('Colin', 'Scott', 'Steven')
    'Steven'
    >>> pick_legend('Jordan', 'Kobe', 'Curry')
    'Jordan'
    >>> pick_legend('aBcDeFg', 'Tom', 'Lamer')
    'aBcDeFg'
    >>> pick_legend('Larry', 'lARRy', 'LARRY')
    'Larry'
    """
    longest_name = ""
    names = [legend_1, legend_2, legend_3]
    for i in range(int(len(names))):
        if len(names[i]) > len(longest_name):
            longest_name = names[i]
    return longest_name


# Question 3
def pick_legend_list(legend_list):
    """
    ##############################################################
    # TODO: This function will take in a list of strings, and the#
    # shortest one will be returned. If there is a tie, the one  #
    # appears first will be returned. If the list is empty, the  #
    # function will return an empty string.                      #
    # In the question, I will do similar stuff as in Q3:         #
    # I first defined an empty string variable shortest_name.    #
    # Then, I will use an if statement to determine if the list  #
    # is empty. If it is empty, the function will automatically  #
    # return an empty string ''. If it is not empty, I will first#
    # set the shortest_name to the first element of index. Just  #
    # like Q3, I use if statement and for loop to determine if   #
    # anything after the first element is shorter that it. If it #
    # it shorter, the shortest_name become the shorter element,  #
    # and we keep comparing until the end of the for loop.       #
    ##############################################################

    >>> pick_legend_list(['Bangalore', 'Caustic', 'Fuse', 'Lifeline', \
                          'Pathfinder', 'Revenant'])
    'Fuse'
    >>> pick_legend_list(['Loba', 'Fuse', 'Wraith'])
    'Loba'
    >>> pick_legend_list([])
    ''

    # Add at least 3 doctests below here #
    >>> pick_legend_list(['a', 'b', 'c', 'd'])
    'a'
    >>> pick_legend_list(['ab', 'b'])
    'b'
    >>> pick_legend_list(['','', 'a'])
    ''
    >>> pick_legend_list(['Larry', 'Jerry', 'JERRY', 'Colin', 'Scott'])
    'Larry'
    >>> pick_legend_list(['', ' ', '  ', '   '])
    ''
    >>> pick_legend_list(['      ', ' ', ''])
    ''
    """
    shortest_name = ""
    if int(len(legend_list)) > 0:
        shortest_name = legend_list[0]
        for i in range(int(len(legend_list))):
            if len(legend_list[i]) < len(shortest_name):
                shortest_name = legend_list[i]
    return shortest_name


# Question 4
def attack_player(player, health, damage, num_attacks, armor):
    """
    ##############################################################
    # TODO: This function will take in 5 parameters: player in   #
    # string, health, damage, num_attacks, armor in intergers. At#
    # the end of the function, it will either return the player  #
    # is eliminated or the remaining health. In details: I will  #
    # use if statement to determine if someone is eliminated or  #
    # not. I will set new variables:                             #
    # total_health is the sum of health and armor; total_damage  #
    # is the product of damage and number of attacks. The if     #
    # statement will do the following: if the total_damage is    #
    # greater or equal to the total_health, I will return that   #
    # person is eliminated; if not, then I will return that guy  #
    # has (total_health - total_damage) of health left.          #
    ##############################################################

    >>> attack_player('Wraith', 100, 10, 5, 0)
    'Wraith has 50 health remaining'
    >>> attack_player('Loba', 50, 25, 4, 50)
    'Loba is eliminated'

    # Add at least 3 doctests below here #
    >>> attack_player('Larry', 1000000, 10, 10, 1000000)
    'Larry has 1999900 health remaining'
    >>> attack_player('Cecilia', 0, 0, 0, 0)
    'Cecilia is eliminated'
    >>> attack_player('Albert', 1, 100, 0, 0)
    'Albert has 1 health remaining'
    >>> attack_player('Jerry', 500, 1000, 1, 1000)
    'Jerry has 500 health remaining'
    >>> attack_player('Scott', 1, -1000, 2, -1)
    'Scott has 2000 health remaining'
    """
    result = ""
    total_health = health + armor
    total_damage = num_attacks * damage
    if total_damage >= total_health:
        result = player + " is eliminated"
    else:
        new_health = int(total_health - total_damage)
        result = player + " has " + str(new_health) + " health remaining"
    return result


# Question 5
def average_damage(lst):
    """
    ##############################################################
    # TODO: The function will take in a list of string of numbers#
    # and will return the average of those numbers (round to the #
    # nearest integer) in the form of string.                    #
    # In particular, I first sum up all the elements in the list #
    # with their integer form. I also calculated the length of   #
    # the list. I use the sum devide the length to get their real#
    # average. I then round them down to the nearest integer by  #
    # using the int() built in function. I finally change them   #
    # into string, which result in the desired output.           #
    ##############################################################

    >>> average_damage(['205', '107', '51'])
    '121'
    >>> average_damage(['100'])
    '100'
    >>> average_damage(['5', '7', '5'])
    '5'

    # Add at least 3 doctests below here #
    >>> average_damage(['10', '12', '15', '19'])
    '14'
    >>> average_damage(['1', '79', '1004', '2058', '-100000'])
    '-19371'
    >>> average_damage(['18', '20', '109', '102', '183', '189'])
    '103'
    >>> average_damage(['15', '11', '19', '20', '-50'])
    '3'
    >>> average_damage(['1000', '1005', '2000', '1008'])
    '1253'
    """
    sum_of_list = 0
    length = int(len(lst))
    for i in range(length):
        sum_of_list += int(lst[i])
    average = int(sum_of_list / length)
    return str(average)


# Question 6
def best_score(first_player, first_data, second_player, second_data):
    """
    ##############################################################
    # TODO: This function will take in 4 parameters. A string, a #
    # list with three elements, a string, and a list with three  #
    # elements. The function will return the string (the player) #
    # that has higher number of elimination (index 1 in the list)#
    # if the elimination is the same, the player who has higher  #
    # number of index 2 (-1) will be returned. If the index of -1#
    # is still the same, if the index of 1 and -1 are both the   #
    # same, the first string(player's name) will be returned.    #
    # In particular, for this problem, I will use if statements. #
    # I will first see if both data's elimination is the same by #
    # comparing their index of 1. If they are not, the one who   #
    # has higher elimination will be best_score_player returned. #
    # If they are the same elimination and their damage(index -1)#
    # are different, the player who has higher damage will be    #
    # returned. If both of their elimination and damage are the  #
    # same, the first player will be returned just like what the #
    # instruction wanted.                                        #
    ##############################################################

    >>> best_score('Crypto', [3, 5, 267], 'Wraith', [2, 3, 100])
    'Crypto'
    >>> best_score('Lifeline', [1, 10, 498], 'Pathfinder', [2, 10, 500])
    'Pathfinder'
    >>> best_score('Crypto', [1, 5, 267], 'Wraith', [10, 7, 100])
    'Wraith'

    # Add at least 3 doctests below here #
    >>> best_score('A', [1, 3, 5], 'B', [2, 3, 5])
    'A'
    >>> best_score('A', [1, 3, 4], 'B', [2, 3, 5])
    'B'
    >>> best_score('A', [1, 1, 1], 'B', [1, 3, 1])
    'B'
    >>> best_score('A', [1, -5, -5], 'B', [1, -6, 5])
    'A'
    >>> best_score('A', [1, 0, 6], 'B', [1, 0, 3])
    'A'
    """
    elimination = 1
    damage = -1
    best_score_player = ""
    if first_data[elimination] != second_data[elimination]:
        if first_data[elimination] > second_data[elimination]:
            best_score_player = first_player
        else:
            best_score_player = second_player
    elif (first_data[elimination] == second_data[elimination]) \
            and (first_data[damage] != second_data[damage]):
        if first_data[damage] > second_data[damage]:
            best_score_player = first_player
        else:
            best_score_player = second_player
    elif (first_data[elimination] == second_data[elimination]) \
            and (first_data[damage] == second_data[damage]):
        best_score_player = first_player
    return best_score_player


# Question 7
def best_placement(first_player, first_data, second_player, second_data):
    """
    ##############################################################
    # TODO: This function will take two strings and two lists.   #
    # After logical comparison, the string associate with the    #
    # lower value of index 1 of the lists will be returned. If   #
    # they are the same, we will use the function from Q6 to     #
    # return the string.                                         #
    # In dataied, I will first compare if both player have the   #
    # same placement. If they do not, the player who has the     #
    # smaller placement will be returned. If they do, I will call#
    # the function from question 6 to determine which player     #
    # should be return. Just like question6, I will only use if  #
    # statements.                                                #
    ##############################################################

    >>> best_placement('Crypto', [3, 5, 267], 'Wraith', [2, 3, 100])
    'Wraith'
    >>> best_placement('Fuse', [1, 2, 167], 'Loba', [1, 3, 100])
    'Loba'

    # Add at least 3 doctests below here #
    >>> best_placement('A', [1, 3, 5], 'B', [2, 3, 5])
    'A'
    >>> best_placement('A', [1, 1, 1], 'B', [1, 3, 1])
    'B'
    >>> best_placement('A', [1, -5, -5], 'B', [1, -6, 5])
    'A'
    >>> best_placement('A', [500, 2, 3], 'B', [1, 2, 3])
    'B'
    """
    placement = 0
    best_placement_player = ""
    if first_data[placement] != second_data[placement]:
        if first_data[placement] < second_data[placement]:
            best_placement_player = first_player
        else:
            best_placement_player = second_player
    else:
        best_placement_player = best_score(first_player, first_data,
                                           second_player, second_data)
    return best_placement_player


# Question 8
def declare_winner(first_player, first_data, second_player, second_data):
    """
    ##############################################################
    # TODO: This function will take in four same parameters as   #
    # Question7. The function will return a statement such as:   #
    # Attention players,                                         #
    # The better player between player1 and player2 is           #
    #                                                            #
    # (player with best placement)                               #
    # In detailed, I will use the function defined in question 7.#
    # I will use \n\n to create the blackline desired. The       #
    # function from Q7 determines who has better placement, which#
    # will be returned.                                          #
    ##############################################################

    >>> print(declare_winner('Crypto', [3, 5, 267], 'Wraith', [2, 3, 100]))
    Attention players,
    The better player between Crypto and Wraith is
    <BLANKLINE>
    Wraith
    >>> print(declare_winner('Loba', [1, 5, 267], 'Fuse', [1, 10, 267]))
    Attention players,
    The better player between Loba and Fuse is
    <BLANKLINE>
    Fuse

    # Add at least 3 doctests below here #
    >>> print(declare_winner('A', [1, 3, 5], 'B', [2, 3, 5]))
    Attention players,
    The better player between A and B is
    <BLANKLINE>
    A
    >>> print(declare_winner('A', [1, 1, 1], 'B', [1, 3, 1]))
    Attention players,
    The better player between A and B is
    <BLANKLINE>
    B
    >>> print(declare_winner('A', [1, -5, -5], 'B', [1, -6, 5]))
    Attention players,
    The better player between A and B is
    <BLANKLINE>
    A
    >>> print(declare_winner('A', [500, 2, 3], 'B', [1, 2, 3]))
    Attention players,
    The better player between A and B is
    <BLANKLINE>
    B
    """
    winner = best_placement(first_player, first_data, second_player,
                            second_data)
    result = "Attention players,\n" \
             + "The better player between " + first_player + " and " + \
             second_player + " is\n\n" + winner
    return result


# Question 9
def in_zone(zone_1, zone_2, zone_3, zone_4, player_coord):
    """
    ##############################################################
    # TODO: This function will intake five lists of two integers,#
    # which the first four are the coordinates of bounds, and the#
    # last one is the coordinates of the player. The function    #
    # returns True if the player is within or on the bound of the#
    # four coordinates; False if the player is outsied the four  #
    # coordinates.                                               #
    # In particular, I will first use the index to find the      #
    # minimum/maximum value of x and y, which will help me set up#
    # two inclusive intervals. If both player's x and y are in   #
    # the two intervals, then the function returns True; else,   #
    # the function will return False. I can easily make the above#
    # conclusion because we are assuming the coordinates will be #
    # in the form of ractangles in this particular problem.      #
    ##############################################################

    >>> in_zone([1,2], [3,2], [1,4], [3,4], [1,2])
    True
    >>> in_zone([1,2], [3,2], [1,4], [3,4], [4,3])
    False
    >>> in_zone([1,2], [3,4], [3,2], [1,4], [2,3])
    True

    # Add at least 3 doctests below here #
    >>> in_zone([2,3], [4,3], [2,-2], [4,-2], [1,0])
    False
    >>> in_zone([-5,-6], [-5,2], [0,2], [0,-6], [-6,-6])
    False
    >>> in_zone([1,100], [50,100], [1,-100], [50,-100], [50,-100])
    True
    >>> in_zone([-7,-2], [-5,-2], [-7,6], [-5,6], [-6,6])
    True
    """
    zones = [zone_1, zone_2, zone_3, zone_4]
    min_x = zones[0][0]
    max_x = zones[0][0]
    min_y = zones[0][1]
    max_y = zones[0][1]
    for zone in range(int(len(zones))):
        if zones[zone][0] < min_x:
            min_x = zones[zone][0]
        if zones[zone][0] > max_x:
            max_x = zones[zone][0]
        if zones[zone][1] < min_y:
            min_y = zones[zone][1]
        if zones[zone][1] > max_y:
            max_y = zones[zone][1]
    if (min_x <= player_coord[0]) and (player_coord[0] <= max_x) and \
       (min_y <= player_coord[1]) and (player_coord[1] <= max_y):
        result = True
    else:
        result = False
    return result


# Question 10
def winner_list(winner, players):
    """
    ##############################################################
    # TODO: The function will take a string and a list of strings#
    # and return a list. In particular, I will use if statement  #
    # to test if the list is empty. If so, return a list with    #
    #"Empty list"; else, use for loop to append "Winner" and     #
    #"Loser" based of if the name each element in the list match #
    #the name of the winner given.                               #
    ##############################################################

    >>> winner_list('Wattson', ['Wraith', 'Revenant', 'Pathfinder', \
                    'Wattson'])
    ['Loser', 'Loser', 'Loser', 'Winner']
    >>> winner_list('Wattson', ['Mirage', 'Lifeline', 'Horizon'])
    ['Loser', 'Loser', 'Loser']

    # Add at least 3 doctests below here #
    >>> winner_list('A', ['A', 'B', 'C', 'D'])
    ['Winner', 'Loser', 'Loser', 'Loser']
    >>> winner_list('A', [])
    ['Empty list']
    >>> winner_list('A', ['B', 'C', 'D', 'E'])
    ['Loser', 'Loser', 'Loser', 'Loser']
    >>> winner_list('A', ['C', 'D', 'A'])
    ['Loser', 'Loser', 'Winner']
    """
    result_list = []
    length = int(len(players))
    if length > 0:
        for player in range(length):
            if players[player] == winner:
                result_list.append("Winner")
            else:
                result_list.append("Loser")
    else:
        result_list.append("Empty list")
    return result_list
