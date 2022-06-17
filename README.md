# majority-judgment-fixtures-generator-python

## Majority Judgment Data testing
A program to generate *.yml files with input, configuration and output.
Input such as ballots, candidates
Configutaion as different entry parameters
Output as ranks, majoritygrades, constestationgroupsize


### Specification format (commentary will be avoided)

```
# Grades are usually sorted from "worst" to "best".
tests:
    -
        # CONFIGURATION
        title: "Simple usage with …"
        # algorithm: mj
        # favorContestation: true
        # normalizer: static (0)
        # normalizer: median
        # normalizer: stretch
        
        # INPUT
        # Provide either `ballots` or `tallies` as input.
        # If you provide both, `tallies` may be used as an assertion (output)
        ballots:
            # [Grade to A, Grade to B, Grade to C]
            - [0, 1, 1]  # Participant 1
            - [2, 0, 1]  # Participant 2
            - …
        tallies:
            - [1, 2, 1]  # Candidate A
            - [0, 5, 3]  # Candidate B
            - [5, 1, 2]  # Candidate C
        
        # OUTPUT
        ranks:
            - 1  # Candidate A
            - 2  # Candidate B
            - 0  # Candidate C
        # Optional, perhaps under analysis or analyses (TBD, perhaps support both?)
        majorityGrades:
            - 2  # Candidate A
            - 1  # Candidate B
            - 0  # Candidate C
        # secondMajorityGrades: […]
        # contestationGroupSizes: […]
        # etc.
        # 
        # analysis: 
        # analyses:
    
    - …
```
	
### Programs used to generate files
- **python majority judgment algorithm package : TBD
- **python class to generate yml dump : TBD

