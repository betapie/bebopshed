import argparse
import os
import tarfile


def main():
    parser = argparse.ArgumentParser(
        description="Copies all relevant files to a tar-file for deployment"
    )
    parser.add_argument(
        "-t", "--target_path", default=".", help="Path to the target directory"
    )
    parser.add_argument(
        "-f",
        "--filename",
        default="deploy.tar",
        help="Name of the created tar file",
    )
    args = parser.parse_args()
    target_path = os.path.abspath(args.target_path)
    target_file = os.path.join(target_path, args.filename)
    source_folders = ["api", "bebopshed", "lily_proc", "frontend"]
    with tarfile.open(target_file, "w:gz") as tarhandle:
        while source_folders:
            path = source_folders.pop()
            for elem in os.listdir(path):
                fullpath = os.path.join(path, elem)
                if os.path.isdir(fullpath) and not elem.startswith("__"):
                    source_folders.append(fullpath)
                elif elem.endswith(".py") or elem.endswith(".ily"):
                    tarhandle.add(fullpath)

        tarhandle.add("frontend/static")
        tarhandle.add("frontend/templates/frontend")


if __name__ == "__main__":
    main()
