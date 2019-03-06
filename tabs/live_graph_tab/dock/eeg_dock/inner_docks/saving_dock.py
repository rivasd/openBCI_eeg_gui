from tabs.live_graph_tab.dock.inner_dock import InnerDock
from save.data_saver import DataSaver


class SavingDock:
    def __init__(self, eeg_dock):
        self.eeg_dock = eeg_dock
        self.create_saving_dock()

    def create_saving_dock(self):
        saving_d = InnerDock(
                self.eeg_dock.layout, 'Saving', b_pos=(0, 2), toggle_button=True,
                size=(1, 1))
        DataSaver(
                self.eeg_dock.gv.main_window, self.eeg_dock.gv,
                saving_d.layout, size=(1,1))
        self.eeg_dock.dock_area.addDock(saving_d.dock)

