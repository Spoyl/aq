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
        self.weight = modified_sigmoid((post_weight-self.weight)*upvote_or_ignore)
        print("Updated user weight: " + str(self.weight))
    
    def post_interact(self, post_id, upvote_or_ignore, post_weight):
        self.history[post_id]=upvote_or_ignore
        if self.weight:
            update_weight(upvote_or_ignore, post_weight)
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

    def initialise(self, wieght):
        self.weight = weight

    def __str__(self):
        return f"{self.id},{self.weight}"
    
    def update_weight(post_id, vote_or_ignore):
        return 


def sigmoid(x):
    from numpy import exp
    return 1/(1 + exp(-x))

x = user(3)
print(str(x))
x.initialise()
print(str(x))