from queue import Queue


class State:
    def __init__(self, num_of_objects, player1, player2):
        self.num_of_objects = num_of_objects
        self.player1 = player1
        self.player2 = player2

    def toString(self):
        return self.num_of_objects, self.player1, self.player2


# in this function we search the state space based on BFS
def search(values: list):
    print("regular search:")
    qu = Queue()
    new_qu = Queue()
    qu.put(State(0, 0, 0))  # insert the start state to the queue
    for i in range(0, len(values)):
        q_len = qu.qsize()
        for j in range(0, q_len):
            org_state = qu.get()
            print(org_state.toString())
            son_state1 = State(org_state.num_of_objects + 1, org_state.player1 + values[i],
                               org_state.player2)  # add the object to player1
            son_state2 = State(org_state.num_of_objects + 1, org_state.player1,
                               org_state.player2 + values[i])  # add the object to player1
            # insert the 2 new states to the queue
            qu.put(son_state1)
            qu.put(son_state2)
            new_qu.put(org_state)  # insert the original state to the final queue
    q_len = qu.qsize()
    # print the states from the last iteration and insert them to the queue
    for j in range(0, q_len):
        org_state = qu.get()
        print(org_state.toString())
        new_qu.put(org_state)
    print("the num of states is: " + str(new_qu.qsize()))
    return new_qu


# in this function we search the state space with the first pruning rule based on BFS
def search_with_pruning(values: list):
    print("search with pruning:")
    qu = Queue()
    new_qu = Queue()
    flag = False
    qu.put(State(0, 0, 0))  # insert the start state to the queue
    for i in range(0, len(values)):
        q_len = qu.qsize()
        for j in range(0, q_len):
            org_state = qu.get()
            print(org_state.toString())
            son_state1 = State(org_state.num_of_objects + 1, org_state.player1 + values[i],
                               org_state.player2)  # add the object to player1
            son_state2 = State(org_state.num_of_objects + 1, org_state.player1,
                               org_state.player2 + values[i])  # add the object to player1
            # insert the 2 new states to the queue
            qu.put(son_state1)
            qu.put(son_state2)
            # if this state does not already exist, put it in the final queue
            for k in range(0, new_qu.qsize()):
                curr = new_qu.get()
                if org_state.toString() == curr.toString():
                    flag = True
                new_qu.put(curr)
            if not flag:
                new_qu.put(org_state)
    q_len = qu.qsize()
    # print the states from the last iteration and insert them to the queue
    for j in range(0, q_len):
        org_state = qu.get()
        print(org_state.toString())
        new_qu.put(org_state)
    print("the num of states is: " + str(new_qu.qsize()))
    return new_qu


if __name__ == "__main__":
    search([20, 15, 12])
    search_with_pruning([20, 15, 12])
    search([33, 33, 12, 1])
    search_with_pruning([33, 33, 12, 1])
    search([5, 15, 25, 35])
    search_with_pruning([5, 15, 25, 35])
    search([10, 20, 30, 40])
    search_with_pruning([10, 20, 30, 40])

