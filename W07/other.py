def other(game):
    other_file1 = "test.dat"
    other_file2 = "test.txt"
    other_file3 = "test.tmp"

    shutil.copyfile(other_file1, other_file3)
    if not game.file_exists(other_file1):
        print("no file... create")
        file = open(other_file1, "xt")
        file.close()
    file = open(other_file1, "rt")
    file_raw_data = file.read()
    if file_raw_data != "": file_data = ast.literal_eval(file_raw_data)
    else: file_data = file_raw_data
    file.close()
    print(other_file1)
    print(file_data)
    if file_data == "":  file_data = {}
    if "x" in file_data.keys(): print(f"x = {file_data['x']}")
    if "y" in file_data.keys(): print(f"y = {file_data['y']}")
    file_data["x"] = 1
    file_data["y"] = 2
    file = open(other_file1, "wt")
    file.write(str(file_data))
    file.close()
    os.remove(other_file3)

    now = datetime.now()

    print(f"created:  {other_file2} - {game.file_created_datetime(other_file2)} - {game.file_created_age(other_file2)} - {game.is_data_filename_create_expired(other_file2)}")
    print(f"now {now}")
    game.request_enter_to_continue()

