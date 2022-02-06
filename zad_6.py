portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

D = [
        [0,8943,8019,3652,10545],
        [8943,0,2619,6317,2078],
        [8019,2619,0,5836,4939],
        [3652,6317,5836,0,7825],
        [10545,2078,4939,7825,0]
    ]

co2 = 0.020

smallest = 1000000
bestroute = [0, 0, 0, 0, 0]


def permutations(route, ports):

    if len(ports) > 1:
        for i in range(len(ports)):
            pom_route = []
            for j in range(len(portnames) - len(ports)):
                pom_route += [route[j]]
            pom_ports = []
            for j in range(len(ports)):
                if j != i:
                    pom_ports += [ports[j]]
                else:
                    route += [ports[j]]
                    pom_route += [ports[j]]
            permutations(pom_route, pom_ports)
    else:
        route += [ports[0]]
        print(' '.join([portnames[i] for i in route]))
        ukupno = 0
        for i in range(len(route) - 1):
            #print(D[route[i]][route[i + 1]])
            ukupno += D[route[i]][route[i + 1]] * co2
        print("ukupno za route", route, "je:", ukupno)
        global smallest, bestroute
        if ukupno < smallest:
            smallest = ukupno
            bestroute = route


def main():
    # this will start the recursion
    permutations([0], list(range(1, len(portnames))))

    # print the best route and its emissions
    print("\nBEST ROUTE:")
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)


main()