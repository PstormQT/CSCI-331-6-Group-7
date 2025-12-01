import model

class MonteCarloNode:
    def __init__(self, state: model.Board2048, parent = None, action = None):
        self.state = state
        self.parent = parent
        self.parentAction = action
        self.children = dict()
        self.visitCount = 0
        self.totalWeight = 0.0
        self.isEnded = state.getGameOver()
