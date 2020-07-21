class OldCoffeeMachine():
    def __init__(self):
        pass

    def selectA(self, *args, **kwargs):
        print('Running first selection: Old Machine')

    def selectB(self, *args, **kwargs):
        print('Running second selection: Old Machine')


class CoffeeMachineInterface():
    def __init__(self):
        pass

    def chooseFirstSelection(self, *args, **kwargs):
        raise NotImplementedError()

    def chooseSecondSelection(self, *args, **kwargs):
        raise NotImplementedError()


class CoffeeTouchscreenAdapter(CoffeeMachineInterface):
    def __init__(self):
        self.__old_machine = OldCoffeeMachine()

    def chooseFirstSelection(self, *args, **kwargs):
        self.__old_machine.selectA()

    def chooseSecondSelection(self, *args, **kwargs):
        self.__old_machine.selectB()


adapter = CoffeeTouchscreenAdapter()

adapter.chooseFirstSelection()
adapter.chooseSecondSelection()
