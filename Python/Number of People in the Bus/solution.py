def number(bus_stops):
    on_the_bus = 0
    for stop in bus_stops:
        cycle = stop[0] - stop[1]
        on_the_bus += cycle
        
    return on_the_bus
