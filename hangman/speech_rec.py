import speech_recognition as sr
import audiomath; audiomath.RequireAudiomathVersion( '1.12.0' )

class DuckTypedMicrophone( sr.AudioSource ): # descent from AudioSource is required purely to pass an assertion in Recognizer.listen()
    def __init__( self, device=None, chunkSeconds=1024/44100.0 ):  # 1024 samples at 44100 Hz is about 23 ms
        self.recorder = None
        self.device = device
        self.x=0
        self.chunkSeconds = chunkSeconds
    def __enter__( self ):
        self.nSamplesRead = 0
        self.recorder = audiomath.Recorder( audiomath.Sound( 5, nChannels=1 ), loop=True, device=self.device )
        # Attributes required by Recognizer.listen():
        self.CHUNK = audiomath.SecondsToSamples( self.chunkSeconds, self.recorder.fs, int )
        self.SAMPLE_RATE = int( self.recorder.fs )
        self.SAMPLE_WIDTH = self.recorder.sound.nbytes
        return self
    def __exit__( self, *blx ):
        self.recorder.Stop()
        self.recorder = None
    def read( self, nSamples ):
        self.x+=1
        if self.x>120:
            return
        sampleArray = self.recorder.ReadSamples( self.nSamplesRead, nSamples )
        self.nSamplesRead += nSamples
        return self.recorder.sound.dat2str( sampleArray )
    @property
    def stream( self ): # attribute must be present to pass an assertion in Recognizer.listen(), and its value must have a .read() method
        return self if self.recorder else None
