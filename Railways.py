import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS
import matplotlib
def textTospeech(text, file):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(file)

def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined
def aa_rahi_hai():
    # yatri kripaya dhyaan de 
    aud=AudioSegment.from_mp3("real_announcement.mp3")
    str=0000
    end=3200
    processed= aud[str:end]
    processed.export("1.mp3", format="mp3")
    # ke raaste 1
    str=4650
    end=5500
    processed= aud[str:end]
    processed.export("3.mp3", format="mp3")
    # se aane wali
    str=6900
    end=8000
    processed= aud[str:end]
    processed.export("5.mp3", format="mp3")
     # ke raaste 2
    str=4650
    end=5500
    processed= aud[str:end]
    processed.export("7.mp3", format="mp3")
    # ko jaane wali gaadi sankhya
    str=12000
    end=14700
    processed= aud[str:end]
    processed.export("9.mp3", format="mp3")
    #platform no.
    str=19000
    end=20050
    processed= aud[str:end]
    processed.export("11.mp3", format="mp3")
    # par aa rahi hai 
    str=21000
    end=24000
    processed= aud[str:end]
    processed.export("13.mp3", format="mp3")

def generationg_file(file):
    fl=pd.read_excel(file)
    print(fl)
    for index, item in fl.iterrows():
        textTospeech(item["from_via"],"2.mp3")     

        textTospeech(item["from_station"],"4.mp3") 

        textTospeech(item["To_via"],"6.mp3")

        textTospeech(item["To_station"],"8.mp3")

        textTospeech(item["train_num"]+"  "+ item["train_name"] ,"10.mp3")

        textTospeech(item["platform"],"12.mp3")

        
        audios = [f"{i}.mp3" for i in range(1,14)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement{index+1}.mp3", format="mp3")

def delay():
    aud=AudioSegment.from_mp3("merged_annon.mp3")
    #yatri kripiya dhyaan de
    str=0000
    end=3800
    processed= aud[str:end]
    processed.export("1_1.mp3", format="mp3")
    # ke raaste
    str=5300
    end=6400
    processed= aud[str:end]
    processed.export("1_3.mp3", format="mp3")
    # se aane wali
    str=7500
    end=8700
    processed= aud[str:end]
    processed.export("1_5.mp3", format="mp3")
    # ko jaane wali gaadi sankhya
    str=12000
    end=14500
    processed= aud[str:end]
    processed.export("1_7.mp3", format="mp3")
    # apne nirdharit samay se
    str=19000
    end=21000
    processed= aud[str:end]
    processed.export("1_9.mp3", format="mp3")
    # ghante ki deri se chal rahi hai 
    str=22000
    end=24000
    processed= aud[str:end]
    processed.export("1_11.mp3", format="mp3")
    #aapko hui asuvidha ke liye hame khed hai 
    str=30000
    end=35600
    processed= aud[str:end]
    processed.export("1_12.mp3", format="mp3")

def generationg_file_delay(file):
    fl=pd.read_excel(file)
    print(fl)
    for index, item in fl.iterrows():
        textTospeech(item["from_via"],"1_2.mp3")     

        textTospeech(item["from_station"],"1_4.mp3") 

        textTospeech(item["To_station"],"1_6.mp3")

        textTospeech(item["train_num"]+"  "+ item["train_name"] ,"1_8.mp3")

        textTospeech(item["delay_hour"],"1_10.mp3")

        
        audios = [f"1_{i}.mp3" for i in range(1,13)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement{index+1}.mp3", format="mp3")

def platform_par_khadi_hai():
    aud=AudioSegment.from_mp3("merged_annon.mp3")
    #yatri kripiya dhyaan de
    str=0000
    end=3800
    processed= aud[str:end]
    processed.export("2_1.mp3", format="mp3")
    # ke raaste
    str=5300
    end=6400
    processed= aud[str:end]
    processed.export("2_3.mp3", format="mp3")
    # se aane wali
    str=7500
    end=8700
    processed= aud[str:end]
    processed.export("2_5.mp3", format="mp3")
    # ko jaane wali gaadi sankhya
    str=12000
    end=14500
    processed= aud[str:end]
    processed.export("2_7.mp3", format="mp3")    
    # platform no.
    str=52500
    end=53500
    processed= aud[str:end]
    processed.export("2_9.mp3", format="mp3")
    # par khadi hai 
    str=54000
    end=55500
    processed= aud[str:end]
    processed.export("2_11.mp3", format="mp3")

def generationg_file_at_station(file):
    fl=pd.read_excel(file)
    print(fl)
    for index, item in fl.iterrows():
        textTospeech(item["from_via"],"2_2.mp3")     

        textTospeech(item["from_station"],"2_4.mp3") 

        textTospeech(item["To_station"],"2_6.mp3")

        textTospeech(item["train_num"]+"  "+ item["train_name"] ,"2_8.mp3")

        textTospeech(item["platform"],"2_10.mp3")

        
        audios = [f"2_{i}.mp3" for i in range(1,12)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement{index+1}.mp3", format="mp3")

def departure():
    aud=AudioSegment.from_mp3("merged_annon.mp3")
    #yatri kripiya dhyaan de
    str=0000
    end=3800
    processed= aud[str:end]
    processed.export("3_1.mp3", format="mp3")
    # ke raaste
    str=5300
    end=6400
    processed= aud[str:end]
    processed.export("3_3.mp3", format="mp3")
    # ko jaane wali gaadi sankhya
    str=12000
    end=14500
    processed= aud[str:end]
    processed.export("3_5.mp3", format="mp3")    
    # apne nirdharit samay 
    str=19000
    end=20600
    processed= aud[str:end]
    processed.export("3_7.mp3", format="mp3")
    # platform no.
    str=52500
    end=53500
    processed= aud[str:end]
    processed.export("3_9.mp3", format="mp3")
    #se jayegi
    str=73000
    end=76000
    processed= aud[str:end]
    processed.export("3_11.mp3", format="mp3")

def generationg_file_departure(file):
    fl=pd.read_excel(file)
    print(fl)
    for index, item in fl.iterrows():
        textTospeech(item["from_via"],"3_2.mp3")     

        textTospeech(item["To_station"],"3_4.mp3")

        textTospeech(item["train_num"]+"  "+ item["train_name"] ,"3_6.mp3")

        textTospeech(item["departure_time"] ,"3_8.mp3")

        textTospeech(item["platform"],"3_10.mp3")

        
        audios = [f"3_{i}.mp3" for i in range(1,12)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement{index+1}.mp3", format="mp3")
if __name__=="__main__":
    print("Welcome To INDIAN RAILWAYS")
    #aa_rahi_hai()
    #platform_par_khadi_hai()
    #departure()
    #generationg_file('anno.xlsx')
    delay()
    generationg_file_delay('anno.xlsx')
    
   
