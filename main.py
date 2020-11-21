from db_array import *
from ui_console import *
from ui_graph import *

db = ArrayDB()
ui = GraphUI(db)
#ui = ConsoleUI(db)
ui.start()
