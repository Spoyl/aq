class user:
    """
    Object representing a simple agent.
    """
    def __init__(self, id):
        self.id = id
        self.weight = 0.5

    def __str__(self):
        return f"{self.id},{self.weight}"
    
    def update_weight(post_id, vote_or_ignore):
        return 
    
    def post_interact():
        return


class post:
    """
    Object representing a post.
    """
    def __init__(self, id):
        self.id = id
        self.weight = 0.5
    
    def __str__(self):
        return f"{self.id},{self.weight}"
    
    def update_weight(post_id, vote_or_ignore):
        return 
