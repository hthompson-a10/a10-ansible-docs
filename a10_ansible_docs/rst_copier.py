import glob
import os
import shutil
import sys


def main():
    args = sys.argv
    module_path = args[1]
    version_path = args[2]

    mod_filenames = glob.glob(module_path + '/*.rst')
    mod_filenames = [x.split('/')[-1] for x in mod_filenames]
    ver_dirnames = [x.strip('./').split('/')[-1] for x in glob.glob(version_path + '/*/')]

    for mod_filename in mod_filenames:
        longest_common_dirname = ""
        for ver_dirname in ver_dirnames:
            if len(ver_dirname) > len(longest_common_dirname):
                if ver_dirname.replace('-', '_') in mod_filename[4:-4]: # Account for 'a10_' and '.rst' chars
                    longest_common_dirname = ver_dirname
        if len(longest_common_dirname) > 0:
            old_path = os.path.join(module_path, mod_filename)
            new_path = os.path.join(version_path, longest_common_dirname)
            new_path = os.path.join(new_path, mod_filename)
            shutil.move(old_path, new_path)
        else:
            #raise Exception()
            print("No intermediates found")

if __name__ == "__main__":
    main()
