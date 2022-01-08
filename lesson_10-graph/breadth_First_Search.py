from collections import deque

def breadth_First_Search(start_node, target='celebrity'):
    search_queue = deque()
    search_queue += graph[start_node]  
    searched = set()

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person == target:
                print(f'{target}ni topdik!')
                # print(searched)
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False


graph = {'siz': ['ali', 'vali', 'tohir'],
			'ali': ['aziza', 'olim'],
			'vali': ['botir', 'ziyoda'],
			'tohir': ['celebrity', 'mohir'],
			'olim': [],
			'aziza': [],
			'botir': [],
			'ziyoda': ['aziza'],
			'elon musk': [],
			'mohir': []
			}

print(breadth_First_Search('siz'))
print(breadth_First_Search('ali','vali'))