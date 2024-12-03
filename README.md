AQ
==
AQ (arsehole quotient) is an algorithm for moderating political content on a website like twitter. The idea is that it categorises content as more or less moderate based on interactions of users with posts.

___

Iteration 1
-----------
There are users and posts. In the simplest form, a new post has a weighting indicating it's whether it's moderate (closer to 0) or more extreme (closer to 1), with the weight defined on a sigmoid function. A user's interaction with a post can be upvoting (+1) or ignoring (0). The user also has a weighting indicating it's political position in the same way a the post.

After a user-post interaction, the user's weighting is updated according to the following equation:
$
W_user = SIG*((W_post - W_user)*upvote_or_ignore + W_user)
$
