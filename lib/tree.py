class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        def depth_first_traversal(node):
            if node is None:
                return None
            if node['id'] == id:
                return node
            for child in node['children']:
                result = depth_first_traversal(child)
                if result:
                    return result
            return None

        return depth_first_traversal(self.root)
