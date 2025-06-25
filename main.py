import sys
import os
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
        timeout = self.ui.b_optionsTimeout.currentText()
        memory  = self.ui.b_optionsMaxMemory.currentText()

        # call analysis logic...
        print("🔎 Starting analysis on", self.selected_file)
        print(f" • Architecture: {arch}")
        print(f" • Timeout (mins): {timeout}")
        print(f" • Max Memory: {memory}")

        # TODO: replace prints with actual analysis functions

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = ConfigureDialog()
    dlg.show()
    sys.exit(app.exec())
