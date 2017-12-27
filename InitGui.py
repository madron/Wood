class WoodWorkbench(Workbench):
    def __init__(self):
        self.__class__.Icon = FreeCAD.getResourceDir() + '../Mod/Wood/icons/WorkbenchIcon.svg'
        self.__class__.MenuText = 'Wood'
        self.__class__.ToolTip = 'Wood Workbench'

    def Initialize(self):
        pass


Gui.addWorkbench(WoodWorkbench())
