# All of the variables needed for the obfuscation experiment

KEYS = ['S', 'D', 'F', 'J', 'K', 'L']
ON_KEYS = KEYS[2:4]
CONF_DICT = {k: str(20*i) for i, k in enumerate(KEYS)}
STIM_HEIGHT = 300
STIM_WIDTH = 200

STIM_ENCODE_DUR = 3.0
OLDNEW_RESP_DUR = 3.0
CONF_CHOICE_VIEW = 1.0
# CONF_RESP_DUR = 3.0
ISI = 1.0

CROSS_FONT_SIZE = 50
FONT_SIZE = 35


ENCODE_REMINDER = "In the following section, you just need to view the faces that are being shown to you on the screen. Please try to look at them for the full duration that they are on the screen.\n\nWhen you are ready press any key!"

TEST_REMINDER = "In the following section, you will be shown faces and asked to judge if you have seen them before and your confidence in this choice. The faces wont look exactly the same, so do your best to identify if they are an old face from the previous section, or a brand new face you have never seen before." + \
                 "\n\nIf you want to indicate a Face is Old, Press %s." + \
                 "\n\nIf you want to indicate a Face is New, Press %s." + \
                 "\n\nThe keys for indicating confidence are %s, %s, %s, %s, %s, and %s. These keys are in order and increase in increments of 20." + \
                 "\n\nPress %s for 0%% confidence, %s for 20%% confidence, and so on to %s for 100%% confidence. Your choices will be displayed on the screen in case there is any confusion." + \
                 "\n\nWhen you are ready to start, press any key!"
