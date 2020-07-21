class OldCoffeeMachine():
    def selectA(self, *args, **kwargs):
        print('Running first selection: Old Machine')

    def selectB(self, *args, **kwargs):
        print('Running second selection: Old Machine')


class CoffeeMachineInterface():
    def chooseFirstSelection(self, *args, **kwargs):
        raise NotImplementedError()

    def chooseSecondSelection(self, *args, **kwargs):
        raise NotImplementedError()


class CoffeeTouchscreenAdapter(CoffeeMachineInterface):
    def __init__(self, old_machine):
        self.__old_machine = old_machine

    def chooseFirstSelection(self, *args, **kwargs):
        self.__old_machine.selectA()

    def chooseSecondSelection(self, *args, **kwargs):
        self.__old_machine.selectB()


old_machine = OldCoffeeMachine()
adapter = CoffeeTouchscreenAdapter(old_machine)

adapter.chooseFirstSelection()
adapter.chooseSecondSelection()
