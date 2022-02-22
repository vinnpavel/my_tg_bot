import ephem

# Forming lists of Planets and Moons
planets_list, moons_list = [], []
# Extracting list of tuples of planets from library
for body in ephem._libastro.builtin_planets():
    if body[1] == 'Planet':
        planets_list.append(body[2])
    else:
        moons_list.append(body[2])
# Converting lists to tuples
planets_tuple = tuple(planets_list)
moons_tuple = tuple(moons_list)
del planets_list, moons_list

# Function of constellation calculation
def check_constellation(body):
    if body in planets_tuple:
        # Extracting attribute of planet from ephem
        planet = getattr(ephem, body)
        # Setting up current date
        planet = planet(ephem.now())
        # Getting current constellation
        constell = ephem.constellation(planet)
        return f'{body} is a Planet and located in {constell[1]} constellation'
    elif body in moons_tuple:
        # Perform same manipulations for moon
        moon = getattr(ephem, body)
        #moon = moon(ephem.now())  # Moon object is not callable
        # But for moons it is not so easy
        # Have to get the moon's coordinates
        # "You can either pass a Body whose position is computed, or a tuple (ra, dec) of coordinates"
        # Setting up an observer by default (zero lon and lat)
        obs = ephem.Observer()
        # Transmitt our omserver to the moon to be able to get coordinates
        o = moon(obs)
        # Getting coordinates as a tuple
        moon_coordinates = (o.ra, o.dec)
        # And finally calculating constellation
        constell = ephem.constellation(moon_coordinates)
        return f'{body} is a Moon and located in {constell[1]} constellation'
    else:
        return f"Sorry, can't identify {body} as a planet or moon"
