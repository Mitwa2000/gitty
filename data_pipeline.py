from functions import *
import time
import datetime

print("Starting the data pipeline",datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

print("---------------------------------------------------------------------")


# STep 1:exract video ID's

t0=time.time() # before capturing time
getVideoIDs()
t1=time.time() # after capturing time
print("Step 1: Done")
print("-----> Video IDs download in",str(t1-t0),"seconds","\n") # time tken by the function


# step 2: Extract the transcripts for he videos
t0=time.time() 
getVideoTranscripts()
t1=time.time()
print("Step 2: Done" )
print("----> Transcripts downlaod in",str(t1-t0),"seconds")


# step 3: transform data function
t0=time.time()
transformData()
t1=time.time()
print("Step 3: Done")
print("----> Data Transformed in",str(t1-t0),"seconds")

# step 4: generate text embeddings
t0=time.time()
createtextembeddings()
t1=time.time()
print("Step 4: Done")
print("----> EMbeddings generated in",str(t1-t0),"seconds")