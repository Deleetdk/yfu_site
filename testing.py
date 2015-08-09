def remove_ticks(x):
    #pop list
    remove = ["tick1", "tick2", "tick3", "tick4", "tick5", "tick6", "tick7", "tick8", "tick9", "tick10"]
    
    #pop
    for i in remove:
        d.pop(i, None)

    #return
    return(d)

d = {"tick1": True, "tick10": True, "name": "Test Name"}

print(remove_ticks(d))