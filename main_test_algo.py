import majority_judgment
import matplotlib.pyplot as plt

# data: Dict[str, List[Union[int, float]]] 
#data = { 'candidate 1' : [1, 3, 5], 'candidate 2' : [4, 3, 2], 'Candidate 3': [4, 3, 2] }
data = { 'candidate 1' : [1, 3, 5], 'candidate 2' : [4, 3, 2], 'Candidate 3': [4, 3, 2], 'Candidate 4': [0, 3, 2] }
data = {'Candidate 1': [0, 0, 2], 'Candidate 2': [5, 0, 1], 'Candidate 3': [1, 1, 1], 'Candidate 4': [4, 4, 1]}
data = {'Pizza': [3, 2, 2, 3], 'Chips': [2, 4, 2, 2], 'Pasta': [3, 2, 3, 2], 'Bread': [1, 3, 4, 2]}

print('*****************************')
print(data)
ranking, median_grades = majority_judgment.majority_judgment( data )
print('ranking', ranking)
print('median_grades', median_grades)

