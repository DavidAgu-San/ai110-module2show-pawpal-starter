from datetime import datetime, timedelta

class Task:
    def __init__(self, description, time, frequency="once"):
        self.description = description
        self.time = time
        self.frequency = frequency
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def next_occurrence(self):
        if self.frequency == "once":
            return None

        today = datetime.today()
        if self.frequency == "daily":
            next_date = today + timedelta(days=1)
        elif self.frequency == "weekly":
            next_date = today + timedelta(weeks=1)
        else:
            return None

        return Task(self.description, self.time, self.frequency)

    def __repr__(self):
        return f"Task({self.description}, {self.time}, {self.frequency}, completed={self.completed})"


class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

    def get_incomplete_tasks(self):
        return [t for t in self.tasks if not t.completed]


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def get_pet(self, name):
        for pet in self.pets:
            if pet.name.lower() == name.lower():
                return pet
        return None

    def get_all_tasks(self):
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.tasks)
        return tasks


class Scheduler:
    def sort_by_time(self, tasks):
        return sorted(tasks, key=lambda t: datetime.strptime(t.time, "%H:%M"))

    def filter_by_pet(self, owner, pet_name):
        pet = owner.get_pet(pet_name)
        return pet.get_tasks() if pet else []

    def filter_by_status(self, tasks, completed=False):
        return [t for t in tasks if t.completed == completed]

    def detect_conflicts(self, tasks):
        time_map = {}
        for t in tasks:
            time_map.setdefault(t.time, []).append(t)

        return {time: ts for time, ts in time_map.items() if len(ts) > 1}

    def handle_recurrence(self, pet):
        new_tasks = []
        for task in pet.tasks:
            if task.completed:
                next_task = task.next_occurrence()
                if next_task:
                    new_tasks.append(next_task)

        for t in new_tasks:
            pet.add_task(t)

    def build_daily_schedule(self, owner):
        tasks = owner.get_all_tasks()
        tasks = self.sort_by_time(tasks)
        conflicts = self.detect_conflicts(tasks)

        schedule = []
        for t in tasks:
            schedule.append({
                "description": t.description,
                "time": t.time,
                "pet": self._find_pet_for_task(owner, t),
                "completed": t.completed,
                "frequency": t.frequency
            })

        return schedule, conflicts

    def _find_pet_for_task(self, owner, task):
        for pet in owner.pets:
            if task in pet.tasks:
                return pet.name
        return "Unknown"
