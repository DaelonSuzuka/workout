from nicegui import ui


class ExerciseCard(ui.card):
    def __init__(self, parent: 'RoutineCard'):
        super().__init__()
        self.props('flat bordered')

        with self, ui.row(wrap=False).classes('w-full items-center'):
            ui.input('Exercise Name:')
            ui.input('Type:')
            ui.button(
                icon='close', color='red', on_click=lambda: parent.delete_exercise(self)
            )


class RoutineCard(ui.card):
    def __init__(self):
        super().__init__()
        self.props('flat bordered')
        self.exercises = []

        with self:
            with ui.row().classes('w-full justify-between items-center'):
                ui.input('Routine Name:')
                ui.button('Add Exercise', on_click=self.new_exercise)

            self.exercise_container = ui.column()
            self.exercise_container.classes('w-full items-center')

            ui.button('Submit Routine', on_click=self.on_submit)

    def new_exercise(self):
        with self.exercise_container:
            exercise = ExerciseCard(self)
            self.exercises.append(exercise)

    def delete_exercise(self, exercise: ExerciseCard):
        self.exercises.remove(exercise)
        exercise.delete()

    def on_submit(self):
        ui.notify(self.exercises)


class WorkoutApp(ui.column):
    def __init__(self):
        super().__init__()
        self.classes('w-full')
        self.routines = []

        with self:
            ui.markdown("""# Workout Record\n\nv6.9""")

            self.routine_container = ui.column()
            self.routine_container.classes('w-full')
            ui.button('add record', on_click=self.new_routine)

    def new_routine(self):
        with self.routine_container:
            routine = RoutineCard()
            self.routines.append(routine)


@ui.page('/')
def index():
    WorkoutApp()


ui.run(
    title='Workout Record',
    dark=True,
    port=9999,
)
