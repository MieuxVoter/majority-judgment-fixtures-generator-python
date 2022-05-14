#pip install PyYaml
import yaml
import random

# nb test in file
nb_tests = 10
tests = ['tests:']

# here we use only 5 choice max
max_vote_value = 5

# boucle du nombre de tests
for i in range (nb_tests):
    
    # one test list
    test = []
    
    # nb choice
    nb_vote_value = random.randrange(0, max_vote_value)
    
    # nb ballots
    nb_ballots = random.randrange(1, 11)
    
    # nb candidates
    nb_candidates = random.randrange(1, 5)
    
    #--------------------- CONFIGURATION attributes (hardcoded in this version)
    
    test.append( '# CONFIGURATION' )
    title = 'title: "Simple usage with {} ballots and {} candidates"'.format(nb_ballots, nb_candidates)
    test.append( title)
    algorithm = 'mj'
    test.append( '# algorithm: {}'.format(algorithm) )
    favorContestation = 'true'
    test.append( '# favorContestation: {}'.format(favorContestation) )
    normalizer = 'static (0)'
    test.append( '# normalizer: {}'.format(normalizer) )
    normalizer = 'median'
    test.append( '# normalizer: {}'.format(normalizer) )
    normalizer = 'stretch'
    test.append( '# normalizer: {}'.format(normalizer) )
    
    #--------------------- INPUT  
    
    test.append( '# INPUT' )
    test.append( 'Provide either `ballots` or `tallies` as input.' )
    test.append( 'If you provide both, `tallies` may be considered as an assertion (output)' )
    
    # generating ballots
    test.append( 'ballots:' )
    # this generate too many 0 values :s
    ballots = [[random.randint(0, nb_vote_value) for p in range(nb_candidates)] for j in range (nb_ballots)]
    ballots.append([random.randint(0, nb_vote_value) for p in range(nb_candidates)])
    test.append( ballots ) 
    #print( nb_ballots,  ballots )
    
    # generating tallies
    test.append( 'tallies:' )
    tallies = [sum(i) for i in zip(*ballots)]
    test.append(tallies)
    
    
    #--------------------- OUTPUT (empty while generating test) - TBD
    
    test.append( '# OUTPUT' )
    test.append( 'ranks:' )
    
    test.append( '# Optional, perhaps under analysis or analyses (TBD, perhaps support both?)' )
    test.append( 'majorityGrades:' )
    test.append( 'secondMajorityGrades:' )
    test.append( 'contestationGroupSizes:' )
    test.append( 'analysis1:' )
    test.append( 'analysis2:' )
    test.append( 'analysis3:' )
    
    #adding test to full list
    tests.append(test)
    
print (yaml.dump(tests, explicit_start=True) )

with open('MJ_stress_test.yml', 'w') as outfile:
    yaml.dump(tests, outfile, explicit_start=True)
