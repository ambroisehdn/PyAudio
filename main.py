#coding:utf-8
import os
import moviepy.editor as MovieEditor

# clip = MovieEditor.VideoFileClip("")
BASE_PATH = os.path.dirname(os.path.realpath(__file__))+os.path.sep
VIDEO_MEDIA_PATH = BASE_PATH+"media/video"
AUDIO_MEDIA_PATH = BASE_PATH+"media/audio"

def isFile(filePath) :
    return os.path.isfile(filePath)

def isDirectory(path) :
    return os.path.isdir(path)
    
def getVideoContents(pathContent:str) :
    
    asFileContents = []
    
    contents = os.listdir(pathContent)
    
    for content in contents :
        exceptedFilePath = pathContent+os.path.sep+str(content)
        
        if isFile(exceptedFilePath):
            asFileContents.append(exceptedFilePath)
        elif isDirectory(exceptedFilePath) :
            asFileContents.extend(getVideoContents(exceptedFilePath))
        else :
            continue
    return asFileContents

def main() :
    
    videoContents = getVideoContents(VIDEO_MEDIA_PATH)
    
    if videoContents :
        print(len(videoContents))
    else : exit("Videos folder is empty")

if __name__ == '__main__' :
    main()