import turtle

def snowflake(sideLen, levels):
    if levels == 0:
        snowflakeSide(sideLen, levels)
        turtle.right(120)
        snowflakeSide(sideLen, levels)
        turtle.right(120)
        snowflakeSide(sideLen, levels)
        turtle.right(120)
    else:
        snowflakeSide(sideLen, levels)
        turtle.right(120)
        snowflakeSide(sideLen, levels)
        turtle.right(120)
        snowflakeSide(sideLen, levels)
        turtle.right(120)

def snowflakeSide(sideLen, levels):
    if levels == 0:
        turtle.forward(sideLen/(3**levels))
    else:
        snowflakeSide(sideLen/3, levels-1)
        turtle.left(60)
        snowflakeSide(sideLen/3, levels-1)
        turtle.right(120)
        snowflakeSide(sideLen/3, levels-1)
        turtle.left(60)
        snowflakeSide(sideLen/3, levels-1)
        
        
        
