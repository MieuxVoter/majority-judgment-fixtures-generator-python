import random
import os
import itertools
from pathlib import Path
import typing as t
from dataclasses import dataclass
import ruamel.yaml
import tap
import tqdm
from majority_judgment import majority_judgment


yaml = ruamel.yaml.YAML(typ="safe")

Algorithm = t.Literal["majority_judgment"]
Ranking = t.Dict[int, int]
Ballot = t.List[int]


@dataclass
class BallotGenerator:
    """
    Generate a sequence of ballots
    """
    num_candidates: int
    num_grades: int

    def generate_ballot(self) -> Ballot:
        """
        Generate a ballot
        """
        return random.choices(range(self.num_grades), k=self.num_candidates)


def compute_majority_judgment_ranking(ballots: t.Sequence[Ballot]) -> Ranking:
    """
    Return the ranking obtained with majority judgment
    """
    ballots = [list(i) for i in zip(*ballots)]

    if ballots == []:
        raise ValueError("The ballot box is empty!")

    num_candidates = len(ballots[0])

    if any(len(b) != num_candidates for b in ballots):
        raise NotImplementedError("Some ballots have a variable number of candidates")

    candidates = list(range(num_candidates))
    votes_per_candidates = dict(zip(candidates, ballots))
    return majority_judgment(votes_per_candidates)


def export_yaml(ballots: t.List[Ballot], ranking: Ranking, filepath: t.Union[str, Path], **kwargs):
    """
    Store a ballot and its corresponding ranking in yaml file
    """
    data ={'algorithm': kwargs, 'ballots': ballots, 'ranking': ranking}

    # export yml dump in file
    with open(filepath, "w") as f:
        yaml.dump(data, f)


class Arguments(tap.Tap):
    output: Path
    max_ballots: int = 50
    max_ballots_step: int = 3
    max_candidates: int = 5
    max_grades: int = 10
    max_trials: int = 10
    algorithm: Algorithm = "majority_judgment"
    seed: int = 0


if __name__ == "__main__":
    args = Arguments()
    print(args.parse_args())

    random.seed(args.seed)

    # loop paramters
    ballots = range(1, args.max_ballots + 1, args.max_ballots_step)
    candidates = range(2, args.max_candidates + 1)
    grades = range(2, args.max_grades + 1)

    parameters = itertools.product(ballots, candidates, grades)

    for param in tqdm.tqdm(list(parameters)):
        num_ballots, num_candidates, num_grades = param
        generator = BallotGenerator(num_candidates, num_grades)

        output_dir = args.output / str(num_grades) / str(num_candidates) / str(num_ballots)
        output_dir.mkdir(parents=True, exist_ok=True)

        for i in range(args.max_trials):
            ballots = [generator.generate_ballot() for _ in range(num_ballots)]
            ranking = compute_majority_judgment_ranking(ballots)
            export_yaml(ballots, ranking, output_dir / f'{i}.yaml',name=args.algorithm)

