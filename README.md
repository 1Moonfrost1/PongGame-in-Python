A PongGame in Python using Turtle.

As a sidenote the ball works based on heading and velocity which is problematic when it comes to clipping the paddle and the ball, as the ball can get stuck inside the paddle.
A fix to this would be either moving the ball using velocity (speed on x coord , speed on y coord), or by making it so that the collision is within a range where the turtle.forward()
can get out of when the collision occurs.
