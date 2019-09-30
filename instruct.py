

from smile.common import Subroutine, Func, Label, UntilDone, KeyPress, Wait, \
                         Loop
from smile.scale import scale as s
from trial import EncodeTrial, TestTrial

import os


def gen_instruct_blocks(config):
    encode = []
    encode.append({"stim": os.path.join("assets", "inst_images",
                                        "Bart2_resize.jpg"),
                   "cond": "INST",
                   "trail_type": "INST"})
    encode.append({"stim": os.path.join("assets", "inst_images",
                                        "homer_study_bar.jpg"),
                   "cond": "INST",
                   "trail_type": "INST"})

    test = []
    test.append({"stim": os.path.join("assets", "inst_images",
                                      "Bart1_resize.jpg"),
                 "encode_cond": "INST",
                 "cond": "OLD",
                 "corr_resp": config.ON_KEYS[0]})
    test.append({"stim": os.path.join("assets", "inst_images",
                                      "Morty_resize.jpg"),
                 "encode_cond": "INST",
                 "cond": "OLD",
                 "corr_resp": config.ON_KEYS[1]})
    test.append({"stim": os.path.join("assets", "inst_images",
                                      "homer_test.jpg"),
                 "encode_cond": "INST",
                 "cond": "OLD",
                 "corr_resp": config.ON_KEYS[0]})
    test.append({"stim": os.path.join("assets", "inst_images", "Zapp.jpg"),
                 "encode_cond": "INST",
                 "cond": "OLD",
                 "corr_resp": config.ON_KEYS[1]})
    return [encode, test]


@Subroutine
def Instruct(self, config):

    et = Func(gen_instruct_blocks, config)

    Label(text=config.INST1, font_size=s(config.INST_FONT_SIZE),
          text_size=(s(1000), None))
    with UntilDone():
        KeyPress()
    Wait(.5)

    with Loop(et.result[0]) as lp:
        EncodeTrial(config, lp.current)

    Label(text=config.INST2, font_size=s(config.INST_FONT_SIZE),
          text_size=(s(1000), None))
    with UntilDone():
        KeyPress()
    Wait(.5)

    Label(text=config.INST3, font_size=s(config.INST_FONT_SIZE),
          text_size=(s(1000), None))
    with UntilDone():
        KeyPress()
    Wait(.5)

    Label(text=config.INST4, font_size=s(config.INST_FONT_SIZE),
          text_size=(s(1000), None))
    with UntilDone():
        KeyPress()
    Wait(.5)


    with Loop(et.result[1]) as lp:
        TestTrial(config, lp.current)


if __name__ == "__main__":
    from smile.common import Experiment
    import config
    config.INST2 = config.INST2 % (config.ON_KEYS[0], config.ON_KEYS[1],
                                                   config.KEYS[0], config.KEYS[1], config.KEYS[2], config.KEYS[3], config.KEYS[4], config.KEYS[5],
                                                   config.KEYS[0], config.KEYS[1], config.KEYS[5])
    exp = Experiment()

    Instruct(config)

    exp.run()
