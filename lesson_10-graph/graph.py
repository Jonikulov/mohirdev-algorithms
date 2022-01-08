# GRAPHS

graph1 = {'siz':['ali', 'vali', 'tohir'],
        'ali':['aziza', 'olim'],
        'vali':['botir', 'ziyoda'],
        'tohir':['elon musk', 'mohir'],
        'olim':[],
        'aziza':[],
        'botir':[],
        'ziyoda':['aziza'],
        'elon musk':[],
        'mohir':[]
    }

graph2 = {'siz':
            {'ali':
                {'olim':[], 'aziza':[]},
            'vali':
                {'botir':[], 'ziyoda':{'aziza':[]}},
            'tohir':
                {'elon musk':[], 'mohir':[]}
            }
    }

print(graph1['siz'])
print(graph2['siz']['ali'])