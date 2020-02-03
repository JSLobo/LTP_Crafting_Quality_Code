# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.
    def __init__(self, symbol, row, col):
        """ (Rat, str, int, int) -> NoneType

        A Rat with symbol, row and column.

        >>> rat = Rat('J', 2, 2)
        >>> rat.symbol
        'J'
        >>> rat.row
        2
        >>> rat.col
        2
        """

        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        """ (Rat, int, int) -> NoneType

        Set de Rat's row and col instance variables to the given row and column.

        >>> rat = Rat('J', 2, 2)
        >>> rat.set_location(2, 3)
        >>> rat.row
        2
        >>> rat.col
        3
        """

        self.row = row
        self.col = col

    def eat_sprout(self):
        """ (Rat) -> NoneType

        Add one to the rat's instance variable num_sprouts_eaten.

        >>> rat = Rat('J', 2, 2)
        >>> rat.eat_sprout()
        >>> rat.num_sprouts_eaten
        1
        """
        self.num_sprouts_eaten += 1

    def __str__(self):
        """ (Rat) -> str

        Return a string representation of the rat, in this format: symbol at (row, col) at enum_sprouts_eaten sprouts.

        >>> rat = Rat('J', 4, 3)
        >>> rat.eat_sprout()
        >>> rat.eat_sprout()
        >>> rat.__str__()
        'J at (4, 3) ate 2 sprouts.'
        """
        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol, self.row, self.col, self.num_sprouts_eaten)


class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    def __init__(self, maze, rat_1, rat_2):
        """ (Maze, list of list of str, Rat, Rat) -> NoneType

        A Maze with its contents, the first rat and second rat.

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                          ['#', '.', '.', '.', '.', '.', '#'], \
                          ['#', '.', '#', '#', '#', '.', '#'], \
                          ['#', '.', '.', '@', '#', '.', '#'], \
                          ['#', '@', '#', '.', '@', '.', '#'], \
                          ['#', '#', '#', '#', '#', '#', '#']], \
                          Rat('J', 1, 1), \
                          Rat('P', 1, 4))
        >>> maze.maze
        [['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']]
        >>> maze.rat_1.symbol
        'J'
        >>> maze.rat_2.symbol
        'P'
        >>> maze.num_sprouts_left
        3
        """
        sprouts_counter = 0
        for each_list in maze:
            for each_char in each_list:
                if each_char == SPROUT:
                    sprouts_counter += 1
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = sprouts_counter

    def is_wall(self, row, col):
        """ (Maze, int, int) -> bool

        Return True if and only if there is a wall at the given row and column of the maze.

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                          ['#', '.', '.', '.', '.', '.', '#'], \
                          ['#', '.', '#', '#', '#', '.', '#'], \
                          ['#', '.', '.', '@', '#', '.', '#'], \
                          ['#', '@', '#', '.', '@', '.', '#'], \
                          ['#', '#', '#', '#', '#', '#', '#']], \
                          Rat('J', 1, 1), \
                          Rat('P', 1, 4))
        >>> maze.is_wall(2, 2)
        True
        >>> maze.is_wall(2, 5)
        False
        """
        return self.maze[row][col] == WALL

    def get_character(self, row, col):
        """ (Maze, int, int) -> str

        Return the character in the maze at the given row and column.
        If there is a rat at that location, then its character should be returned rather than HALL.

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                          ['#', 'J', '.', '.', 'P', '.', '#'], \
                          ['#', '.', '#', '#', '#', '.', '#'], \
                          ['#', '.', '.', '@', '#', '.', '#'], \
                          ['#', '@', '#', '.', '@', '.', '#'], \
                          ['#', '#', '#', '#', '#', '#', '#']], \
                          Rat('J', 1, 1), \
                          Rat('P', 1, 4))
        >>> maze.get_character(1, 1)
        'J'
        >>> maze.get_character(1, 2)
        '.'
        """

        result = ''
        if self.maze[row][col] == HALL:
            result = HALL
        else:
            result = self.maze[row][col]
        return result

    def move(self, rat, ver_direc_change, hor_direc_change):
        """ (Maze, Rat, int, int) -> bool

        Move the rat in the given direction, unless there is a wall in the way.

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                          ['#', 'J', '.', '.', 'P', '@', '#'], \
                          ['#', '.', '#', '#', '#', '.', '#'], \
                          ['#', '.', '.', '@', '#', '.', '#'], \
                          ['#', '@', '#', '.', '@', '.', '#'], \
                          ['#', '#', '#', '#', '#', '#', '#']], \
                          Rat('J', 1, 1), \
                          Rat('P', 1, 4))
        >>> maze.move(maze.rat_1, DOWN, RIGHT)
        False
        >>> maze.num_sprouts_left
        4
        >>> maze.move(maze.rat_2, NO_CHANGE, RIGHT)
        True
        >>> maze.num_sprouts_left
        3
        """
        rat_row = rat.row
        rat_col = rat.col
        new_row_pos = rat_row + ver_direc_change
        new_col_pos = rat_col + hor_direc_change

        if self.is_wall(new_row_pos, new_col_pos):
            return False
        elif self.get_character(new_row_pos, new_col_pos) == SPROUT:
            rat.num_sprouts_eaten += 1
            self.maze[rat_row][rat_col] = HALL
            self.maze[new_row_pos][new_col_pos] = rat.symbol
            self.num_sprouts_left -= 1
            rat.set_location(new_row_pos, new_col_pos)
            return True
        else:
            self.maze[rat_row][rat_col] = HALL
            self.maze[new_row_pos][new_col_pos] = rat.symbol
            rat.set_location(new_row_pos, new_col_pos)
            return True

    def __str__(self):
        """ (Maze) -> str

        Return a string representation of the maze, using the format shown in this example:
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                          ['#', 'J', '.', '.', 'P', '.', '#'], \
                          ['#', '.', '#', '#', '#', '.', '#'], \
                          ['#', '.', '.', '@', '#', '.', '#'], \
                          ['#', '@', '#', '.', '@', '.', '#'], \
                          ['#', '#', '#', '#', '#', '#', '#']], \
                          Rat('J', 1, 1), \
                          Rat('P', 1, 4))
        >>> maze.__str__()
        '#######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.'
        """
        result = ''
        for each_list in self.maze:
            for each_char in each_list:
                result += each_char

            result += '\n'
        return '{0} {1} at ({2}, {3}) ate {4} sprouts.\n' \
               ' {5} at ({6}, {7}) ate {8} sprouts.'.format(result, self.rat_1.symbol, self.rat_1.row, self.rat_1.col,
                                                            self.rat_1.num_sprouts_eaten, self.rat_2.row, self.rat_2.symbol,
                                                            self.rat_2.col, self.rat_2.num_sprouts_eaten)


'''if __name__ == '__main__':
    import doctest

    doctest.testmod()'''
