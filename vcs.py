import argparse
from repo_manager import Repository as repo
from staging import Index as idx
from config import Config as conf
from commit import Commit

index = idx()

def main(args):

    if args.command == "init":
        repo.initialize_repository() 
    elif args.command == "user-config":
        conf.configure_user()  
    elif args.command == "add":
        index.add(args.files)  
    elif args.command == "commit":
        ful_message = " ".join(args.message)
        Commit.commit(ful_message)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=""
    )

    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Available commands"
    )

    parser_init = subparsers.add_parser("init", help="Initialize the repository")
    
    parser_config = subparsers.add_parser(
        "user-config", help="Configure user settings for the repository"
    )
    
    parser_add = subparsers.add_parser(
        "add", help="Add files to the staging area"
    )
    parser_add.add_argument(
        "files", nargs="+", help="List of files to be added to the index"
    )

    parser_commit= subparsers.add_parser(
        "commit", help="Commit indexed data"
    )
    parser_commit.add_argument(
        "message", nargs="+", help="Commit message"
    )

    args = parser.parse_args()
    main(args)