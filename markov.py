import numpy as np
import csv

class MarkovChain(object):
    def __init__(self, tmatrix, states):
        """
        Initialize the MarkovChain instance.
        Parameters
        ----------
        transition_matrix: 2-D array
            A 2-D array representing the probabilities of change of 
            state in the Markov Chain.
        states: 1-D array 
            An array representing the states of the Markov Chain. It
            needs to be in the same order as transition_matrix.
        """
        self._transition_matrix = np.atleast_2d(tmatrix)
        self._states = states
        self._index_dict = {self._states[index]: index for index in range(len(self._states))}
        self._state_dict = {index: self._states[index] for index in range(len(self._states))}

    def next_state(self, current_state):
        """
        Returns the state of the random variable at the next time instance.
        Parameters
        ----------
        current_state: str
            The current state of the system.
        """
        return np.random.choice(
        self._states, 
        p=self._transition_matrix[self._index_dict[current_state], :]
        )

    def generate_states(self, current_state, no=10):
        """
        Generates the next states of the system.

        Parameters
        ----------
        current_state: str
            The state of the current random variable.

        no: int
            The number of future states to generate.
        """
        future_states = []
        for i in range(no):
            next_state = self.next_state(current_state)
            future_states.append(next_state)
            current_state = next_state
        return future_states

class MarkovFile(object):
    def __init__(self, filename):
        self._file = open(filename, "r")
        self._reader = csv.reader(self.file)

    def parse(self):
        rnum = 0
        tmpmatrix = []
        for row in self._reader:
            if rnum == 0:
                self._states = row
            else:
                tmpmatrix.append(list(map(float, row)))
            rnum+=1
        self._MC = MarkovChain(tmpmatrix, self.states)

    def gstates(self, current_state, num=10):
        self.parse()
        return self._MC.generate_states(current_state, num)

pList = [[0, .1, .9],
        [.3, .4, .3],
        [.7, .2, .1]]

#cTest = MarkovChain(pList, ["a", "b", "c"])
#print(cTest.generate_states("a", 10))
fTest = MarkovFile("test.csv")
print(fTest.gstates("a", 10))