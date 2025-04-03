from hash import ComputeHash
from pathlib import Path
import shutil
import datetime
import hashlib

class Commit:

    def commit(self, message = ""):

        with open(".gitto/index", "r") as index:
            content = index.read()
            if len(content) > 0:

                files = list(Path(".gitto/commits").glob("*"))
                if files:
                    last_commit = max(files, key=lambda f: f.stat().st_mtime)
                    last_commit = last_commit.name
                else:
                    last_commit = None

                hash_hex = ComputeHash.compute_file_hash(".gitto/index")
                commit_metadata =   f"Commit Hash: hash_hex_commit\n"\
                                    f"Data: {datetime.datetime.now()}\n"\
                                    f"Mensagem: {message}\n"\
                                    f"Tree: {hash_hex}\n"\
                                    f"Commit Anterior: {last_commit}\n"
                
                hash_obj = hashlib.sha256(commit_metadata.encode())
                hash_hex_commit= hash_obj.hexdigest()

                trees = list(Path(".gitto/trees").glob("*"))
                try:
                    if trees:
                        last_tree = max(trees, key=lambda f: f.stat().st_mtime)
                        last_tree = last_tree.name
                    else:
                        last_tree = None
                except:
                    last_tree = None
                
                if last_tree != hash_hex:

                    shutil.copy2(".gitto/index", f".gitto/trees/{hash_hex}")

                    with open(f".gitto/commits/{hash_hex_commit}", "w") as commit:
                        commit.write(commit_metadata)
                    with open(f".gitto/commits/{hash_hex_commit}", "r") as commit:
                        commit_hash = commit.read().replace("hash_hex_commit", hash_hex_commit)
                    with open(f".gitto/commits/{hash_hex_commit}", "w") as commit:
                        commit.write(commit_hash)
                    
                    with open(".gitto/index", "w") as index:
                        index.write("")
                
                else:
                    print(f"\n-- Commit {hash_hex_commit} was the last commit!\n")

                    with open(".gitto/index", "w") as index:
                        index.write("")