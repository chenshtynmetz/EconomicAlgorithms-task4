
class State:
    def __init__(self, num_of_objects, player1, player2):
        self.num_of_objects = num_of_objects
        self.player1 = player1
        self.player2 = player2

    def toString(self):
        return self.num_of_objects, self.player1, self.player2


def search(values: list):
    """
    in this function search the state space based on BFS. the function get a list of valuse for any object and return
    list of all the existing states.

    >>> [search([2, 5])]
    the num of states is: 7
    [[(0, 0, 0), (1, 2, 0), (1, 0, 2), (2, 7, 0), (2, 2, 5), (2, 5, 2), (2, 0, 7)]]

    >>> [search([0, 15])]
    the num of states is: 7
    [[(0, 0, 0), (1, 0, 0), (1, 0, 0), (2, 15, 0), (2, 0, 15), (2, 15, 0), (2, 0, 15)]]

    >>> [search([20, 15, 12])]
    the num of states is: 15
    [[(0, 0, 0), (1, 20, 0), (1, 0, 20), (2, 35, 0), (2, 20, 15), (2, 15, 20), (2, 0, 35), (3, 47, 0), (3, 35, 12), (3, 32, 15), (3, 20, 27), (3, 27, 20), (3, 15, 32), (3, 12, 35), (3, 0, 47)]]

    >>> search([5, 15, 25, 35])
    the num of states is: 31
    [(0, 0, 0), (1, 5, 0), (1, 0, 5), (2, 20, 0), (2, 5, 15), (2, 15, 5), (2, 0, 20), (3, 45, 0), (3, 20, 25), (3, 30, 15), (3, 5, 40), (3, 40, 5), (3, 15, 30), (3, 25, 20), (3, 0, 45), (4, 80, 0), (4, 45, 35), (4, 55, 25), (4, 20, 60), (4, 65, 15), (4, 30, 50), (4, 40, 40), (4, 5, 75), (4, 75, 5), (4, 40, 40), (4, 50, 30), (4, 15, 65), (4, 60, 20), (4, 25, 55), (4, 35, 45), (4, 0, 80)]

    >>> search([10, 20, 30, 40])
    the num of states is: 31
    [(0, 0, 0), (1, 10, 0), (1, 0, 10), (2, 30, 0), (2, 10, 20), (2, 20, 10), (2, 0, 30), (3, 60, 0), (3, 30, 30), (3, 40, 20), (3, 10, 50), (3, 50, 10), (3, 20, 40), (3, 30, 30), (3, 0, 60), (4, 100, 0), (4, 60, 40), (4, 70, 30), (4, 30, 70), (4, 80, 20), (4, 40, 60), (4, 50, 50), (4, 10, 90), (4, 90, 10), (4, 50, 50), (4, 60, 40), (4, 20, 80), (4, 70, 30), (4, 30, 70), (4, 40, 60), (4, 0, 100)]
    """
    qu = []
    new_qu = []
    qu.append(State(0, 0, 0))  # insert the start state to the queue
    for i in range(0, len(values)):
        q_len = len(qu)
        for j in range(0, q_len):
            org_state = qu.pop(0)
            son_state1 = State(org_state.num_of_objects + 1, org_state.player1 + values[i],
                               org_state.player2)  # add the object to player1
            son_state2 = State(org_state.num_of_objects + 1, org_state.player1,
                               org_state.player2 + values[i])  # add the object to player1
            # insert the 2 new states to the queue
            qu.append(son_state1)
            qu.append(son_state2)
            new_qu.append(org_state.toString())  # insert the original state to the final queue
    q_len = len(qu)
    # insert the states from the last iteration and insert them to the queue
    for j in range(0, q_len):
        org_state = qu.pop(0)
        new_qu.append(org_state.toString())
    print("the num of states is: " + str(len(new_qu)))
    return new_qu


