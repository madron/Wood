class WoodWorkbench(Workbench):
    def __init__(self):
        self.__class__.Icon = FreeCAD.getResourceDir() + '../Mod/Wood/icons/WorkbenchIcon.svg'
        self.__class__.MenuText = 'Wood'
        self.__class__.ToolTip = 'Wood Workbench'

    def Initialize(self):
        import dovetail
        self.appendToolbar('Wood Tools', ['dovetail_command'])
        self.appendMenu("Wood Tools", ['dovetail_command'])
        Log('Loading WoodWorkbench... done\n')
        Log(dir(FreeCAD))

    def GetClassName(self):
        return "Gui::PythonWorkbench"


Gui.addWorkbench(WoodWorkbench())
