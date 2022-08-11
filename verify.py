node1 = {'public_key': 'op', 'private_key': 'opr', 'name': 'sita'}
node2 = {'public_key': 'ap', 'private_key': 'apr', 'name': 'raju'}
node3 = {'public_key': 'bp', 'private_key': 'bpr', 'name': 'ravi'}
node4 = {'public_key': 'cp', 'private_key': 'cpr', 'name': 'giri'}
_Nodes = [node1,node2, node3,node4]

class ver:
    def __init__(self, key):
        self.key = key

    #this method returns if private key is present or not
    def veriprivate(key):
        for i in range(0, len(_Nodes)):
            if key == _Nodes[i].get("private_key"):
                return True
        return False

    # this method returns the entire details given private key
    def getprivate(key):
        for i in range(0, len(_Nodes)):
            if key == _Nodes[i].get("private_key"):
                return _Nodes[i]

    #this method returns the name for user based on private key
    def getname(key):
        for i in range(0, len(_Nodes)):
            if key == _Nodes[i].get("private_key"):
                return _Nodes[i].get("name")
        return "NOT FOUND"

