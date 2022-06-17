import random
import ruamel.yaml
import sys

# Regular imports
from copy import deepcopy

# Yaml loaders and dumpers
from ruamel.yaml.main import \
    round_trip_load as yaml_load, \
    round_trip_dump as yaml_dump


# Yaml commentary
from ruamel.yaml.comments import \
    CommentedMap as OrderedDict, \
    CommentedSeq as OrderedList

# For manual creation of tokens
from ruamel.yaml.tokens import CommentToken
from ruamel.yaml.error import CommentMark

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
        self.tallies = [sum(i) for i in zip(*self.ballots)]

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



if __name__ == '__main__':

    MV = MajorityJugment_Sample(3, 4)
    print(MV.nb_ballot, MV.nb_candidate)
    print(MV.ballots)
    
    print('******************')
    print ('MV dict',  {'test':MV.__dict__})


    print('******************')
    data = {'tests':MV.__dict__}

    yaml = ruamel.yaml.YAML(typ='unsafe')
    print(yaml.dump(data, sys.stdout))

   # with open('MJ_stress_test.yml', 'w') as file:
   #     yaml.dump(data, file)
    print('******************')
    data2 = yaml_dump(dict(MV.__dict__), indent=INDENTATION, block_seq_indent=INDENTATION)
    print('data2', data2)

    print('******************')
    data3 = yaml_load(yaml_dump({'tests':dict(MV.__dict__)}, indent=INDENTATION))
    data3.get("tests").\
        yaml_set_comment_before_after_key(key="title", before="# CONFIGURATION")

    object_depth = 1 # tests
    data3.get("tests").\
        yaml_set_comment_before_after_key(
            key=1, # "Farmhouse gold" is the second item in the list
            before="Last Resorts",
            indent=object_depth*INDENTATION
        )
    print('data3', yaml_dump(data3, 
                    indent=INDENTATION, 
                    block_seq_indent=INDENTATION))

    print('******************')
    data4 = yaml.load(str({'tests':dict(MV.__dict__)}), ruamel.yaml.RoundTripLoader)
    data4['title'].yaml_set_start_comment('# CONFIGURATION', indent=INDENTATION)
    print('data4', data4)
    
