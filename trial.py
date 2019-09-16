from smile.common import Subroutine, Label, Parallel, Wait, UntilDone, Image,\
                         Log, KeyPress, Ref
from smile.scale import scale as s


@Subroutine
def EncodeTrial(self, config, trial_dict):
    """Show an image for encoding """
    with Parallel():
        Label(text="+", font_size=s(config.CROSS_FONT_SIZE))
        with UntilDone():
            Image(source=trial_dict['stim'],
                  height=s(config.STIM_HEIGHT),
                  width=s(config.STIM_WIDTH),
                  duration=config.STIM_ENCODE_DUR)
            Wait(config.ISI, jitter=config.ISI_JIT)
    Log(trial_dict,
        name="ENCODE")


@Subroutine
def TestTrial(self, config, trial_dict):
    """Show an image and test memory/confidence """

    stim_img = Image(source=trial_dict['stim'],
                     height=s(config.STIM_HEIGHT),
                     width=s(config.STIM_WIDTH))
    with UntilDone():

        Label(text="Old or New", font_size=s(config.FONT_SIZE),
                       top=stim_img.bottom - s(10))
        with UntilDone():

            Wait(until=stim_img.appear_time)
            kp1 = KeyPress(keys=config.ON_KEYS,
                           correct_resp=trial_dict['corr_resp'],
                           base_time=stim_img.appear_time['time'])

        # Ask for confidence
        conlbl = Label(text="Confidence?", font_size=s(config.FONT_SIZE),
                       top=stim_img.bottom - s(10))
        with UntilDone():

            Wait(until=conlbl.appear_time)
            kp2 = KeyPress(keys=config.KEYS,
                           base_time=conlbl.appear_time['time'])
            Label(text=Ref.getitem(config.CONF_DICT, kp2.pressed),
                  top=conlbl.bottom,
                  font_size=s(config.FONT_SIZE),
                  duration=config.CONF_CHOICE_VIEW)

    Log(trial_dict,
        name="TEST",
        stim_appear_time=stim_img.appear_time,
        conf_appear_time=conlbl.appear_time,
        oldnew_pressed=kp1.pressed,
        conf_pressed=kp2.pressed,
        oldnew_rt=kp1.rt,
        conf_rt=kp2.rt,
        oldnew_base_time=kp1.base_time,
        conf_base_time=kp2.base_time)
    Wait(config.ISI)


if __name__ == "__main__":

    from smile.common import Experiment
    import config
    import os

    tde = {'stim': os.path.join("assets", "inst_images", "Bart1_resize.jpg"),
           'corr_resp': "F"}
    tdt1 = {'stim': os.path.join("assets", "inst_images", "Bart2_resize.jpg"),
            'corr_resp': "F"}
    tdt2 = {'stim': os.path.join("assets", "inst_images", "Homer_test.jpg"),
            'corr_resp': "J"}
    exp = Experiment()

    Label(text="encode", duration=1.0)

    EncodeTrial(config, trial_dict=tde)

    Label(text="test", duration=1.0)

    TestTrial(config, trial_dict=tdt1)
    TestTrial(config, trial_dict=tdt2)

    exp.run()
