import sys
from PyQt5.QtWidgets import QApplication
from db import connect_db, create_table_if_not_exists
from ui import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    conn = connect_db()
    create_table_if_not_exists(conn)

    main_win = MainWindow()
    main_win.show()

    sys.exit(app.exec_())
