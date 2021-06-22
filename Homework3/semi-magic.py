"""
Phang Teng Fone 1003296 A.I Coding Hw2
"""


from csp import *
import time
import pdb
from random import shuffle
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


def solve_semi_magic(algorithm=backtracking_search, **args):
    """ From CSP class in csp.py
        vars        A list of variables; each is atomic (e.g. int or string).
        domains     A dict of {var:[possible_value, ...]} entries.
        neighbors   A dict of {var:[var,...]} that for each variable lists
                    the other variables that participate in constraints.
        constraints A function f(A, a, B, b) that returns true if neighbors
                    A, B satisfy the constraint when they have values A=a, B=b
                    """
    # Use the variable names in the figure
    csp_vars = ['V%d' % d for d in range(1, 10)]  # ['V1','V2' ... 'V9']
    #########################################
    # Fill in these definitions

    csp_domains = {'V1': [1, 2, 3], 'V2': [1, 2, 3], 'V3': [1, 2, 3], 'V4': [1, 2, 3], 'V5': [
        1, 2, 3], 'V6': [1, 2, 3], 'V7': [1, 2, 3], 'V8': [1, 2, 3], 'V9': [1, 2, 3]}
    csp_neighbors = {'V1': ['V2', 'V3', 'V4', 'V7', 'V5', 'V9'],
                     'V2': ['V1', 'V3', 'V5', 'V8'],
                     'V3': ['V1', 'V2', 'V6', 'V9'],
                     'V4': ['V5', 'V6', 'V1', 'V7'],
                     'V5': ['V2', 'V8', 'V1', 'V9', 'V4', 'V6'],
                     'V6': ['V3', 'V9', 'V4', 'V5'],
                     'V7': ['V1', 'V4', 'V8', 'V9'],
                     'V8': ['V2', 'V5', 'V7', 'V9'],
                     'V9': ['V1', 'V5', 'V7', 'V8', 'V3', 'V6']}

    def csp_constraints(A, a, B, b):
        if a != b:
            return True

    #########################################

    # define the CSP instance
    csp = CSP(csp_vars, csp_domains, csp_neighbors,
              csp_constraints)

    # run the specified algorithm to get an answer (or None)
    ans = algorithm(csp, **args)

    print('number of assignments', csp.nassigns)
    assign = csp.infer_assignment()
    if assign:
        for x in sorted(assign.items()):
            print(x)
    return csp


"""
Pure BackTracking
"""
print("Pure BackTracking:")
timer = time.time()
solve_semi_magic()
print(f"Time taken: {time.time() - timer}s\n")

"""
Minimum-remaining-values heuristic.
"""
timer = time.time()
print("Minimum-remaining-values heuristic.")
solve_semi_magic(select_unassigned_variable=mrv)
print(f"Time taken: {time.time() - timer}s\n")

"""
Least-constraining-values
"""
timer = time.time()
print("Least-constraining-values")
solve_semi_magic(order_domain_values=lcv)
print(f"Time taken: {time.time() - timer}s\n")

"""
Minimum-remaining-values + least-constraining-values heuristic
"""
timer = time.time()
print("Minimum-remaining-values + least-constraining-values heuristic")
solve_semi_magic(select_unassigned_variable=mrv, order_domain_values=lcv)
print(f"Time taken: {time.time() - timer}s\n")

"""
Forward Checking
"""
timer = time.time()
print("Forward Checking")
solve_semi_magic(inference=forward_checking)
print(f"Time taken: {time.time() - timer}s\n")

"""
Maintain arc consistency
"""
timer = time.time()
print("Maintain arc consistency")
solve_semi_magic(inference=mac)
print(f"Time taken: {time.time() - timer}s\n")

"""
Minimum-remaining-values + least-constraining-values heuristic + maintaining arc consistency
"""
timer = time.time()
print("Minimum-remaining-values + least-constraining-values heuristic + maintaining arc consistency")
solve_semi_magic(select_unassigned_variable=mrv,
                 order_domain_values=lcv, inference=mac)
print(f"Time taken: {time.time() - timer}s\n")

"""
PART 3
Analysis

MRV requires 18 Assignments while MRV + LCV requires 21 Assignments, these numbers are not fixed and subjected to change per iteration.
Pure backtracking, LCV, Forward Checking, MRV + LCV + MAC requires only 9 assigments constantly.

-------------------------------------------------------------------------
Pure BackTracking VS MRV

BackTracking - 9 Assignments , 0.0009732246398925781s 
MRV - 18 Assignments , 0.0009975433349609375s

The reason why MRV takes in more assignments and a longer time to compute is because of the way csp.py introduce the algorithm.
Instead of reducing the number of variables with the constraint, it uses a minimal random function when faced with 
a tie. Furthermore it requires another step to check the variables if its not within the assignment values. Thus it spends more time and
more assignments. 

The constant assignments faced by pure backtracking is because of the choosing of variables are the same as the path of the solution.
-------------------------------------------------------------------------
Pure Backtracking VS LCV

BackTracking - 9 Assignments , 0.0009732246398925781s 
LCV - 9 Assignments, 0.0019948482513427734s

LCV choose the least constraining value but in return traverse the rest of the path
to determine what is the best value, as such it takes a longer time but this ensures the 
shortest path.
-------------------------------------------------------------------------
Forward Checking vs MAC

Forward Checking - 9 Assignments , 0.0009982585906982422s
MAC - 9 Assignments , 0.001994609832763672s

Both methods solves keep track of remaining legal values for unassigned variables in MRV.
However, forward checking does not provide early detection for all failures and will 
continue to propagate while AC3(MAC) enforce constraints locally. Since MAC iterates through
the entire tree EACH time a variable is visited, the time taken will be longer as compared to
Forward Checking but it also ensures the shortest assignments.
-------------------------------------------------------------------------
MRV + LCV

MRV + LCV - 18 Assignments , 0.001993417739868164s

MRV uses random selection during a tie while LCV only improve the chances of selecting the correct constraining path. As such
the time taken will be as of LCV which explores deeper while the assignment wise will be the same as the MRV.
-------------------------------------------------------------------------
MRV + LCV + MAC

MRV + LCV + MAC - 9 Assignments , 0.0019943714141845703s

As stated above, since MAC iterates through the entire tree EACH time a variable is visited, 
the time taken will be longer as compared to MRV and LCV. But guarentees the shortest assignments. 
-------------------------------------------------------------------------
"""