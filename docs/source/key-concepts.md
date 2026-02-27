# User Guide - Main Features

## Pre-defined tags
Pre-defined behavior tags are split into four categories: pedestrian behavior, vehicle behavior, environment conditions, and pedestrian demographics. They are accessible in the AnnotationEditView, in the form of check boxes, to annotate the behaviors and conditions in each frame or group of frames. Using pre-defined tags allows for unity across annotations and resulting data sets and makes it easier to identify patterns or common pedestrian-vehicle interaction scenarios. 

## Multi-frame annotation
![Data Model of a Video Recording](multiframe-annotation.png)
Multi-frame annotation describes pedestrian behavior seen across a sequence of frames.

## Public video annotation
PedAnalyze makes it possible to annotate public videos of pedestrian-vehicle accidents or near-miss scenarios stored on the internet, generally posted on platforms such as YouTube or Instagram. On these platforms, there exists an abundance of footage that the public has already organized into compilations. By directly supporting YouTube links, and direct access to videos on other social media platforms coming in the future, PedAnalyze is able to access this useful yet untapped set of pre-compiled interactions and provide a tool to easily identify and annotate behaviors.

## Structure of the dataset
![Data Model of a Video Recording](data-model.png)

The behavior tags for pedestrian decision-making are inspired by YouTube video observations, PSI Dataset annotations, and various factors influencing pedestrian crossing decisions. The tags are categorized into four main types: Pedestrian Behaviors, Vehicle Behaviors, Environment Conditions, and Pedestrian Demographics. These categories help describe key interactions and context factors in multi-frame scenes.

Pedestrian behavior tags are further divided into subsets like Instant Reaction, Collision, Interaction, Mental State, and Intention. Vehicle behavior tags include subsets like Collision, Interaction, and Irregular phenomena. The tagging system is designed to be intuitive and scalable, incorporating ideas from existing literature to enhance pedestrian behavior analysis.