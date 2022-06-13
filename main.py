#coding:utf-8
import os,ntpath
import moviepy.editor as MovieEditor

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

def toMp3(videoClip:MovieEditor.VideoFileClip,audioFileName:str):
    return videoClip.audio.write_audiofile(audioFileName)

def makeDire(path):
    
    if not isDirectory(path) :
        os.makedirs(path)
  
def fileNameFromFilePath(path) -> str : 
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)    

def mp3FileName(path : str) -> str:
    return  fileNameFromFilePath(path).split(".")[0]+".mp3"

def convertToMp3(videoToconverts:list) :
    
    if videoToconverts :
        for video in videoToconverts :
            try :
                videoClip = MovieEditor.VideoFileClip(video)
                exceptAudioDir = os.path.dirname(video).replace('video','audio')+os.path.sep
                makeDire(exceptAudioDir)
                fullFileName = exceptAudioDir+mp3FileName(video)
                toMp3(videoClip,fullFileName)
                print(fullFileName)
            except IndexError:
                continue
            except OSError :
                continue
    else : exit("The folder is empty")
    
def main() :
    
    videoContents = getVideoContents(VIDEO_MEDIA_PATH)
    convertToMp3(videoContents)

if __name__ == '__main__' :
    main()