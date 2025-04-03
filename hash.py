import hashlib

class ComputeHash:
     
    def compute_file_hash(files):
            hash_obj = hashlib.sha256()
            with open(files, 'rb') as f:
                while chunk := f.read(4096):
                    hash_obj.update(chunk)
            return hash_obj.hexdigest()