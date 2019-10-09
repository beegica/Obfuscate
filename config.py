# -*- coding: utf-8 -*-
# All of the variables needed for the obfuscation experiment

KEYS = ['S', 'D', 'F', 'J', 'K', 'L']
ON_KEYS = KEYS[2:4]
CONF_DICT = {k: str(20*i) for i, k in enumerate(KEYS)}
STIM_HEIGHT = 500
STIM_WIDTH = 300

STIM_ENCODE_DUR = 4.0
OLDNEW_RESP_DUR = 3.0
INTER_PART_WAIT = 90
CONF_CHOICE_VIEW = 1.0
# CONF_RESP_DUR = 3.0
ISI = .4
ISI_JIT = .2

CROSS_FONT_SIZE = 50
FONT_SIZE = 35
INST_FONT_SIZE = 35

BLOCKS = ["OBS", "CLE"]
RECE_TRIAL_LEN = 2
PRIM_TRIAL_LEN = 2
ENCODE_TRIAL_LEN = 18

INST1 = "In this experiment, you will be viewing pictures of faces. Please pay attention, as we will ask you to remember these people later in the experiment.\n\nBefore beginning, we will do a practice version of the task.\n\nPress any key to see an example study phase"

INST2 = "You will now be tested on your memory of the faces you studied previously. Some images will be people you studied. Others will be completely new.\n\nPress any key to continue."

INST3 = "Note that simple features of the faces, such as color or orientation, may be different from the images you saw before. You are asked to accurately remember the person that appeared on the screen during this session, rather than the specific image.\n\nPress any key to continue."

INST4 = "You will now see some images of new people, and people you saw before. For this practice task, please indicate first if you have seen the person, and then provide a confidence rating for this choice."+\
        "\n\nIf you want to indicate you have Seen the Face, Press %s." + \
        "\n\nIf you want to indicate that this is a new Face, Press %s." + \
        "\n\nThe keys for indicating confidence are %s, %s, %s, %s, %s, and %s. These keys are in order and increase in increments of 20." + \
        "\n\nPress %s for 0%% confidence, %s for 20%% confidence, and so on to %s for 100%% confidence. Your choices will be displayed on the screen in case there is any confusion." + \
        "\n\nWhen you are ready to the sample test phase, press any key!"

ENCODE_REMINDER = "In the following section, you just need to view the faces that are being shown to you on the screen.\n\nPlease pay attention to them for the full duration that they are on the screen.\n\nWhen you are ready press any key!"

TEST_REMINDER = "In the following section, you will be shown faces and asked to judge if you have seen them before and your confidence in this choice. The faces won’t look exactly the same, so do your best to identify if they are a face you have seen previously, or a brand new face you have never seen before." + \
                 "\n\nIf you want to indicate a Face is Seen, Press %s." + \
                 "\n\nIf you want to indicate a Face is New, Press %s." + \
                 "\n\nThe keys for indicating confidence are %s, %s, %s, %s, %s, and %s. These keys are in order and increase in increments of 20." + \
                 "\n\nPress %s for 0%% confidence, %s for 20%% confidence, and so on to %s for 100%% confidence. Your choices will be displayed on the screen in case there is any confusion." + \
                 "\n\nWhen you are ready to start, press any key!"
