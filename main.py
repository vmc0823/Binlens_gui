import sys
import os
import angr
from claripy import BVS
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog
from configureAnalysisWindow_ui import Ui_Configure

class ConfigureDialog(QDialog):
    def __init__(self):
        super().__init__()
        # instantiate and setup the UI
        self.ui = Ui_Configure()
        self.ui.setupUi(self)

        # connect signals, slots
        self.ui.b_chooseFile.clicked.connect(self.on_choose_file)
        self.ui.b_StartAnalysis.clicked.connect(self.on_start_analysis)

        # store selected path (optional)
        self.selected_file = None

    def on_choose_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Choose a file",
            "",
            "All Files (*)"
        )
        if not path:
            return
        self.selected_file = path
        name = os.path.basename(path)

        # update UI to show the chosen file
        self.ui.b_chooseFile.setText(name)
        self.ui.l_configAnalysis.setText(f"Configure Analysis on {name}")

    def on_start_analysis(self):
        if not self.selected_file:
            print("⚠️ No file selected!")
            return
        
        arch    = self.ui.b_optionsInstruc.currentText()
        timeout = int(self.ui.b_optionsTimeout.currentText())
        memory  = self.ui.b_optionsMaxMemory.currentText()
        
        # angr logic here
        proj = angr.Project(self.selected_file, auto_load_libs=False)

        sym_arg = BVS("sym_arg", 8 * 8)
        state = proj.factory.entry_state(args=[self.selected_file, sym_arg])

        simgr = proj.factory.simgr(state)
        simgr.explore( 
            find=lambda s: b"Correct!" in s.posix.dumps(1),
            avoid=lambda s: b"Wrong!" in s.posix.dumps(1),
        )

        #results
        if simgr.found:
            found = simgr.found[0]
            solution = found.solver.eval(sym_arg, cast_to=bytes).rstrip(b"\x00")
            print("Solution:", solution.decode())
        else:
            print("No valid input found.")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = ConfigureDialog()
    dlg.show()
    sys.exit(app.exec())
