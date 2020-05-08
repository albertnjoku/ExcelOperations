from export_files import export_files
from process_files import process_files
from import_config import import_config

opt = '10'
while int(opt) not in [0, 1, 2, 3, 4]:
    print("[1] Import Configurations")
    print("[2] Process Files")
    print("[3] Export File")
    print("[0] Exit")
    opt = input("Choose 1 to 4: ")

if opt == '1':
    im = import_config()
    im.import_config()

elif opt == '2':
    pr = process_files()
    pr.process_files()

elif opt == '3':
    ex = export_files()
    ex.export_file()

elif opt == '0':
    print("Goodbye!")
    exit(0)