import time

class Task:
    def __init__ (self, title, description):
        self.id = str(int(time.time() * 1000))[-6:]
        self.title = title
        self.description = description
        self.completed = False
    
    def __repr__ (self):
        status = "Completed" if self.completed else "Pending"
        return f"Task(id={self.id}), title='{self.title}', description='{self.description}', completed='{self.completed}', status='{status}'"

    def getId(self):
        return self.id;

    def getTitle(self):
        return self.title;

    def getDescription(self):
        return self.description
    
    def getCompleted(self):
        return self.completed
