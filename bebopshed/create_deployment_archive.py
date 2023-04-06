# import argparse
import os
import tarfile


def main():
    target_path = "/home/manu/projects/bebopshed/deploy/deploy.tar"
    source_folders = ["api", "bebopshed", "lily_proc", "frontend"]
    with tarfile.open(target_path, "w:gz") as tarhandle:
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
