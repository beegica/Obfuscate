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
                  allow_stretch=True,
                  keep_ratio=True,
                  duration=config.STIM_ENCODE_DUR)
            Wait(config.ISI, jitter=config.ISI_JIT)
    Log(trial_dict,
        name="ENCODE")


@Subroutine
def TestTrial(self, config, trial_dict):
    """Show an image and test memory/confidence """

    stim_img = Image(source=trial_dict['stim'],
                     height=s(config.STIM_HEIGHT),
                     width=s(config.STIM_WIDTH),
                     allow_stretch=True,
                     keep_ratio=True)
    with UntilDone():

        Label(text="Old or New", font_size=s(config.FONT_SIZE),
                       top=stim_img.bottom - s(10))
        with UntilDone():

            Wait(until=stim_img.appear_time)
            kp1 = KeyPress(keys=config.ON_KEYS,
                           correct_resp=trial_dict['corr_resp'],
                           base_time=stim_img.appear_time['time'])

        # Ask for confidence
        with Parallel():
            conlbl = Label(text="Confidence?", font_size=s(config.FONT_SIZE),
                           top=stim_img.bottom - s(10))
            conunderlbl = Label(text="%s" % (config.KEYS[0]),
                                top=conlbl.bottom - s(10),
                                right=self.exp.screen.center_x - s(250),
                                font_size=s(config.FONT_SIZE))
            conunderlblb = Label(text="%s" % (config.KEYS[1]),
                                top=conlbl.bottom - s(10),
                                right=self.exp.screen.center_x - s(150),
                                font_size=s(config.FONT_SIZE))
            conunderlblc = Label(text="%s" % (config.KEYS[2]),
                                top=conlbl.bottom - s(10),
                                right=self.exp.screen.center_x - s(50),
                                font_size=s(config.FONT_SIZE))
            conunderlbld = Label(text="%s" % (config.KEYS[3]),
                                top=conlbl.bottom - s(10),
                                left=self.exp.screen.center_x + s(50),
                                font_size=s(config.FONT_SIZE))
            conunderlble = Label(text="%s" % (config.KEYS[4]),
                                top=conlbl.bottom - s(10),
                                left=self.exp.screen.center_x + s(150),
                                font_size=s(config.FONT_SIZE))
            conunderlblf = Label(text="%s" % (config.KEYS[5]),
                                top=conlbl.bottom - s(10),
                                left=self.exp.screen.center_x + s(250),
                                font_size=s(config.FONT_SIZE))
            Label(text="0%",
                    top=conunderlbl.bottom - s(10),
                    center_x=conunderlbl.center_x,
                    font_size=s(config.FONT_SIZE))
            Label(text="20%",
                    top=conunderlbl.bottom - s(10),
                    center_x=conunderlblb.center_x,
                    font_size=s(config.FONT_SIZE))
            Label(text="40%",
                    top=conunderlbl.bottom - s(10),
                    center_x=conunderlblc.center_x,
                    font_size=s(config.FONT_SIZE))
            Label(text="60%",
                    top=conunderlbl.bottom - s(10),
                    center_x=conunderlbld.center_x,
                    font_size=s(config.FONT_SIZE))
            Label(text="80%",
                    top=conunderlbl.bottom - s(10),
                    center_x=conunderlble.center_x,
                    font_size=s(config.FONT_SIZE))
            Label(text="100%",
                    top=conunderlbl.bottom - s(10),
                    center_x=conunderlblf.center_x,
                    font_size=s(config.FONT_SIZE))
        with UntilDone():

            Wait(until=conlbl.appear_time)
            kp2 = KeyPress(keys=config.KEYS,
                           base_time=conlbl.appear_time['time'])

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
