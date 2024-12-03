class user:
    """
    Object representing a simple agent.
    """
    def __init__(self, id):
        self.id = id
        self.weight = None
        self.history = {}

    def initialise(self, weight):
        self.weight = weight

    def __str__(self):
        return f"{self.id},{self.weight}"
    
    def update_weight(self, upvote_or_ignore, post_weight):
        self.weight = sigmoid((post_weight-self.weight)*upvote_or_ignore+self.weight)
    
    def post_interact(self, post_id, upvote_or_ignore, post_weight):
        self.history[post_id]=upvote_or_ignore
        if self.weight != None:
            self.update_weight(upvote_or_ignore, post_weight)
        else:
            print("User not yet initialised\n")
        return


class post:
    """
    Object representing a post.
    """
    def __init__(self, id):
        self.id = id
        self.weight = None

    def initialise(self, weight):
        self.weight = weight
    
    def get():
        return self.weight

    def __str__(self):
        return f"{self.id},{self.weight}"
    
    def update_weight(post_id, vote_or_ignore):
        return 


def sigmoid(x):
    from numpy import exp
    return 1/(1 + exp(-x))

x = user(3)
x.initialise(0)
print("initial weight: " + str(x))
x.post_interact(3, 0, 0.5)
print("updated weight: " + str(x))
print(x.history)