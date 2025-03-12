class Tree:
    def __init__(self, name):
        self.name = name
        self.children = []

class DirectoryTree:
    def __init__(self):
        self.root = Tree("Pictures")

    def add_directory(self, parent_name, new_name):
        parent = self.find(self.root, parent_name)
        if parent: 
            new_directory = Tree(new_name)
            parent.children.append(new_directory)
        else:
            print("Parent not found")

    def find(self, node, name):
        if node.name == name:
            return node
        for child in node.children:
            result = self.find(child, name)
            if result:
                return result
        return None 

    def delete_directory(self, name):
        parent = self.find_parent(self.root, name)
        if parent:
            parent.children = [child for child in parent.children if child.name != name]
            print("Directory successfully deleted")
        else:
            print("Directory not found")

    def find_parent(self, node, name):
        for child in node.children:
            if child.name == name:
                return node
            parent = self.find_parent(child, name)
            if parent:
                return parent
        return None
    
    def display(self, node=None, indent=0):
        if node is None:
            node = self.root
        print("  " * indent + node.name)
        for child in node.children:
            self.display(child, indent + 1)

# Main execution
if __name__ == "__main__":
    directory_tree = DirectoryTree()

    # Add directories
    directory_tree.add_directory("Pictures", "Saved Pictures")
    directory_tree.add_directory("Saved Pictures", "Web Images")
    directory_tree.add_directory("Web Images", "Chrome")
    directory_tree.add_directory("Web Images", "Opera")
    directory_tree.add_directory("Web Images", "Firefox")
    directory_tree.add_directory("Pictures", "Screenshots")
    directory_tree.add_directory("Pictures", "Camera Roll")
    directory_tree.add_directory("Camera Roll", "2025")
    directory_tree.add_directory("Camera Roll", "2024")
    directory_tree.add_directory("Camera Roll", "2023")

    # Display the directory structure
    print("\n\U0001F4C2 Directory Structure:")
    directory_tree.display()

    # Delete a directory
    directory_tree.delete_directory("Camera Roll")

    # Display the directory structure after deletion
    print("\n\U0001F4C2 Directory Structure After Deletion of Camera Roll:")
    directory_tree.display()
