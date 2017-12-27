from FreeCAD import Gui


class DovetailCommand():
    def GetResources(self):
        return {
            # 'Pixmap': 'dovetail.svg',
            'MenuText': 'Dovetail',
            'ToolTip': 'Create dovetail joint',
        }

    def Activated(self):
        selected_parts = Gui.Selection.getSelection()
        for part in selected_parts:
            print(type(part))


Gui.addCommand('dovetail_command', DovetailCommand())
