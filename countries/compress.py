import ffmpy
input_name = input('Enter name of input file:' )
crf = 
output_name = input('Enter output file name: ')
if not input_name:
    inp={input_name:None}
else:
    inp={input_name:None}
outp = {output_name:'-vcodec libx264 -crf %d'%crf}
ff=ffmpy.FFmpeg(executable='C:\\ffmpeg\\bin\\ffmpeg.exe',inputs=inp,outputs=outp)
print(ff.cmd) # just to verify that it produces the correct ffmpeg command
ff.run()
print('“done!”')