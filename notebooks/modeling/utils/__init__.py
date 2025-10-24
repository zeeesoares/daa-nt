import os
from dotenv import load_dotenv

load_dotenv()

TRAIN_PATH = os.getenv("TRAIN_PATH")
TEST_PATH = os.getenv("TEST_PATH")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "../submissions")

print(f"[utils] TRAIN_PATH={TRAIN_PATH}")
print(f"[utils] TEST_PATH={TEST_PATH}")
print(f"[utils] OUTPUT_DIR={OUTPUT_DIR}")
