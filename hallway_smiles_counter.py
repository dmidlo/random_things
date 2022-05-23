"""
    How many people smile at each other in a hallway where all people smile at each
    new oncoming walker?
    
    a program that counts how many smiles are exchanged during a walk along
    a hallway. assuming that everyone gives a friendly smile to new on-comers.
    
    The hall is represented by a string. For example: "--->-><-><-->-"
     - in the above example, there are ten smiles
    
    string tokens:
        '>' -  person walking to the right
        '<' -  person walking to the left
        '-' -  an empty space.
    
    1. Whenever two people cross, each of them smiles nicely at the other.
    2  People continue walking until they reach the end, finally leaving the hallway.
    
    # Test cases
    # ==========
    
    # Input:
    # >>> get_total_smiles(">----<")
    # Output:
    #     2
    
    # Input:
    # >>> get_total_smiles("<<>><")
    # Output:
    #     4
    """
    import random
    from random import randint
    
    def get_total_smiles(hallway_str: str):
        """get_total_smiles(s): takes a string representing people walking along
           a hallway and returns the number of times the people smile at each other.
    
        Args:
            hallway_str (str): "--->-><-><-->-"
                               ">----<"
                               "<<>><"
                               "-<>-><--><-><----><"
                               "<<-<-->-<--<--<<->><<<<<<<->>-->-<---<<><->>->>-->>-"
    
        Returns:
            int: 10
                 2
                 4
                 28
                 100
        """
        people = hallway_str.replace("-","") # get rid of the dashes.
                                             #
                                             # We care about the people.
    
        people_list = list(people)  # turn the string into a list.
                                    # strings are immutable, lists are not.
                                    # going to iteratively check with the first
                                    # person on the left who is walking right and
                                    # count how many people they encounter.
                                    # for each encounter, there will be
                                    # two cordial smiles exchanged.
    
        def smile_counter(hallway: list):
            smiles = 0  # we haven't started counting smiles yet. :/
    
            while len(hallway) > 0:  # until we've counted each person heading right
                walker = hallway.pop(0)  # look at the person farthest left
    
                if walker == ">": # if our farthest left walker is heading left,
                                  # they are likewise exiting the left side of
                                  # the hallway and have already greeted everyone.
                                  # so we are only going watch the people heading
                                  # right. A binary split on the number of
                                  # people we're watching... cuts the number 
                                  # roughly in half.
    
                    for person in hallway:  # Then we look to see how many
                        if person == "<":   # people are heading towards us.
                            smiles += 2     # each person counts for 2 smiles
                                            # one for our walker, and one for 
                                            # other the person.
    
            # now that we've checked with each person walking right
            # we can send the total number of smiles to the caller
            return smiles
    
        return smile_counter(people_list)
    
    def random_hallway_generator(str_size: int, chars = "<>-"):
        """creates a random hallway of length == str_size: int
    
        Args:
            str_size (int): hallway length
            chars (str, optional): Allowed Characters. Defaults to "<>-".
    
        Returns:
            str: "-<>-><--><-><----><"
                 "<<-<-->-<--<--<<->><<<<<<<->>-->-<---<<><->>->>--
        """
        return ''.join(random.choice(chars) for _ in range(str_size))
    
    if __name__ == "__main__":
        hallways = [random_hallway_generator(randint(2, 100)) for _ in range(1, 10)]
    
        for h in hallways:
            print(h, get_total_smiles(h), ":)")
    
    
        # result_list = [get_total_smiles(h) for h in hallways]
        # zipped = zip(result_list, hallways)
        # print(list(zipped))
