'''
Author: Uzio
Date: 2022-11-14 14:15:19
Email: 1336299411@qq.com
LastEditors:  
LastEditTime: 2022-11-14 21:27:36
Description: 
version:  
'''
import sys
import angr
import time
from timeit import timeit

def main():
    path_to_binary = "target\seed"
    project = angr.Project(path_to_binary)
    init_state = project.factory.entry_state(
        add_options = { angr.options.SYMBOL_FILL_UNCONSTRAINED_MEMORY,
                        angr.options.SYMBOL_FILL_UNCONSTRAINED_REGISTERS}
    )
    
    simgr = project.factory.simgr(init_state)

    #>> filters
    def found2stash(state:angr.SimState):
        stdO = state.posix.dumps(sys.stdout.fileno())
        print(f"found: {stdO}")
        time.sleep(0.3)
        return 'OK'.encode() in stdO

    # def avoid2stash(state:angr.SimState):
    #     stdO = state.posix.dumps(sys.stdout.fileno())
    #     # print(f"avoid: {stdO}")
    #     # time.sleep(1)
    #     return 'pass'.encode() in stdO

    #>> path explore
    simgr.explore(find=found2stash)
    
    #>> result
    if simgr.found: #* the FOUND_STASH is not None
        found_state = simgr.found[0]
        solution = found_state.posix.dumps(sys.stdin.fileno())
        print(f"{solution}")
    else:
        print("Could not find the solution")

if __name__ == '__main__':
    print(f"耗时：{timeit(main, number=1):.4f}s")