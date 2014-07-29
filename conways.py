from lifegame import LifeGame
from visual import graph_show


def main():
    """runs my version of Conway's Game of Life"""
    xx = LifeGame()
    xx.show()
    grid = xx.get_board_state()
    graph_show(grid)
    brick = ["^" for i in xrange(30)]
    print brick
    for i in xrange(xx._num_batches):
        for j in xrange(xx._batch_size):
            try:
                xx.run_game()
            except KeyboardInterrupt:
                last_state = xx.get_board_state()
                f = open("newfile.txt", "w")
                for row in last_state:
                    f.write(row)
                f.close()

        xx.show()
        grid = xx.get_board_state()
        graph_show(grid)
        print brick
main()
