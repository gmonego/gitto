import os
import shutil

class Repository:
    def initialize_repository():
        subdirs = [
            "objects",
            "refs/heads",
            "logs/refs/heads",
            "commits",
            "trees"
        ]
        files = [
            "HEAD",
            "index",
            "config.ini"
        ]

        if ".gitto" in os.listdir(os.getcwd()):
            repo_exists = input("\n-> Repository already exists. Overwrite? [y/n] ").upper()
            
            if repo_exists == "Y":
                confirm = input("-> Attention! All data will be replaced. Continue? [y/n] ").upper()
                
                if confirm == "Y":
                    shutil.rmtree(".gitto")
                    
                    for dirs in subdirs:
                        os.makedirs(f".gitto/{dirs}", exist_ok=True)
                    os.system("attrib +h .gitto")
                    
                    for file in files:
                        with open(f".gitto/{file}", "w") as f:
                            f.write("")
                    
                    with open(".gitto/refs/heads/main", "w") as f:
                        f.write("")
                    
                    with open(".gitto/HEAD", "w") as f:
                        f.write("ref: refs/heads/main")
                    
                    with open(".gitto/logs/HEAD", "w") as f:
                        f.write("")
                    
                    print(f"-> Versioning system successfully overwritten in => {os.getcwd()}\n")
                elif confirm == "N":
                    print("\n")
                else:
                    print("-> Invalid value.\n")
            elif repo_exists == "N":
                print("\n")
            else:
                print("-> Invalid value.\n")
        else:
            for dirs in subdirs:
                os.makedirs(f".gitto/{dirs}", exist_ok=True)
            os.system("attrib +h .gitto")
            
            for file in files:
                with open(f".gitto/{file}", "w") as f:
                    f.write("")
            
            with open(".gitto/refs/heads/main", "w") as f:
                f.write("")
            
            with open(".gitto/HEAD", "w") as f:
                f.write("ref: refs/heads/main")
            
            with open(".gitto/logs/HEAD", "w") as f:
                f.write("")
            
            print(f"\n-> Versioning system successfully created in => {os.getcwd()}\n")