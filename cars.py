showroom = set()

showroom = { "Bugatti", "Lamborghini", "Porsche", "Datsun" }

print(len(showroom))

showroom.add("Datsun")

print(showroom)

new_cars = { "Malibu", "Taurus" }

showroom.update(new_cars)

print(showroom)

showroom.discard("Datsun")

print(showroom)

junkyard = { "Bugatti", "Porsche", "Cadillac", "Mustang", "Civic" }

similar_cars = showroom.intersection(junkyard)

print(similar_cars)

new_showroom = showroom.union(junkyard)

print(new_showroom)

new_showroom.discard("Taurus")

print(new_showroom)
