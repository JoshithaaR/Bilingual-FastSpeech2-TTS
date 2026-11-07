import sys
from pathlib import Path

SHARED_SOURCE = Path(__file__).resolve().parents[1] / "FastSpeech2_Source"
if str(SHARED_SOURCE) not in sys.path:
    sys.path.insert(0, str(SHARED_SOURCE))

import argparse

import yaml

from preprocessor.preprocessor import Preprocessor


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=str, help="path to preprocess.yaml")
    args = parser.parse_args()

    config = yaml.load(open(args.config, "r"), Loader=yaml.FullLoader)
    preprocessor = Preprocessor(config)
    preprocessor.build_from_path()
