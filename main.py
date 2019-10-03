from smile.common import Subroutine, Func, Wait, Loop, Label, UntilDone,\
                         KeyPress, Parallel, Serial
from smile.scale import scale as s
from listgen import gen_stim
from instruct import Instruct
from trial import EncodeTrial, TestTrial
from flanker import config as Flanker_config
from flanker import FlankerExp


@Subroutine
def Obfuscation(self, config):
    blocks = Func(gen_stim, config, ".").result

    Instruct(config)

    Label(text="You have now finished the practice instructions.\n" +
               "Press any key to continue to the main experiment.",
          font_size=s(config.FONT_SIZE))
    with UntilDone():
        KeyPress()

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

        Label(text="You are now about to do a different task before being tested.\n\nPress any key to continue.",
              font_size=s(config.FONT_SIZE))
        with UntilDone():
            KeyPress()

        with Serial():
            FlankerExp(Flanker_config,
                       run_num=block.i,
                       lang="E",
                       pulse_server=None)
            Label(text="Please wait, the rest of the experiment will begin shortly.",
                  font_size=s(config.FONT_SIZE))
        with UntilDone():
            Wait(config.INTER_PART_WAIT)

        Label(text=config.TEST_REMINDER, multiline=True,
              font_size=s(config.INST_FONT_SIZE), )
        with UntilDone():
            KeyPress()

        Wait(1.0)

        with Loop(block.current[1]) as test_trial:
            TestTrial(config, trial_dict=test_trial.current)

        Label(text="You are now about to do a different task before going onto the next block.\n\nPress any key to continue.",
              font_size=s(config.FONT_SIZE), text_size=(s(1000), None))
        with UntilDone():
            KeyPress()

        with Serial():
            FlankerExp(Flanker_config,
                       run_num=block.i,
                       lang="E",
                       pulse_server=None)
            Label(text="Please wait, the rest of the experiment will begin shortly.",
                  font_size=s(config.FONT_SIZE))
        with UntilDone():
            Wait(config.INTER_PART_WAIT)


if __name__ == "__main__":
    from smile.common import Experiment
    from smile.startup import InputSubject
    import config

    config.TEST_REMINDER = config.TEST_REMINDER % (config.ON_KEYS[0], config.ON_KEYS[1],
                                                   config.KEYS[0], config.KEYS[1], config.KEYS[2], config.KEYS[3], config.KEYS[4], config.KEYS[5],
                                                   config.KEYS[0], config.KEYS[1], config.KEYS[5])

    config.INST4 = config.INST4 % (config.ON_KEYS[0], config.ON_KEYS[1],
                                   config.KEYS[0], config.KEYS[1], config.KEYS[2], config.KEYS[3], config.KEYS[4], config.KEYS[5],
                                   config.KEYS[0], config.KEYS[1], config.KEYS[5])
    Flanker_config.RESP_KEYS = config.ON_KEYS[:]
    Flanker_config.CONT_KEY = config.ON_KEYS[:]
    Flanker_config.TOUCH = False
    exp = Experiment(background_color=(.35, .35, .35, 1.0),
                     name="obfuscate")

    InputSubject(name="Obfuscation")

    Obfuscation(config)

    Label(text="You are now finished with the experiment,\nLet your experimenter Know!",
          font_size=s(config.FONT_SIZE))
    with UntilDone():
        KeyPress()

    exp.run()
