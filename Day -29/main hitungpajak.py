from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from hitungpajak import Ui_Dialog

class Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.calculate_tax)

    def calculate_tax(self):
        try:
            # Ambil nilai harga dari QLineEdit
            harga = float(self.lineEdit.text())
            
            # Ambil nilai pajak dari QComboBox
            persentase_pjk_str = self.comboBox.currentText()
            persentase_pjk = float(persentase_pjk_str.rstrip('%')) / 100
            
            # Hitung total harga beserta pajak
            total_harga = harga + (harga * persentase_pjk)
            
            # Tampilkan hasilnya di QLabel
            self.label_4.setText(f"Total Harga Beserta Pajak Adalah : Rp {total_harga:.2f}")
        except ValueError:
            # Tampilkan pesan kesalahan jika input tidak valid
            QMessageBox.warning(self, "Input Error", "Masukkan harga yang benar.")

if __name__ == '__main__':
    app = QApplication([])
    dialog = Dialog()
    dialog.show()
    app.exec_()
