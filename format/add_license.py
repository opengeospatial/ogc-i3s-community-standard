import shutil

input_filepath = "./format/17-014r11.html"

license_fin = open("./format/license_clause.html","r")

license_lines = license_fin.readlines()

fin = open(input_filepath,"r")
fout = open(input_filepath.replace(".html","_temp.html"),"w")

lines_in = fin.readlines()

for line in lines_in:
    if "Use of this document is subject to the license agreement at" in line:
        for license_line in license_lines:
            fout.write(license_line)
    else:
        fout.write(line)

license_fin.close()
fout.close()
fin.close()

shutil.copyfile(input_filepath.replace(".html","_temp.html"), input_filepath)