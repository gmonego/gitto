import os
import shutil
from hash import ComputeHash


class Index:
    def add(self, filename):
        for files in filename:
            if files in os.listdir(os.getcwd()) or os.path.exists(files):
                
                hash_hex = ComputeHash.compute_file_hash(files)
                
                shutil.copy2(files, f".gitto/objects/{hash_hex}")
                
                with open(".gitto/index", "r") as index:
                    index_content = index.read()
                
                if os.path.relpath(files) in index_content and hash_hex not in index_content:
                    confirm = input(
                        f"\n-> You are adding an uncommitted version of a pending file to the Index,\n"
                        "-> if you continue, the file will be overwritten. Do you want to continue? [y/n]\n"
                        f"-> file: {files}"
                    ).upper()
                
                    if confirm == "Y":
                        try:
                            with open(".gitto/index", "r") as index, open(".gitto/index_temp", "w") as index_temp:
                                for objects in index:
                                    if files in objects:
                                        index_temp.write(f"{hash_hex} {os.path.relpath(files)}\n")
                                    else:
                                        index_temp.write(objects)
                            
                            os.replace(".gitto/index_temp", ".gitto/index") 
                        except:
                            if os.path.exists(".gitto/index_temp"):
                                os.remove(".gitto/index_temp")
                    elif confirm == "N":
                        print("\n")
                    else:
                        print("-> Invalid value.\n")

                elif os.path.relpath(files) not in index_content and hash_hex not in index_content:
                    with open(".gitto/index", "a") as index:
                        index.write(f"{hash_hex} {os.path.relpath(files)}\n")
                    print(f"\n-> Index update => File added: {os.path.relpath(files)}")

                else:
                    print(f"-> There were no changes to the file <{os.path.relpath(files)}> to overwrite.")

            else:
                print(f"\n-> No such file or directory: {files}")
        print("\n")