import os
import sys


MODEL_START=60000
MODEL_END=180000
STEP=1000


PRED_DIR="/cluster/project2/mr/skasewa/models/1layer-small-s2s-fce-lang8/corruptions/"
PRED_NAME="fcec-"

path_train = ""

HEADERS = [
"export TSV_MAKER=${HOME}/stuff/project/dev/create_many_tsv.py",
"export MODEL_DIR=/cluster/project2/mr/skasewa/models/1layer-small-s2s-fce-lang8",
"export TEST_SOURCES=${HOME}/stuff/project/data/exp-data/train/fce/targets.txt",
]

print("\n".join(HEADERS))


for i in range(MODEL_END,MODEL_START,-STEP):
    commands = [" ",
                "export TEST_PREDS="+PRED_DIR+PRED_NAME+str(i),
                "python3 -m bin.infer \\",
                "  --tasks \"",
                "    - class: DecodeText", 
                "      params:",
                "        unk_replace: True\" \\",
                "  --model_dir $MODEL_DIR \\",
                "  --checkpoint_path ${MODEL_DIR}/model.ckpt-"+str(i)+" \\",
                "  --input_pipeline \"",
                "    class: ParallelTextInputPipeline",
                "    params:",
                "      source_files:",
                "        - $TEST_SOURCES\" \\",
                "  --sampler \"multinomial\" \\",
                "  --temp 0.5 \\",
                "  >  ${TEST_PREDS}.txt"," ",
                "echo \"Predictions from Model "+str(i)+" written\""," ",
                "python3 $TSV_MAKER $TEST_PREDS 1 ${TEST_PREDS}.txt $TEST_SOURCES &"]
    path_train += PRED_DIR+PRED_NAME+str(i)+".tsv,"
    print('\n'.join(commands))

print(path_train)




