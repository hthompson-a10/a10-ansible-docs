import glob
import os
import shutil
import sys


INTERMEDIATE_FILE = (
"{filename} \n"
"{title_bar} \n\n"
"Actions:\n\n\n"
".. toctree::\n"
"   :maxdepth: 1\n"
"   :glob:\n\n"
"   *")


def add_to_overview(new_dir_name, version_path):
    link = "{}/{}.rst".format(new_dir_name, new_dir_name) 
    link_line = "   {}\n".format(link)
    incl_line = "    .. include:: {link}\n".format(link=link)

    # TODO: Brute force method. Replace with file seeking later
    version_number = version_path.strip('./').split('/')[-1]
    overview_file = os.path.join(version_path, version_number + ".rst")

    file_break_pos = 0
    with open(overview_file, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for i, line in enumerate(f):
            if line.startswith('    .. include::'):
                file_break_pos = i - 1
                break
        if file_break_pos == 0:
            raise Exception()
        f.seek(0)
        lines.insert(file_break_pos, link_line)
        lines.insert(file_break_pos+2, incl_line)
        f.writelines(lines)


def build_inter_file(new_dir_name, new_dir_path):
    inter_filename = os.path.join(new_dir_path, new_dir_name + ".rst")
    with open(inter_filename, 'w') as f:
         title_bar = "=" * len(new_dir_name)
         f.write(INTERMEDIATE_FILE.format(filename=new_dir_name, title_bar=title_bar))


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
                inter_name = ver_dirname.replace('-', '_')
                if mod_filename.startswith(inter_name, 4, len(mod_filename)-4): # Account for 'a10_' and '.rst' chars
                    longest_common_dirname = ver_dirname
        if len(longest_common_dirname) > 0:
            old_path = os.path.join(module_path, mod_filename)
            new_path = os.path.join(version_path, longest_common_dirname)
            new_path = os.path.join(new_path, mod_filename)
            shutil.move(old_path, new_path)
        else:
            # No intermediates found. Likely it's own vertical
            new_dir = mod_filename[4:-4].replace('_', '-')
            dirpath = os.path.join(version_path, new_dir)
            os.mkdir(dirpath)
            ver_dirnames.append(new_dir)
            build_inter_file(new_dir, dirpath)
            add_to_overview(new_dir, version_path)

            old_path = os.path.join(module_path, mod_filename)
            new_path = os.path.join(dirpath, mod_filename)
            shutil.move(old_path, new_path)


if __name__ == "__main__":
    main()
