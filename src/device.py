from helpers import get_guid

class Device:
    def __init__(self, guid=None, tasks=[]):
        self.guid = guid
        self.tasks = tasks if tasks is not None else []
        if not guid:
            self.guid = get_guid()

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        try:
            self.tasks.remove(task)
        except ValueError:
            print("No such task")