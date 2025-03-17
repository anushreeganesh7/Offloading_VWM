#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Thu Oct 13 15:09:06 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'Experiment 1'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/anushree/Desktop/Experiment 1/Experiment 1.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Instruction" ---
instructions = visual.TextStim(win=win, name='instructions',
    text='This is the start of the experiment. The instructions are as follows:\nPlease press space bar to continue',
    font='Times New Roman',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_Instruction = keyboard.Keyboard()

# --- Initialize components for Routine "BlankScreen" ---
fixation_point = visual.ShapeStim(
    win=win, name='fixation_point',
    size=(0.03, 0.03), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
# Run 'Begin Experiment' code from code
import numpy as np

#randomisation of stimulus
directory = "StimulusSet/" 
stimulus_list2 = np.random.randint(1,25,5) 
stimulus1 = f'{directory}{stimulus_list2[0]}.bmp'
stimulus2 = f'{directory}{stimulus_list2[1]}.bmp'
stimulus3 = f'{directory}{stimulus_list2[2]}.bmp' 
stimulus4 = f'{directory}{stimulus_list2[3]}.bmp' 
stim5 = f'{directory}{stimulus_list2[4]}.bmp'
stim1 = stimulus1 #to assign the target image
stim2 = stimulus2
stim3 = stimulus3
stim4 = stimulus4

breakduration = 0 #counter for break routine
trialnumber = 0 #trialnumber initial counter, see begin routine for counter.

#to pick a random retrocue box orientation
retrocue_box_array = np.random.randint(1,5,1) 
orientation = "Orientation/"
rc_box1 = f'{orientation}{retrocue_box_array[0]}.jpeg'

#target present or absent condition
targetCond = np.random.randint(0,2,1)

#set sizes
setCond = np.repeat(a = [0,1,2,3],repeats = 40)
np.random.shuffle(setCond)
cond = setCond[trialnumber]

# --- Initialize components for Routine "trial" ---
boxes = visual.ImageStim(
    win=win,
    name='boxes', 
    image='box.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.165), size=(0.8, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=0.0)
img1 = visual.ImageStim(
    win=win,
    name='img1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.138, -0.02), size=(0.26, 0.26),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
img2 = visual.ImageStim(
    win=win,
    name='img2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.138, -0.02), size=(0.26, 0.26),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-2.0)
img3 = visual.ImageStim(
    win=win,
    name='img3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.138, -0.3), size=(0.26, 0.26),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-3.0)
img4 = visual.ImageStim(
    win=win,
    name='img4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.138, -0.3), size=(0.26, 0.26),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-4.0)
off_img1 = visual.ImageStim(
    win=win,
    name='off_img1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.138, -0.02), size=(0.26, 0.26),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-5.0)
off_img2 = visual.ImageStim(
    win=win,
    name='off_img2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.138, -0.02), size=(0.26, 0.26),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-6.0)
off_img3 = visual.ImageStim(
    win=win,
    name='off_img3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.138, -0.3), size=(0.26, 0.26),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-7.0)
off_img4 = visual.ImageStim(
    win=win,
    name='off_img4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.138, -0.3), size=(0.26, 0.26),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-8.0)
retrocue_box = visual.ImageStim(
    win=win,
    name='retrocue_box', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.165), size=(0.8, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-9.0)
resp_img1 = visual.ImageStim(
    win=win,
    name='resp_img1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.138, -0.02), size=(0.26, 0.26),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-10.0)
resp_img2 = visual.ImageStim(
    win=win,
    name='resp_img2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.138, -0.02), size=(0.26, 0.26),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-11.0)
resp_img3 = visual.ImageStim(
    win=win,
    name='resp_img3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.138, -0.3), size=(0.26, 0.26),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-12.0)
resp_img4 = visual.ImageStim(
    win=win,
    name='resp_img4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.138, -0.3), size=(0.26, 0.26),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-13.0)
resp_target = visual.ImageStim(
    win=win,
    name='resp_target', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-14.0)
resp_key = keyboard.Keyboard()

# --- Initialize components for Routine "intertrialinterval" ---
fixation_point_2 = visual.ShapeStim(
    win=win, name='fixation_point_2',
    size=(0.03, 0.03), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "pause_participant" ---
key_resp = keyboard.Keyboard()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "ExpEnd" ---
text_End = visual.TextStim(win=win, name='text_End',
    text='End of experiment',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Instruction" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_Instruction.keys = []
key_resp_Instruction.rt = []
_key_resp_Instruction_allKeys = []
# keep track of which components have finished
InstructionComponents = [instructions, key_resp_Instruction]
for thisComponent in InstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instruction" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructions.started')
        instructions.setAutoDraw(True)
    
    # *key_resp_Instruction* updates
    waitOnFlip = False
    if key_resp_Instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_Instruction.frameNStart = frameN  # exact frame index
        key_resp_Instruction.tStart = t  # local t and not account for scr refresh
        key_resp_Instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_Instruction, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_Instruction.started')
        key_resp_Instruction.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_Instruction.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_Instruction.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_Instruction.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_Instruction.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_Instruction_allKeys.extend(theseKeys)
        if len(_key_resp_Instruction_allKeys):
            key_resp_Instruction.keys = _key_resp_Instruction_allKeys[-1].name  # just the last key pressed
            key_resp_Instruction.rt = _key_resp_Instruction_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instruction" ---
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_Instruction.keys in ['', [], None]:  # No response was made
    key_resp_Instruction.keys = None
thisExp.addData('key_resp_Instruction.keys',key_resp_Instruction.keys)
if key_resp_Instruction.keys != None:  # we had a response
    thisExp.addData('key_resp_Instruction.rt', key_resp_Instruction.rt)
thisExp.nextEntry()
# the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=20.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code
    import numpy as np
    #randomisation of stimulus
    directory = "StimulusSet/" 
    stimulus_list2 = np.random.randint(1,25,5) 
    stimulus1 = f'{directory}{stimulus_list2[0]}.bmp' 
    stimulus2 = f'{directory}{stimulus_list2[1]}.bmp' 
    stimulus3 = f'{directory}{stimulus_list2[2]}.bmp' 
    stimulus4 = f'{directory}{stimulus_list2[3]}.bmp' 
    stim5 = f'{directory}{stimulus_list2[4]}.bmp'
    stim1 = stimulus1 #to assign the target image
    stim2 = stimulus2
    stim3 = stimulus3
    stim4 = stimulus4
    thisExp.addData('Image top-left', stimulus1)
    thisExp.addData('Image top-right', stimulus2)
    thisExp.addData('Image bottom-left', stimulus3)
    thisExp.addData('Image bottom-right', stimulus4)
    
    #Randomise box orientation
    retrocue_box_array = np.random.randint(1,4,1) 
    orientation = "Orientation/"
    rc_box1 = f'{orientation}{retrocue_box_array[0]}.jpeg'
    thisExp.addData('Box orientation', retrocue_box_array)
    
    #target present or absent condition
    targetCond = np.random.randint(0,2,1)
    thisExp.addData('Target', targetCond)
    
    #set sizes
    cond = setCond[trialnumber]
    thisExp.addData('Condition', cond)
    
    imgSet1 = [stim1, stim3, stim4]
    np.random.shuffle(imgSet1)
    #rand1 = imgSet1[0]
    #rand2 = imgSet1[1]
    #print("rand1 = ",rand1 , "rand2 = ", rand2)
    
    imgSet2 = [stim2, stim3, stim4]
    np.random.shuffle(imgSet2)
    #rand3 = imgSet2[0]
    #rand4 = imgSet2[1]
    #print("rand3 = ",rand3 , "rand4 = ", rand4)
    imgSet3 = [stim1, stim2, stim4]
    np.random.shuffle(imgSet3)
    #rand5 = imgSet3[0]
    #rand6 = imgSet3[1]
    #print("rand5 = ",rand5 , "rand6 = ", rand6)
    
    imgSet4 = [stim1, stim2, stim3]
    np.random.shuffle(imgSet4)
    #rand7 = imgSet4[0]
    #rand8 = imgSet4[1]
    #print("rand7 = ",rand7 , "rand8 = ", rand8)
    
    #print(" test" )
    #print(cond)
    #print(trialnumber)
    
    #og retrocue and target condition if loops:   
    if retrocue_box_array[0] == 1:
        if targetCond[0] == 1:
           stim5 = stimulus2
        if cond == 0:
            stim1 = f'{directory}25.bmp'
            stim3 = f'{directory}25.bmp'
            stim4 = f'{directory}25.bmp'
        if cond == 1:
            imgSet1[0]=f'{directory}25.bmp'
            imgSet1[1]=f'{directory}25.bmp'
            #print('test')
            #print(rand1)
            #print(rand2)
        if cond == 2:
            imgSet1[0]=f'{directory}25.bmp'
            #rand1 = f'{directory}25.bmp'
        stim2 = f'{directory}25.bmp'
    
    if retrocue_box_array[0] == 2:
        if targetCond[0] == 1:
           stim5 = stimulus1
        if cond == 0:
            stim2 = f'{directory}25.bmp'
            stim3 = f'{directory}25.bmp'
            stim4 = f'{directory}25.bmp'
        if cond == 1:
            imgSet2[0]= f'{directory}25.bmp'
            imgSet2[1]= f'{directory}25.bmp'
        if cond == 2:
            imgSet2[0] = f'{directory}25.bmp'
        stim1 = f'{directory}25.bmp'
    
    if retrocue_box_array[0] == 3:
        if targetCond[0] == 1:
           stim5 = stimulus3
        if cond == 0:
            stim2 = f'{directory}25.bmp'
            stim1 = f'{directory}25.bmp'
            stim4 = f'{directory}25.bmp'
            
        if cond == 1:
            imgSet3[0] = f'{directory}25.bmp'
            print(f'{imgSet3[0]}_theone')
            imgSet3[1] = f'{directory}25.bmp'
        if cond == 2:
            imgSet3[1] = f'{directory}25.bmp'
        stim3 = f'{directory}25.bmp'
    
    if retrocue_box_array[0] == 4:
        if targetCond[0] == 1:
           stim5 = stimulus4
        if cond == 0:
            stim2 = f'{directory}25.bmp'
            stim3 = f'{directory}25.bmp'
            stim1 = f'{directory}25.bmp'
        if cond == 1:
            imgSet4[0] = f'{directory}25.bmp'
            imgSet4[1]  = f'{directory}25.bmp'
        if cond == 2:
            imgSet4[0] = f'{directory}25.bmp'
        stim4 = f'{directory}25.bmp'
    
    
    
    print(imgSet3[0])
    #print("after rand1 = ",rand1 , "after rand2 = ", rand2)
    #print("after rand3 = ",rand3 , "after rand4 = ", rand4)
    #print("after rand5 = ",rand5 , "after rand6 = ", rand6)
    #print("after rand7 = ",rand7 , "after rand8 = ", rand8)
    #tracker.append(targetCond[0])
    #trialnumber += 1 #trial number counter for break routine
    # keep track of which components have finished
    BlankScreenComponents = [fixation_point]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_point* updates
        if fixation_point.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_point.frameNStart = frameN  # exact frame index
            fixation_point.tStart = t  # local t and not account for scr refresh
            fixation_point.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_point, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_point.started')
            fixation_point.setAutoDraw(True)
        if fixation_point.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_point.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_point.tStop = t  # not accounting for scr refresh
                fixation_point.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_point.stopped')
                fixation_point.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    trialnumber += 1 #trial number counter for break routine
    
    if trialnumber == 60: #consider 120 trials and this to be halfway mark
        breakduration = 1000 #break during halfway mark
    else:
        breakduration = 0
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    img1.setImage(stimulus1)
    img2.setImage(stimulus2)
    img3.setImage(stimulus3)
    img4.setImage(stimulus4)
    off_img1.setImage(stim1)
    off_img2.setImage(stim2)
    off_img3.setImage(stim3)
    off_img4.setImage(stim4)
    retrocue_box.setImage(rc_box1)
    resp_img1.setImage(stim1)
    resp_img2.setImage(stim2)
    resp_img3.setImage(stim3)
    resp_img4.setImage(stim4)
    resp_target.setImage(stim5)
    resp_key.keys = []
    resp_key.rt = []
    _resp_key_allKeys = []
    # keep track of which components have finished
    trialComponents = [boxes, img1, img2, img3, img4, off_img1, off_img2, off_img3, off_img4, retrocue_box, resp_img1, resp_img2, resp_img3, resp_img4, resp_target, resp_key]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *boxes* updates
        if boxes.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            boxes.frameNStart = frameN  # exact frame index
            boxes.tStart = t  # local t and not account for scr refresh
            boxes.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(boxes, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'boxes.started')
            boxes.setAutoDraw(True)
        if boxes.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > boxes.tStartRefresh + 1.6-frameTolerance:
                # keep track of stop time/frame for later
                boxes.tStop = t  # not accounting for scr refresh
                boxes.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'boxes.stopped')
                boxes.setAutoDraw(False)
        
        # *img1* updates
        if img1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            img1.frameNStart = frameN  # exact frame index
            img1.tStart = t  # local t and not account for scr refresh
            img1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'img1.started')
            img1.setAutoDraw(True)
        if img1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > img1.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                img1.tStop = t  # not accounting for scr refresh
                img1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'img1.stopped')
                img1.setAutoDraw(False)
        
        # *img2* updates
        if img2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            img2.frameNStart = frameN  # exact frame index
            img2.tStart = t  # local t and not account for scr refresh
            img2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'img2.started')
            img2.setAutoDraw(True)
        if img2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > img2.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                img2.tStop = t  # not accounting for scr refresh
                img2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'img2.stopped')
                img2.setAutoDraw(False)
        
        # *img3* updates
        if img3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            img3.frameNStart = frameN  # exact frame index
            img3.tStart = t  # local t and not account for scr refresh
            img3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'img3.started')
            img3.setAutoDraw(True)
        if img3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > img3.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                img3.tStop = t  # not accounting for scr refresh
                img3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'img3.stopped')
                img3.setAutoDraw(False)
        
        # *img4* updates
        if img4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            img4.frameNStart = frameN  # exact frame index
            img4.tStart = t  # local t and not account for scr refresh
            img4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'img4.started')
            img4.setAutoDraw(True)
        if img4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > img4.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                img4.tStop = t  # not accounting for scr refresh
                img4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'img4.stopped')
                img4.setAutoDraw(False)
        
        # *off_img1* updates
        if off_img1.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            off_img1.frameNStart = frameN  # exact frame index
            off_img1.tStart = t  # local t and not account for scr refresh
            off_img1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(off_img1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'off_img1.started')
            off_img1.setAutoDraw(True)
        if off_img1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > off_img1.tStartRefresh + 0.6-frameTolerance:
                # keep track of stop time/frame for later
                off_img1.tStop = t  # not accounting for scr refresh
                off_img1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'off_img1.stopped')
                off_img1.setAutoDraw(False)
        
        # *off_img2* updates
        if off_img2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            off_img2.frameNStart = frameN  # exact frame index
            off_img2.tStart = t  # local t and not account for scr refresh
            off_img2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(off_img2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'off_img2.started')
            off_img2.setAutoDraw(True)
        if off_img2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > off_img2.tStartRefresh + 0.6-frameTolerance:
                # keep track of stop time/frame for later
                off_img2.tStop = t  # not accounting for scr refresh
                off_img2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'off_img2.stopped')
                off_img2.setAutoDraw(False)
        
        # *off_img3* updates
        if off_img3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            off_img3.frameNStart = frameN  # exact frame index
            off_img3.tStart = t  # local t and not account for scr refresh
            off_img3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(off_img3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'off_img3.started')
            off_img3.setAutoDraw(True)
        if off_img3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > off_img3.tStartRefresh + 0.6-frameTolerance:
                # keep track of stop time/frame for later
                off_img3.tStop = t  # not accounting for scr refresh
                off_img3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'off_img3.stopped')
                off_img3.setAutoDraw(False)
        
        # *off_img4* updates
        if off_img4.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            off_img4.frameNStart = frameN  # exact frame index
            off_img4.tStart = t  # local t and not account for scr refresh
            off_img4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(off_img4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'off_img4.started')
            off_img4.setAutoDraw(True)
        if off_img4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > off_img4.tStartRefresh + 0.6-frameTolerance:
                # keep track of stop time/frame for later
                off_img4.tStop = t  # not accounting for scr refresh
                off_img4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'off_img4.stopped')
                off_img4.setAutoDraw(False)
        
        # *retrocue_box* updates
        if retrocue_box.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            retrocue_box.frameNStart = frameN  # exact frame index
            retrocue_box.tStart = t  # local t and not account for scr refresh
            retrocue_box.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(retrocue_box, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'retrocue_box.started')
            retrocue_box.setAutoDraw(True)
        
        # *resp_img1* updates
        if resp_img1.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            resp_img1.frameNStart = frameN  # exact frame index
            resp_img1.tStart = t  # local t and not account for scr refresh
            resp_img1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_img1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resp_img1.started')
            resp_img1.setAutoDraw(True)
        
        # *resp_img2* updates
        if resp_img2.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            resp_img2.frameNStart = frameN  # exact frame index
            resp_img2.tStart = t  # local t and not account for scr refresh
            resp_img2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_img2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resp_img2.started')
            resp_img2.setAutoDraw(True)
        
        # *resp_img3* updates
        if resp_img3.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            resp_img3.frameNStart = frameN  # exact frame index
            resp_img3.tStart = t  # local t and not account for scr refresh
            resp_img3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_img3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resp_img3.started')
            resp_img3.setAutoDraw(True)
        
        # *resp_img4* updates
        if resp_img4.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            resp_img4.frameNStart = frameN  # exact frame index
            resp_img4.tStart = t  # local t and not account for scr refresh
            resp_img4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_img4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resp_img4.started')
            resp_img4.setAutoDraw(True)
        
        # *resp_target* updates
        if resp_target.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            resp_target.frameNStart = frameN  # exact frame index
            resp_target.tStart = t  # local t and not account for scr refresh
            resp_target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_target, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resp_target.started')
            resp_target.setAutoDraw(True)
        
        # *resp_key* updates
        waitOnFlip = False
        if resp_key.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            resp_key.frameNStart = frameN  # exact frame index
            resp_key.tStart = t  # local t and not account for scr refresh
            resp_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resp_key.started')
            resp_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_key.status == STARTED and not waitOnFlip:
            theseKeys = resp_key.getKeys(keyList=['y','n'], waitRelease=False)
            _resp_key_allKeys.extend(theseKeys)
            if len(_resp_key_allKeys):
                resp_key.keys = _resp_key_allKeys[-1].name  # just the last key pressed
                resp_key.rt = _resp_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp_key.keys in ['', [], None]:  # No response was made
        resp_key.keys = None
    trials.addData('resp_key.keys',resp_key.keys)
    if resp_key.keys != None:  # we had a response
        trials.addData('resp_key.rt', resp_key.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "intertrialinterval" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    intertrialintervalComponents = [fixation_point_2]
    for thisComponent in intertrialintervalComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "intertrialinterval" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_point_2* updates
        if fixation_point_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_point_2.frameNStart = frameN  # exact frame index
            fixation_point_2.tStart = t  # local t and not account for scr refresh
            fixation_point_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_point_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_point_2.started')
            fixation_point_2.setAutoDraw(True)
        if fixation_point_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_point_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_point_2.tStop = t  # not accounting for scr refresh
                fixation_point_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_point_2.stopped')
                fixation_point_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intertrialintervalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "intertrialinterval" ---
    for thisComponent in intertrialintervalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "pause_participant" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    text.setText('This is a break, now you are halfway done! \nPress space to continue')
    # keep track of which components have finished
    pause_participantComponents = [key_resp, text]
    for thisComponent in pause_participantComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "pause_participant" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + breakduration-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.stopped')
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + breakduration-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pause_participantComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pause_participant" ---
    for thisComponent in pause_participantComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    # the Routine "pause_participant" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 20.0 repeats of 'trials'


# --- Prepare to start Routine "ExpEnd" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
ExpEndComponents = [text_End]
for thisComponent in ExpEndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "ExpEnd" ---
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_End* updates
    if text_End.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_End.frameNStart = frameN  # exact frame index
        text_End.tStart = t  # local t and not account for scr refresh
        text_End.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_End, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_End.started')
        text_End.setAutoDraw(True)
    if text_End.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_End.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_End.tStop = t  # not accounting for scr refresh
            text_End.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_End.stopped')
            text_End.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ExpEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ExpEnd" ---
for thisComponent in ExpEndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)
# Run 'End Experiment' code from code
#import numpy as np
#np.savetxt(f'tracker{np.random.rand()}.txt', tracker)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
