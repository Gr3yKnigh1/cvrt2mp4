"""
Original:
https://gist.github.com/wahengchang/19a65f561fdb57846e0f7c512028cb0d
"""
import subprocess
import argparse
import shutil
import os


is_exe_exists = lambda name: shutil.which(name) is not None


if not is_exe_exists("ffmpeg"):
    raise Exception("This program require 'ffmpeg' executable in PATH variable")


parser = argparse.ArgumentParser()
parser.add_argument("target", help="target directory")
parser.add_argument("--output", help="output directory", default="./mp4")
args = parser.parse_args()


src = args.target
dst = args.output 


if not os.path.exists(dst):
    os.mkdir(dst)


# TODO(Gr3yKnigh1): Create progress bar and verbose argument
def main():
    for root, dirs, filenames in os.walk(src, topdown=False):
        for filename in filenames:
            print('[INFO] 1', filename)
            
            try:
                frmt = '' # format
                if ".flv" in filename.lower():
                    frmt=".flv"
                elif ".mp4" in filename.lower():
                    frmt=".mp4"
                elif ".avi" in filename.lower():
                    frmt=".avi"
                elif ".mov" in filename.lower():
                    frmt=".mov"
                else:
                    continue

                inputfile = os.path.join(root, filename)
                print('[INFO] 1', inputfile)
                outputfile = os.path.join(dst, filename.lower().replace(frmt, ".mp4"))
                subprocess.call(['ffmpeg', '-i', inputfile, outputfile])  
            except Exception as e:
                print("An exception occurred")
                print(e)


if __name__ == '__main__':
    main()
