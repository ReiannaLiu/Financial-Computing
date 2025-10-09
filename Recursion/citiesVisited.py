from fc_utils import Tree

def citiesVisited(flights, destination):
    return citiesVisitedHelper(flights, destination)

def citiesVisitedHelper(flights, destination):
    if flights.getValue() == destination:
        return [destination]
    else:
        res = [flights.getValue()]
        for child in flights.getChildren():
            potentialSolns = citiesVisitedHelper(child, destination)
            if potentialSolns != None:
                return res + potentialSolns
        return None

def testCitiesVisited():
    pghFlights = Tree('PGH',
                      Tree('DET',
                      Tree('DEN'),
                      Tree('ORD')),
                      Tree('IAD',
                           Tree('PHX')),
                      Tree('LGA',
                           Tree('SAN'),
                           Tree('JFK'),
                           Tree('LAX')))
    assert(citiesVisited(pghFlights, 'JFK') == ['PGH', 'LGA', 'JFK'])
    assert(citiesVisited(pghFlights, 'IAD') == ['PGH', 'IAD'])
    assert(citiesVisited(pghFlights, 'PGH') == ['PGH'])

    mcoFlights = Tree('MCO',
                      Tree('MIA',
                            Tree('SEA',
                                 Tree('LGA'),
                                 Tree('IAD')),
                            Tree('ORD')),
                      Tree('SFA',
                           Tree('DFW')),
                      Tree('LAX',
                           Tree('PGH'),
                           Tree('JFK',
                                Tree('PHX')),
                           Tree('SAN')))
    assert(citiesVisited(mcoFlights, 'MIA') == ['MCO', 'MIA'])
    assert(citiesVisited(mcoFlights, 'DFW') == ['MCO', 'SFA', 'DFW'])
    assert(citiesVisited(mcoFlights, 'PHX') == ['MCO', 'LAX', 'JFK', 'PHX'])

def main():
    testCitiesVisited()

main()