# Abdullah Hasani
# ahh190004
# NLP HW 2

# assumes sysarg is /anat19.txt
import sys

def readfile(filepath):

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('No sysarg provided!')
    else:
        filepath = sys.argv[1]
        print("The file path is " + filepath)
        contents = readfile(filepath)

