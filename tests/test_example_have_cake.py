import unittest
from example_have_cake import have_cake
from run_search import run_search
from aimacode.search import (
    Node, breadth_first_search, astar_search, depth_first_graph_search,
    uniform_cost_search, greedy_best_first_graph_search, Problem,
)

class TestExample(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_add_action_level(self):
        p = have_cake()
        for a in p.actions_list:
            print('   {}{}'.format(a.name, a.args))
        print("Fluents in this problem are:")
        for f in p.state_map:
            print('   {}'.format(f))
        print("Goal requirement for this problem are:")
        for g in p.goal:
            print('   {}'.format(g))
        run_search(p, breadth_first_search)