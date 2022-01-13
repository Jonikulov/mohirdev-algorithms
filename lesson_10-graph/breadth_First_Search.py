from my_queue import Queue

def breadth_First_Search(start_node, target='elon musk'):
    search_queue = Queue()
    search_queue.append(graph[start_node])
    searched = set()

    while not search_queue.isEmpty():
        search_item = search_queue.popleft()
        if search_item not in searched:
            searched.add(search_item)
            if search_item == target:
                print(f"{search_item} found!")
                return True
            else:
                search_queue.append(graph[search_item])
    return False


graph = {'siz': ['ali', 'vali', 'tohir'],
			'ali': ['aziza', 'olim'],
			'vali': ['botir', 'ziyoda'],
			'tohir': ['elon musk', 'mohir'],
			'olim': [],
			'aziza': [],
			'botir': [],
			'ziyoda': ['aziza'],
			'elon musk': [],
			'mohir': []
			}

breadth_First_Search('siz', 'elon musk')
# print(breadth_First_Search('siz', 'elon musk'))