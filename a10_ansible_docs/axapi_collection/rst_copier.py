import os
import shutils


def main(*args):
    module_path = args[0]
    version_path = args[1]

    mod_dirpath, mod_dirnames, mod_filenames = os.walk(module_path)
    ver_dirpath, ver_dirnames, ver_filenames = os.walk(version_path)

    for mod_filename in mod_filenames:
        longest_common_dirname = ""
        for ver_dirname in ver_dirnames:
            if len(ver_dirname) > longest_common_dirname:
                if ver_dirname in mod_filename[4:]:
                    longest_common_dirname = ver_dirname
        if len(longest_common_dirname) > 0:
            old_path = os.path.join(mod_dirpath, mod_filename)
            new_path = os.path.join(ver_dirpath, ver_dirname)
            new_path = os.path.join(new_path, mod_filename)
            shutil.move(old_path, new_path)
        else:
            raise Exception()

if __name__ == "__main__":
    main()