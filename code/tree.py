#https://stackoverflow.com/questions/8484943/construct-a-tree-from-list-os-file-paths-python-performance-dependent

def attach(branch, trunk):
    '''
    Insert a branch of directories on its trunk.
    '''
    parts = branch.split('/', 1)
    if len(parts) == 1:  # branch is a file
        trunk[FILE_MARKER].append(parts[0])
    else:
        node, others = parts
        if node not in trunk:
            trunk[node] = defaultdict(dict, ((FILE_MARKER, []),))
        attach(others, trunk[node])

def prettify(d, indent=0):
    '''
    Print the file tree structure with proper indentation.
    '''
    for key, value in d.iteritems():
        if key == FILE_MARKER:
            if value:
                print '  ' * indent + str(value)
        else:
            print '  ' * indent + str(key)
            if isinstance(value, dict):
                prettify(value, indent+1)
            else:
                print '  ' * (indent+1) + str(value)



main_dict = defaultdict(dict, ((FILE_MARKER, []),))
for line in input_.split('\n'):
    attach(line, main_dict)

prettify(main_dict)