def search_with_pruning(values: list):
    """
    in this function we search the state space with the first pruning rule based on BFS.
    the function get a list of valuse for any object and return list of all the existing states after deleting
    duplicate states.
    In the second and last examples we can see that the number of state is diffrent compared to the same example in the
    previous function, this is caused by duplicate states being deleted.

    >>> [search_with_pruning([2, 5])]
    the num of states is: 7
    [[(0, 0, 0), (1, 2, 0), (1, 0, 2), (2, 7, 0), (2, 2, 5), (2, 5, 2), (2, 0, 7)]]

    >>> [search_with_pruning([0, 15])]
    the num of states is: 4
    [[(0, 0, 0), (1, 0, 0), (2, 15, 0), (2, 0, 15)]]

    >>> search_with_pruning([20, 15, 12])
    the num of states is: 15
    [(0, 0, 0), (1, 20, 0), (1, 0, 20), (2, 35, 0), (2, 20, 15), (2, 15, 20), (2, 0, 35), (3, 47, 0), (3, 35, 12), (3, 32, 15), (3, 20, 27), (3, 27, 20), (3, 15, 32), (3, 12, 35), (3, 0, 47)]

    >>> search_with_pruning([5, 15, 25, 35])
    the num of states is: 30
    [(0, 0, 0), (1, 5, 0), (1, 0, 5), (2, 20, 0), (2, 5, 15), (2, 15, 5), (2, 0, 20), (3, 45, 0), (3, 20, 25), (3, 30, 15), (3, 5, 40), (3, 40, 5), (3, 15, 30), (3, 25, 20), (3, 0, 45), (4, 80, 0), (4, 45, 35), (4, 55, 25), (4, 20, 60), (4, 65, 15), (4, 30, 50), (4, 40, 40), (4, 5, 75), (4, 75, 5), (4, 50, 30), (4, 15, 65), (4, 60, 20), (4, 25, 55), (4, 35, 45), (4, 0, 80)]

    >>> search_with_pruning([10, 20, 30, 40])
    the num of states is: 25
    [(0, 0, 0), (1, 10, 0), (1, 0, 10), (2, 30, 0), (2, 10, 20), (2, 20, 10), (2, 0, 30), (3, 60, 0), (3, 30, 30), (3, 40, 20), (3, 10, 50), (3, 50, 10), (3, 20, 40), (3, 0, 60), (4, 100, 0), (4, 60, 40), (4, 70, 30), (4, 30, 70), (4, 80, 20), (4, 40, 60), (4, 50, 50), (4, 10, 90), (4, 90, 10), (4, 20, 80), (4, 0, 100)]

    """
    qu = []
    new_qu = []
    qu.append(State(0, 0, 0))  # insert the start state to the queue
    for i in range(0, len(values)):
        q_len = len(qu)
        for j in range(0, q_len):
            flag = False
            org_state = qu.pop(0)
            son_state1 = State(org_state.num_of_objects + 1, org_state.player1 + values[i],
                               org_state.player2)  # add the object to player1
            son_state2 = State(org_state.num_of_objects + 1, org_state.player1,
                               org_state.player2 + values[i])  # add the object to player1
            # insert the 2 new states to the queue
            qu.append(son_state1)
            qu.append(son_state2)
            # if this state does not already exist, put it in the final queue
            for k in range(0, len(new_qu)):
                curr = new_qu.pop(0)
                if org_state.toString() == curr:
                    flag = True
                new_qu.append(curr)
            if not flag:
                new_qu.append(org_state.toString())
    q_len = len(qu)
    # insert the states from the last iteration and insert them to the queue
    for j in range(0, q_len):
        flag = False
        org_state = qu.pop(0)
        for k in range(0, len(new_qu)):
            curr = new_qu.pop(0)
            if org_state.toString() == curr:
                flag = True
            new_qu.append(curr)
        if not flag:
            new_qu.append(org_state.toString())
    print("the num of states is: " + str(len(new_qu)))
    return new_qu


if __name__ == "__main__":
    import doctest

    doctest.testmod()
