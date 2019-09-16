from smile.common import Subroutine, Func, Wait, Loop, Label, UntilDone,\
                         KeyPress
from smile.scale import scale as s
from listgen import gen_blocks
from instruct import Instructions
from trial import EncodeTrial, TestTrial


@Subroutine
def Obfuscation(self, config):
    blocks = Func(gen_blocks, config).result

    Instructions(config)
    Wait(config.ISI)

    with Loop(blocks) as block:

        Label(text="Prepare for a block of the experiment.\n" +
                   "Press any key to continue.",
              font_size=s(config.FONT_SIZE))
        with UntilDone():
            KeyPress()

        Wait(.3)

        Label(text=config.ENCODE_REMINDER, multiline=True,
              font_size=s(config.INST_FONT_SIZE), )
        with UntilDone():
            KeyPress()

        Wait(1.0)

        with Loop(block.current[0]) as encode_trial:
            EncodeTrial(config, trial_dict=encode_trial.current)

        # Insert something 90 seconds long here



        Label(text=config.TEST_REMINDER, multiline=True,
              font_size=s(config.INST_FONT_SIZE), )
        with UntilDone():
            KeyPress()

        Wait(1.0)

        with Loop(block.current[1]) as test_trial:
            TestTrial(config, trial_dict=test_trial.current)

        # Insert something 90 seconds long here


if __name__ == "__main__":
    from smile.common import Experiment
    from smile.startup import InputSubject
    import config

    config.TEST_REMINDER = config.TEST_REMINDER % (config.ON_KEYS[0], config.ON_KEYS[1],
                                                   config.KEYS[0], config.KEYS[1], config.KEYS[2], config.KEYS[3], config.KEYS[4], config.KEYS[5],
                                                   config.KEYS[0], config.KEYS[1], config.KEYS[5])

    exp = Experiment()

    InputSubject(name="Obfuscation")
    
    Obfuscation(config)

    Label(text="You are now finished with the experiment,\nLet your experimenter Know!",
          font_size=s(config.FONT_SIZE))
    with UntilDone():
        KeyPress()

    exp.run()
