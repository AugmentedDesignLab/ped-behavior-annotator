from model import MultiFrameAnnotation, SingleFrameAnnotation
from model.PedestrianTag import PedestrianTag
from model.Recording import Recording
from model.RecordingRepository import RecordingRepository
from model.SceneTag import SceneTag
from model.VehicleTag import VehicleTag
def test_save():
    recording = Recording("Test-Recording","c:\\test-recordingpath", "c:\\test-recordingpath\\annotations")
    recording.name = "Test-Recording"
    recording.video_path = "c:\\test-recordingpath"
    recording.annotation_path = "c:\\test-recordingpath\\annotations"
    recording.multiFrameAnnotations = MultiFrameAnnotation(0.0, 10.0, 15.0, 25.0)
    recording.multiFrameAnnotations.frameStart = 0.0
    recording.multiFrameAnnotations.frameEnd = 10.0
    recording.multiFrameAnnotations.timeEnd = 15.0
    recording.multiFrameAnnotations.tags = {SceneTag.RedLight.value}

    recording.singleFrameAnnotation = SingleFrameAnnotation(0.0, 10)
    recording.singleFrameAnnotation.frameStart = 0.0
    recording.singleFrameAnnotation.frameEnd = 10.0
    recording.singleFrameAnnotation.timeEnd = 15.0
    recording.singleFrameAnnotation.pedTags = {PedestrianTag.Jaywalking.value}
    recording.singleFrameAnnotation.egoTags = {VehicleTag.Speeding.value}
    recording.singleFrameAnnotation.sceneTags = {SceneTag.RedLight.value}

    location = "c:\\SIP\\code\\testrecording.json"
    repository = RecordingRepository(location)
    repository.save(recording)

    expectedResult = "\"Recording(name: Test-Recording,'annotation_path': c:\\\\test-recordingpath\\\\annotations, 'video_path': c:\\\\test-recordingpath, 'multiFrameAnnotations': MultiFrameAnnotations(timeStart=0.0, timeEnd=15.0, frameStart=0.0, frameEnd=10.0, tags={'Red Light'}),'singleFrameAnnotation':SingleFrameAnnotation(time=0.0, frame=10, pedTags={'Jaywalking'}, egoTags={'Speeding'}, sceneTags={'Red Light'})\"\n"
    file = open(location, 'r')
    writtenData = file.readline()

    file.close()
    assert (expectedResult == writtenData)
