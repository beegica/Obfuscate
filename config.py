# All of the variables needed for the obfuscation experiment

KEYS = ['S', 'D', 'F', 'J', 'K', 'L']
ON_KEYS = KEYS[2:4]
CONF_DICT = {k: str(20*i) for i, k in enumerate(KEYS)}
STIM_HEIGHT = 300
STIM_WIDTH = 200

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

INST1 = "In this experiment, you will be viewing a series of faces and asked to remember them as best you can. After each block of viewing faces, you will be asked to view more faces, some different images of the same people and some brand new people, and asked to identify which people you have seen already.\n\nSome of these faces will have an obfuscation over them, and some of them will be clear.\n\nYou will now see an example of the encoding phase of the experiment. Try to remember the faces as best you can.\n\nPlease note that during the main experiment there will be a different task that you must complete between the study and test phases of each block. You will not have to complete that yet.\n\nPress any key to see an example study phase."

INST2 = "You will now see some images of new people, and some new faces of the people you saw before. For this practice task, please indicated first if you have seen the person in the previous block, and then provide a confidence rating for this choice."+\
        "\n\nIf you want to indicate a Face is Old, Press %s." + \
        "\n\nIf you want to indicate a Face is New, Press %s." + \
        "\n\nThe keys for indicating confidence are %s, %s, %s, %s, %s, and %s. These keys are in order and increase in increments of 20." + \
        "\n\nPress %s for 0%% confidence, %s for 20%% confidence, and so on to %s for 100%% confidence. Your choices will be displayed on the screen in case there is any confusion." + \
        "\n\nWhen you are ready to the sample test phase, press any key!"

ENCODE_REMINDER = "In the following section, you just need to view the faces that are being shown to you on the screen.\n\nPlease try to look at them for the full duration that they are on the screen.\n\nWhen you are ready press any key!"

TEST_REMINDER = "In the following section, you will be shown faces and asked to judge if you have seen them before and your confidence in this choice. The faces wont look exactly the same, so do your best to identify if they are an old face from the previous section, or a brand new face you have never seen before." + \
                 "\n\nIf you want to indicate a Face is Old, Press %s." + \
                 "\n\nIf you want to indicate a Face is New, Press %s." + \
                 "\n\nThe keys for indicating confidence are %s, %s, %s, %s, %s, and %s. These keys are in order and increase in increments of 20." + \
                 "\n\nPress %s for 0%% confidence, %s for 20%% confidence, and so on to %s for 100%% confidence. Your choices will be displayed on the screen in case there is any confusion." + \
                 "\n\nWhen you are ready to start, press any key!"
