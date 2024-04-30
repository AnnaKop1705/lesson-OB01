# Менеджер задач
# Задача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны
# быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих
# (не выполненных) задач.

class Task():
    def __init__(self):
        self.tasks = []

    def add_task(self, name, deadline):
        task = {'name': name, 'deadline': deadline, 'status': False}
        self.tasks.append(task)

    def end_task(self, name):
        found = False
        for task in self.tasks:
            if task['name'] == name:
                task['status'] = True
                found = True
                print(f'Задача {name} выполнена')
                break
        if not found:
            print(f'Задача {name} не найдена')


    def show_work_tasks(self):
        found = False
        print('Рабочие задачи: ')
        for task in self.tasks:
            if not task['status']:
                print(f'{task['name']} - выполнить до {task['deadline']}')
                found = True
        if not found:
            print('Сейчас нет рабочих задач')


tasks = Task()

tasks.add_task('Пробежать 5 км', '05.05.2024')
tasks.add_task('Связать шарф', '05.08.2024')
tasks.add_task('Позвонить маме', '01.05.2024')

tasks.show_work_tasks()

tasks.end_task('Позвонить')

tasks.show_work_tasks()

tasks.end_task('Позвонить маме')

tasks.show_work_tasks()