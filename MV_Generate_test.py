import random
from numpy import sort
import ruamel.yaml
from ruamel.yaml.comments import CommentedMap
import sys
import majority_judgment

# Number of spaces for an indent 
INDENTATION = 2 

# Used to reset comment objects
tsRESET_COMMENT_LIST = [None, [], None, None]


class MajorityJugment_Sample:

    def __init__(self, nb_ballot=random.randint(1, 11), nb_candidate=random.randint(1, 5), max_vote_value=5):

        # hypothesis parameters
        self.nb_ballot = nb_ballot
        self.nb_candidate = nb_candidate
        self.max_vote_value = max_vote_value

        # generating ballots
        self.ballots = [[random.randint(0, max_vote_value) for p in range(nb_candidate)] for j in range (nb_ballot)]

        # generating tallies
        self.tallies = [list(i) for i in zip(*self.ballots)]

        # other input parameters - TBD
        self.title = '"Simple usage with {} ballots and {} candidates"'.format(self.nb_ballot, self.nb_candidate)
        self.algorithm = 'mj'
        self.favorContestation = 'true'
        self.normalizer1 = 'static (0)'
        self.normalizer2 = 'median'
        self.normalizer3 = 'stretch'

        # output parameters (empty while generating test) - TBD
        self.MajoritGrades = ''
        self.secondMajorityGrades = ''
        self.contestationGroupSizes = ''
        self.analysis1 = ''
        self.analysis2 = ''

    def majority_judgment_result(self):

        # calling majority_judgment.py
        # data: Dict[str, List[Union[int, float]]
        # str correspond to the names of candidates, List of int is the number for each grades
        
        # generating data

        # initialization to 0
        vote_ag_candidates = dict(('Candidate ' + str(i+1), [0] * (self.max_vote_value + 1) ) for i in range(self.nb_candidate))

        # fill with different votes
        for i in range(self.nb_candidate):
            for j in self.tallies[i]:
                vote_ag_candidates['Candidate ' + str(i+1)][j] += 1

        # calling majority_judgment.py algorithm
        self.ranking, self.median_grades = majority_judgment.majority_judgment( vote_ag_candidates )

        return self.ranking, self.median_grades

    def export_to_yaml(self):
        dico_test = CommentedMap(
                {'tests':{
                'title': self.title,
                'ballots': self.ballots,
                'tallies': self.tallies,
                'ranks': self.ranking,
                'majorityGrades': self.median_grades
                }
            })
        yaml = ruamel.yaml.YAML(typ='rt')
        yaml.version = (1, 2)
        return yaml.dump(dico_test, sys.stdout)
        #return ruamel.yaml.round_trip_dump(dico_test, sys.stdout)

    
if __name__ == '__main__':

    MV = MajorityJugment_Sample(3, 4)
    print(MV.ballots)
    
    print('******************')
    print ('MV dict',  {'test':MV.__dict__})

    print('******************')
    ranking, median_grades = MV.majority_judgment_result()
    print('ranking', ranking)
    print('median_grades', median_grades)

    print('******************')
    dump = MV.export_to_yaml()
    print(dump)

    #print('******************')
    #data = {'tests':MV.__dict__}

    #yaml = ruamel.yaml.YAML(typ='unsafe')
    #print(yaml.dump(data, sys.stdout))


