import pandas as pd
import os
from datetime import datetime
from . import OUTPUT_DIR

def create_submission_file(df, prediction_col='Speed_Diff', filename=None, output_dir=None):
    if output_dir is None:
        output_dir = OUTPUT_DIR

    os.makedirs(output_dir, exist_ok=True)

    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"submission_{timestamp}.csv"

    path = os.path.join(output_dir, filename)

    submission = pd.DataFrame({
        'RowId': range(1, len(df) + 1),
        'Speed_Diff': df[prediction_col]
    })

    submission.to_csv(path, index=False)
    print(f"Submissão criada: {path}")
    return path
