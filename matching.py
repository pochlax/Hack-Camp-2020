from typing import Callable, Dict, List, TextIO
import climatetype


# Set up a matching system based on the user's chosen categories
# Filter categories:
#       Interest— Animal, Climate Change, Humanity
#       Past Experience (keywords: animals, environment, trash, gobal, 
#                                  climate, change, human)
#       Skills (keywords: 
#       Career
#       Task


"""
Climatematch
Climatematch dictionary: Dict[str, Dict[str, object]]
    - each key is a username (a str)
    - each value is a Dict[str, object] with items as follows:
        - key 'name', value represents a user's name (a str)
        - key 'location', value represents a user's location (a str)
        - key 'bio', value represents a user's bio (a str)
        - key 'skills', value represents a user's skills (a List[str])
        - key 'interest', value represents a user's interests
          (a List[str])
          
NGOMatch
NGOMatch dictionary: Dict[Dict[str, object]]
    - each key is a username (a str)
    - each value is a Dict[str, object] with items as follows:
       - key 'skills', value represents a skills specification dictionary
       - key 'interest', value represents a interests specification dictionary
       - key 'number', value represents a number specification dictionary
    
SkillDict
SkillDict dictionary: Dict[str, object]
    - key 'technical', value represents wanted technical skills 
      (a List[str])
    - key 'interpersonal', value represents wanted interpersonal skills 
      (a List[str])
    
InterestDict
InterestDict dictionary: Dict[str, List[str]]
    - key 'interest', value represents interests of company
      (a List[str])
      
NumDict
NumDict dictionary: Dict[str, int]
    - key 'number', value represents # of wanted participants (int)
    
SortDict
SortDict dictionary: Dict[str, str]
    - key 'skill', value represents a skills to be sorted-by 
    - key 'interest', value represents a interests to be sorted-by 
"""

"""
Process:
#List of skills
#List of interests

"""
def process_data(file: TextIO) -> 'Climatematch':
    """ Return Climatematch dictionary from the user's data or the 
    company's data
    
    """
    climate_dict = {}
    line = file.readline()
    
    while line != '':
        username = line.strip()
        climate_dict[username] = {}
        
        line = file.readline().strip()
        climate_dict[username]['name'] = line
        line = file.readline().strip()
        climate_dict[username]['location'] = line
            
        climate_dict[username]['bio'] = ''
        line = file.readline()
        while line != 'ENDBIO\n': 
            climate_dict[username]['bio'] += line
            line = file.readline()
            
        climate_dict[username]['skills'] = []
        line = file.readline().strip()
        while line != 'ENDSKILL':        
            climate_dict[username]['skills'].append(line)
            line = file.readline().strip()
            
        climate_dict[username]['interest'] = []
        line = file.readline().strip()        
        while line != 'END':        
            climate_dict[username]['interest'].append(line)
            line = file.readline().strip()
        line = file.readline()
    
    return climate_dict



def process_query(file: TextIO) -> 'NGOMatch':
    """ Read the file and return the query in the query dictionary format.
    
    """
    query_dict = {}
    query_dict['skills'] = {}
    query_dict['interest'] = []
    line = file.readline().strip()
    
    query_dict['skills']['technical'] = []
    query_dict['skills']['interpersonal'] = []
    
    line = file.readline().strip()
    line = file.readline().strip()
    while line != 'Interpersonal':
        query_dict['skills']['technical'].append(line)
        line = file.readline().strip()    
    
    line = file.readline().strip()
    while line != 'INTEREST':
        query_dict['skills']['interpersonal'].append(line)
        line = file.readline().strip()
        
    line = file.readline().strip()    
    while line != 'NUMBER':
        query_dict['interest'].append(line)
        line = file.readline().strip()
            
    line = file.readline().strip()
    while line != 'SORT':
        query_dict['number'] = line
        line = file.readline().strip()
        
    line = file.readline().strip()
    while line != '':
        if line[:5] == 'skill':
            query_dict['sort-by']['skill'] = line[5:].strip()
        if line [:8] == 'interest':
            query_dict['sort-by']['interest'] = line[8:].strip()
        line = file.readline().strip()
         
    return query_dict


def match_user(dictionary: 'Climatematch', 
                       match: 'NGOMatch') -> Dict[str, tuple(int,int)]:
    """Return a list of usernames that match the skills criteria
    (at least 1 technical and/or 1 interpersonal)
    
    >>> t_dict2 = {'bwinton': {'name': 'Winton', 'location': 'Toronto, ON', 
                       'bio': 'Geek (Thunderbird and iPhone Developer)\n', 
                       'skills': ['Python', 'React'], 
                       'interest': ['environment']}}
    >>> match = {'skills': {'technical': ['Python', 'Photoshop'], 
                 'interpersonal': ['communication']}, 
                 'interest': ['Environment'], 'number': 3, 'sort-by': 'skill'}
       lst = {'agjkk': <2, 1>, 
             'agjkk': <['Python'], ['Environment']>},
    """

    total = {}
    
    for user in dictionary:
        total[user] = {}
        skillsCount = 0
        interestCount = 0
        for sk in dictionary[user]['skills']:           
            if sk in match['skills']['technical']:
                skillsCount = skillsCount + 1
            elif sk in match['skills']['interpersonal']:
                skillsCount = skillsCount + 1
                
        for inte in dictionary[user]['interest']:          
            if inte in match['interest']:
                interestCount = interestCount + 1
                
        total[user][(skillsCount, interestCount)]
    return total


def sort_skill(username: List[str], sort_dict: 'NGOMatch') -> List[str]:
    
    sk = sort_dict['sort_by']
    
    for user in username:
        if sk in user['skills']:
            return -1
        else:
            return 1    
    

def sort_interest(username: List[str]) -> List[str]:
    
    for user in username:
        if user[1] > 
        

def user_sort(data: 'Climatematch', results: List[str], 
               comparison_func: Callable[['Climatematch', str, str], int]
               ) -> None:
    
    for i in range(1, len(results)):
        current = results[i]
        position = i
        while position > 0 and \
                comparison_func(twitter_data, results[position - 1], 
                                current) > 0:
            results[position] = results[position - 1]
            position = position - 1 
        results[position] = current  
        
        
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()
import tree

def sort_user() -> List[str]:
    
    
