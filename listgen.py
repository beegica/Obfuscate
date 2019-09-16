import os
import random
from glob import glob

def gen_stim(config, task_dir):

    # Create Master List
    obs_list = glob(os.path.join(task_dir, "assets", "stim", "obs", "*.jpg"))
    cle_list = glob(os.path.join(task_dir, "assets", "stim", "clear", "*.jpg"))
    rec_list = glob(os.path.join(task_dir, "assets", "stim", "recog", "*.jpg"))
    master_list = list(zip(obs_list, cle_list, rec_list))
    random.shuffle(master_list)

    # Create PRIMACY List
    fir_obs_list = glob(os.path.join(task_dir, "assets",
                                     "stim", "primacy", "prim_obs", "*.jpg"))
    fir_cle_list = glob(os.path.join(task_dir, "assets",
                                     "stim", "primacy", "prim_clear", "*.jpg"))
    fir_list = list(zip(fir_obs_list, fir_cle_list))
    random.shuffle(fir_list)

    # Create RECENCY List
    las_obs_list = glob(os.path.join(task_dir, "assets",
                                     "stim", "recency",
                                     "recency_obs", "*.jpg"))
    las_cle_list = glob(os.path.join(task_dir, "assets",
                                     "stim", "recency",
                                     "recency_clear", "*.jpg"))
    las_list = list(zip(las_obs_list, las_cle_list))
    random.shuffle(las_list)

    blocks = []
    for block in config.BLOCKS:
        encode = []
        test = []
        # Create Primacy Trials
        for p in range(config.PRIM_TRIAL_LEN):
            te = {}
            trial = fir_list.pop()
            if block == "OBS":
                te['stim'] = trial[0]
            elif block == "CLE":
                te['stim'] = trial[1]
            te['cond'] = block
            te['trial_type'] = "PRIMACY"
            encode.append(te.copy())

        # Create Encoding Trials
        for c in range(config.ENCODE_TRIAL_LEN):
            te = {}
            tto = {}
            ttn = {}
            trial = master_list.pop()

            # Create Encode Trial
            if block == "OBS":
                te['stim'] = trial[0]
            elif block == "CLE":
                te['stim'] = trial[1]
            te['cond'] = block
            te['trial_type'] = "ENCODE"
            encode.append(te.copy())

            # Create Corresponding Test Trial
            tto['stim'] = trial[2]
            tto['encode_cond'] = block
            tto['cond'] = "OLD"
            tto['corr_resp'] = config.ON_KEYS[0]
            test.append(tto.copy())

            # Create Corresponding Lure Trial
            trial = master_list.pop()
            ttn['stim'] = trial[2]
            ttn['encode_cond'] = block
            ttn['cond'] = "NEW"
            ttn['corr_resp'] = config.ON_KEYS[-1]
            test.append(ttn.copy())

        # Create Recency Trials
        for r in range(config.RECE_TRIAL_LEN):
            te = {}
            trial = las_list.pop()
            if block == "OBS":
                te['stim'] = trial[0]
            elif block == "CLE":
                te['stim'] = trial[1]
            te['cond'] = block
            te['trial_type'] = "RECENCY"
            encode.append(te.copy())
        random.shuffle(encode)
        random.shuffle(test)
        blocks.append([encode, test])
    return blocks


if __name__ == "__main__":
    import config
    task_dir = "."

    blocks = gen_stim(config, task_dir)

    for b in blocks:
        print(b[0][0]['cond'], len(b[0]), len(b[1]))
