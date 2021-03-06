import networkx as nx
from parse import read_input_file, write_output_file
from utils import *
import sys
from os.path import basename, normpath
import glob
import copy
from solver import GreedySolver, convert_list, BranchAndBoundSolver
import multiprocessing as mp

def output_path(input_path):
    return 'medium/' + basename(normpath(input_path))[:-3] + '.out'


def solve(input_path):

    G, s = read_input_file(input_path)
    cool = BranchAndBoundSolver(G, s)
    cool.solve()
    solution = cool.best
    rooms = len(solution)
    D, k = convert_dictionary(solution), rooms
    assert is_valid_solution(D, G, s, k)
    happiness = calculate_happiness(D, G)
    print("{} Total Happiness: {}".format(output_path(input_path), happiness))
    write_output_file(D, output_path(input_path))


if __name__ == '__main__':
    inputs = glob.glob('inputs/medium/*')
    p = mp.Pool(mp.cpu_count())
    p.map(solve, [input_path for input_path in inputs])



