from typing import List


class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = tasks
        self.task_dict = {}
        for task in tasks:
            userId, taskId, priority = task
            self.task_dict[taskId] = (userId, priority, taskId)
        self.sorted_tasks = sorted(tasks, key=lambda x: (-x[2], -x[1]))
        self.top_task = self.sorted_tasks[0] if self.sorted_tasks else []
        self.was_edited = False

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_dict[taskId] = (userId, priority, taskId)
        self.sorted_tasks.append([userId, taskId, priority])
        if (
            not self.top_task
            or priority > self.top_task[2]
            or (priority == self.top_task[2] and taskId > self.top_task[1])
        ):
            self.top_task = [userId, taskId, priority]
        # self.sorted_tasks.sort(key=lambda x: (-x[2], -x[1]))
        self.was_edited = True

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _, _ = self.task_dict[taskId]
        self.task_dict[taskId] = (userId, newPriority, taskId)
        for i, task in enumerate(self.sorted_tasks):
            if task[1] == taskId:
                self.sorted_tasks[i][2] = newPriority
                break
        if (
            not self.top_task
            or newPriority > self.top_task[2]
            or (newPriority == self.top_task[2] and taskId > self.top_task[1])
        ):
            self.top_task = [userId, taskId, newPriority]
        # self.sorted_tasks.sort(key=lambda x: (-x[2], -x[1]))
        self.was_edited = True

    def rmv(self, taskId: int) -> None:
        del self.task_dict[taskId]
        self.sorted_tasks = [task for task in self.sorted_tasks if task[1] != taskId]
        if self.top_task and self.top_task[1] == taskId:
            if self.was_edited:
                self.sorted_tasks.sort(key=lambda x: (-x[2], -x[1]))
                self.was_edited = False
            self.top_task = self.sorted_tasks[0] if self.sorted_tasks else []

    def execTop(self) -> int:
        if not self.top_task:
            return -1
        userId, taskId, _ = self.top_task
        self.sorted_tasks.remove(self.top_task)
        del self.task_dict[taskId]

        if self.was_edited:
            self.sorted_tasks.sort(key=lambda x: (-x[2], -x[1]))
            self.was_edited = False
        self.top_task = self.sorted_tasks[0] if self.sorted_tasks else []
        return userId


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()


class TaskManager2:
    def __init__(self, tasks: List[List[int]]):
        self.tasks = SortedSet()
        self.task_to_users = {}
        self.task_to_priority = {}
        for user_id, task_id, priority in tasks:
            self.add(user_id, task_id, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks.add((priority, taskId, userId))
        self.task_to_users[taskId] = userId
        self.task_to_priority[taskId] = priority

    def edit(self, taskId: int, newPriority: int) -> None:
        user = self.task_to_users[taskId]
        self.rmv(taskId)
        self.add(user, taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        user = self.task_to_users[taskId]
        priority = self.task_to_priority[taskId]
        self.tasks.remove((priority, taskId, user))
        del self.task_to_users[taskId]
        del self.task_to_priority[taskId]

    def execTop(self) -> int:
        if not self.tasks:
            return -1
        _, task_id, user_id = self.tasks[-1]
        self.rmv(task_id)
        return user_id
