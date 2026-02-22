Please view PedAnalyze's documentation here: https://pedanalyze.readthedocs.io/

Do not use this GitHub repo, for the local Python Tkinter annotator has been discontinued. Please reference the new web version here: https://github.com/PedSim/pedanalyze-web

Please cite our paper if you use PedAnalyze or doing relevant research:

```
@inproceedings{inproceedings,
    author = {Huang, Taorui and Muktadir, Golam Md and Sripada, Srishti and Saravanan, Rishi and Yuan, Amelia and Whitehead, Jim},
    booktitle = {35th IEEE Intelligent Vehicles Symposium IV 2024 (Jeju Shinhwa World, Jeju Island, Korea)},
    year = {2024},
    title = {PedAnalyze - Pedestrian Behavior Annotator and Ontology}
}
```

**Breakdown: PedAnalyze's UI and Functionality**

- The TitleView serves as the project management system in PedAnalyze. TitleView contains an "Add New Project" button, which prompts the initiation window with fields to insert a YouTube video link, a project title, and the local path to where the annotations should be saved. A "Save Project" button enables the user to export previously made annotations regarding the video into a JSON-formatted file saved at the annotation path. Below these two buttons lays the project information, with the project title, annotation path, and video path (URL).

- The VideoView class manages the video playback and navigation. Once a new project has been initialized in TitleView, the VideoView will be rendered automatically with the target video. The VideoView controls playback via typical play, pause, and skip (left or right) buttons along with a "Current Frame" slider that can be dragged to navigate throughout the video quickly. However, to integrate with making annotations, there is also a "Start Frame" slider, an "End Frame" slider, a "Match Frame" button, a "Replay Segment" button, and a segment progress bar.

  The "Start Frame" slider and "End Frame" slider mark the starting frame and the ending frame for an annotation respectively. If the starting frame differs from the ending frame, then a MultiFrameAnnotation will be made when an annotation is saved. Otherwise, if the starting and ending frames match, a SingleFrameAnnotation will be made. The "Match Frame" button supports an easier process of making a SingleFrameAnnotation by matching the "Start Frame" and "End Frame" sliders with the current frame being played.

  To clarify the annotation being made, the video only plays when the current frame is between the "Start Frame" and "End Frame" sliders. When the current frame has reached the end frame, the video pauses by default. Thus, the "Replay Segment" button helps with replaying the MultiFrameAnnotation by resetting the current frame back to the start frame. The segment progress bar shows the current frame's progress between the start frame and the end frame.

- The AnnotationEditView class serves as the interface for users to edit and save their annotations. The AnnotationEditView provides three distinct sections with pre-defined tags in the form of check boxes to annotate (1) pedestrian behaviors, (2) vehicle behaviors, and (3) scene/environment conditions. An additional notes text box also allows the user to input any essential details that may not be able to be captured by our tags.

  A Radio Button facilitates an intuitive distinction between whether a SingleFrameAnnotation or MultiFrameAnnotation will be made. This Radio Button also updates a Label that displays the frame number(s) that will be annotated. Finally, a "Save Annotation" button sends off the annotation data and clears all check boxes as well as additional notes to prepare for a new annotation.

- The RecordingView class is a scrolling set of cards displaying all the annotations that have already been saved for the current project. Each card is called an Annotation View Widget and shows the information represented in one individual annotation, which differs slightly between a SingleFrameAnnotation and MultiFrameAnnotation. 

  Both SingleFrameAnnotations and MultiFrameAnnotations include (1) a list of pedestrian behavior tags, (2) a list of vehicle behavior tags, (3) a list of scene/environment condition tags, and (4) additional notes. The only difference are the frame stamps; SingleFrameAnnotations only have one frame number while MultiFrameAnnotations hold frame start and frame end values.

  Whenever the user saves a new annotation via the AnnotationEditView, the annotation is directly appended to the scrolling list for visualization.
](https://pedanalyze.readthedocs.io/)](https://pedanalyze.readthedocs.io/
