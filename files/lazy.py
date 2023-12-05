import yaml, shutil

# Configable
working_directory = "E:/Projects/lazy-setup/"
program_list_yaml = working_directory + "/settings/Program_List.yaml"

# Dynamically Assigned
selected_role = "analyst"


# Loads the program_list.yaml file
with open(program_list_yaml, "r") as file:
    program_list = yaml.safe_load(file)

    # Defines the roles and objects to be used in the program_list.yaml file
    roles = ["common", selected_role]
    objects = ["files", "rpms", "software"]

    # Loops through the roles and objects to create a dictionary of the objects from the program_list.yaml file
    object_vars = {}
    for role in roles:
        for object in objects:
            selected_object = program_list["role"][role][object]
            if selected_object is not None: # If the object is not empty, add it to the dictionary
                object_vars[object + "_list"] = program_list["role"][role][object]
            else: # If the object is empty, add an empty list to the dictionary
                object_vars[object + "_list"] = []

# Transfers requested objects from the file repository to the local machine
if (object_vars["files_list"]) is not None:
    for object in (object_vars["files_list"]):
        print("Transferring " + object)
        # shutil.copyfile(src, dst)

# Installs requested rpms from the downloaded rpm repository to the local machine
if (object_vars["rpms_list"]) is not None:
    for object in (object_vars["rpms_list"]):
        print("Installing local RPM: " + object)

# Installs requested software from the downloaded software repository to the local machine
if (object_vars["software_list"]) is not None:
    for object in (object_vars["software_list"]):
        print("Installing: " + object)



