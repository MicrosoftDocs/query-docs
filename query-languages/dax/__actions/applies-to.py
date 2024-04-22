from os import listdir
from os.path import isfile, join
import csv

DEBUG = False
VERBOSE = False

MDPath = "..//"
functionFileTail = "-function-dax.md"
appliesToPath = "..//includes//"
functionNameStartString = "# "
appliesToStartString = "[!INCLUDE[applies-to-"
appliesToStatusFile = "applies-to-status.csv"
appliesToStatusFileColumns = ("FunctionName","AppliesToStatus")
appliesToAllFlag = "ALL"
appliesToMCTFlag = "MCT"
appliesToVCFlag = "VC"
appliesToDiscourageFlag = "DISCOURAGE"
appliesToPathNoRelative = "includes/"

# Paths to applies to include files
appliesToAllFile = "applies-to-measures-columns-tables-visual-calculations" #status in CSV: ALL
appliesToAll = appliesToPath+appliesToAllFile+".md"
appliesToMeasuresColumnsTablesFile = "applies-to-measures-columns-tables" #status in CSV: MCT
appliesToMeasuresColumnsTables = appliesToPath+appliesToMeasuresColumnsTablesFile+".md"
appliesToVisualCalculationsFile = "applies-to-visual-calculations" #status in CSV: VC
appliesToVisualCalculations = appliesToPath+appliesToVisualCalculationsFile+".md"
appliesToDiscouragedForVisualCalculationsFile = "applies-to-measures-columns-tables-visual-calculations-discouraged" #DISCOURAGE
appliesToDiscouragedForVisualCalculations = appliesToPath+appliesToDiscouragedForVisualCalculationsFile+".md"

# load AppliesToStatusFile
appliesToFileContents = None
with open(appliesToStatusFile, 'r') as atsfile:
    appliesToFileContents = dict(csv.reader(atsfile))
    # capitalize everything just in case
    appliesToFileContents = {k.upper(): v.upper() for k, v
                             in appliesToFileContents.items()}
if DEBUG:
    print(appliesToFileContents["ABS"])

# iterate over the function files
thefunctions = [f[0:f.index(functionFileTail)] for f in listdir(MDPath) if isfile(join(MDPath, f)) and
                f.endswith(functionFileTail)]
if DEBUG:
    print(thefunctions)
    print(len(thefunctions))

for func in thefunctions:
    if DEBUG:
        print(func)
    funcfile = MDPath+func+functionFileTail
    lines = None
    with open(funcfile, 'r', encoding='utf-8') as f:
        # find the applies to status for this function
        appliesToStatus = None
        try:
            # find the status and load the content
            # can be ALL, MCT, VC, DISCOURAGE #[func.upper()
            appliesToStatus = appliesToFileContents[func.upper()]
            appliesToStatusContent = None
            if DEBUG:
                print(appliesToStatus)
            if appliesToStatus == appliesToAllFlag:
                appliesToStatusContent = "[!INCLUDE["+appliesToAllFile+"]("+appliesToPathNoRelative+appliesToAllFile+".md)]"
            elif appliesToStatus == appliesToVCFlag:
                appliesToStatusContent = "[!INCLUDE["+appliesToVisualCalculationsFile+"]("+appliesToPathNoRelative+appliesToVisualCalculationsFile+".md)]"
            elif appliesToStatus == appliesToDiscourageFlag:
                appliesToStatusContent = "[!INCLUDE["+appliesToDiscouragedForVisualCalculationsFile+"]("+appliesToPathNoRelative+appliesToDiscouragedForVisualCalculationsFile+".md)]"
            elif appliesToStatus == appliesToMCTFlag:
                appliesToStatusContent = "[!INCLUDE["+appliesToMeasuresColumnsTablesFile+"]("+appliesToPathNoRelative+appliesToMeasuresColumnsTablesFile+".md)]"
            #if appliesToStatusContent is None:
            #    raise ValueError
            # read the file
            lines = f.readlines()
            # find title line
            ind = 0
            for l in lines:
                if l.startswith(functionNameStartString):
                    break
                ind = ind+1
            # if line above title contains applies to string, replace if doesn't match,
            # otherwise, insert
            if lines[ind+2].startswith(appliesToStartString):
                if lines[ind+2].strip() == appliesToStatusContent:
                    if VERBOSE:
                        print("Applies to line present for {0} and the same. No action needed.".format(func.upper()))
                else:
                    if VERBOSE:
                        print("Applies to line present for {0} but not the same. Replacing.".format(func.upper()))
                    # do replace here
                    lines[ind+2] = appliesToStatusContent
                    lines.insert(ind+3, "\n")
            else: 
                # insert applies to
                if VERBOSE:
                    print("Applies to line missing for {0}. Inserting.".format(func.upper()))
                lines.insert(ind+1, "\n")
                lines.insert(ind+2, appliesToStatusContent)
                lines.insert(ind+3, "\n")

            if DEBUG:
                print(lines)
        except (KeyError):
            print("KeyError: {0} not found in applies-to file.".format(func.upper()))
        
    if lines is not None:
        with open(funcfile, 'w', encoding='utf8') as fout:
            fout.writelines(lines)
