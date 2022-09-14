import random
from typing import List
import majority_judgment

import yaml

import sys
import ruamel.yaml
from ruamel.yaml.comments import CommentedMap


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
        vote_ag_candidates = dict((str(i+1), [0] * (self.nb_ballot) ) for i in range(self.nb_candidate))

        # fill with different votes order by values
        # ex:
        # data = {
        #     'Pizza': [0,0,0, 1,1, 2,2, 3,3,3], 
        #     'Chips': [0,0, 1,1,2,2,2,2,3,3],
        #     'Pasta': [0,0,1,1,1,2,2,3,3,3],
        #     'Bread': [0,0,1,1,1,1,2,2,2,3],
        # }

        for idx_ballot, ballot in enumerate(self.ballots):
            for idx_candidate, vote in enumerate(ballot):
                vote_ag_candidates[str(idx_candidate+1)][idx_ballot] = vote
        
        for candidate in vote_ag_candidates:
            vote_ag_candidates[candidate].sort()

        print("vote_ag_candidates", vote_ag_candidates)

        # calling majority_judgment.py algorithm
        self.ranking = majority_judgment.majority_judgment( vote_ag_candidates )
        # self.median_grades = majority_judgment.median_grade
        self.median_grades = ''
        
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
        yaml = ruamel.yaml.YAML(typ=['rt', 'string'])
        #yaml = ruamel.yaml.YAML(typ=['unsafe', 'string'])
        #yaml = ruamel.yaml.YAML(typ='rt')
        yaml = ruamel.yaml.YAML(typ='unsafe')
        #yaml = ruamel.yaml.YAML(typ='safe')
        yaml.version = (1, 2)
        #yaml.allow_unicode=True
        #yaml.explicit_start=True

        dico_test = {'tests':MV.__dict__}
        #return ruamel.yaml.dump(dico_test, sys.stdout, allow_unicode=True, explicit_start=True, version=(1, 2))

        return yaml.dump(dico_test, sys.stdout)
        #return ruamel.yaml.round_trip_dump(dico_test, sys.stdout)

def _reverse_2d_list(list_2d: List[List]) -> List[List]:
    lengths = [len(x) for x in list_2d]
    if not len(set(lengths)) == 1:
        raise ValueError('Please provide a square matrix')
    
    sub_length = lengths[0]
    length = len(list_2d)
    
    return [[list_2d[i][j] for i in range(length)] for j in range(sub_length)]

def yml_dump(yaml_content):

    testset = yaml.safe_load(yaml_content)

    for name, item in testset.items():
        print('Testing', name)
        
        if item['algorithm'] != 'mj':
            raise NotImplementedError()
        
        candidates = list(range(1, 1 + item['numCandidates']))
        
        ballots = _reverse_2d_list(item['ballots'])
        votes = dict(zip(candidates, ballots))
        ranking = majority_judgment(votes)
        for c, r in ranking.items():
            ranking[c] += 1
        
        true_ranking = dict(zip(candidates, item['ranking']))
        
        assert ranking == true_ranking, (ranking, true_ranking)


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


