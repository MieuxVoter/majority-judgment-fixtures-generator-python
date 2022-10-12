import random
import majority_judgment
import os
import ruamel.yaml

class MajorityJugment_Sample:
    
    random.seed(10)
    
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

        # MJ, MJ Favre+, MJ Favre-
        self.algorithm = 'MJ'


        #Maybe later...

        #self.favorContestation = 'true'
        #self.normalizer1 = 'static (0)'
        #self.normalizer2 = 'median'
        #self.normalizer3 = 'stretch'
        #output parameters (empty while generating test) - TBD
        #self.MajoritGrades = ''
        #self.secondMajorityGrades = ''
        #self.contestationGroupSizes = ''
        #self.analysis1 = ''
        #self.analysis2 = ''

    def majority_judgment_result(self):

        # calling majority_judgment.py
        # data: Dict[str, List[Union[int, float]]
        # str correspond to the names of candidates, List of int is the number for each grades
        
        # generating data

        # initialization to 0
        vote_aggr_candidates = dict((str(i+1), [0] * (self.nb_ballot) ) for i in range(self.nb_candidate))

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
                vote_aggr_candidates[str(idx_candidate+1)][idx_ballot] = vote
        for candidate in vote_aggr_candidates:
            vote_aggr_candidates[candidate].sort()

        # calling majority_judgment.py algorithm
        self.ranking = majority_judgment.majority_judgment( vote_aggr_candidates )

        # maybe later...
        # self.median_grades = ''
        #return self.ranking, self.median_grades

        return self.ranking

    def export_to_yaml(self, filename = "test.yml"):

        yaml = ruamel.yaml.YAML(typ='safe')

        # get the current script path, subdir, filepath
        here = os.path.dirname(os.path.realpath(__file__))
        subdir = "Releases"
        filepath = os.path.join(here, subdir, filename)

        # export yml dump in file
        with open(os.path.expanduser(filepath), 'w') as f:
            yaml.dump(MV.__dict__, f)

        # terminal print
        # return yaml.dump(MV.__dict__, sys.stdout)

if __name__ == '__main__':

    ### generating files

    random.seed(1)

    # loop paramters
    max_iter_all = 10
    max_iter_ballots_iter = 50
    max_iter_ballots_iter_step = 3
    max_iter_candidate = 5
    max_vote_value = 10
    
    for nb_ballot in range(1, max_iter_ballots_iter, max_iter_ballots_iter_step):
        for nb_candidate in range(1, max_iter_candidate+1):
            for max_vote_value in range(1, max_vote_value+1):
                for iter in range(1, max_iter_all):

                    # generating random ballots
                    MV = MajorityJugment_Sample(nb_ballot, nb_candidate, max_vote_value)

                    # calculate ranking
                    MV.majority_judgment_result()

                    # export to yml files in subdirectory "export_to_yaml:Releases"
                    filename = 'test_bal' + str(nb_ballot) + "_cand" + str(nb_candidate) \
                        + "_voteval" + str(max_vote_value) + "_iter" + str(iter) + '.yml'
                    print( "generating " + filename)
                    print(MV.ballots)
                    print(MV.ranking)
                    MV.export_to_yaml( filename )
    