"""
Utility script to split `reference.csv` into public and private subsets.

The public subset contains a random 30% sample (random_state=2) sorted by ID.
The private subset holds the remaining 70% sorted by the same ID column.
Both outputs are written next to the original file and are ignored by git.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    ref_path = base_dir / "reference.csv"
    public_path = base_dir / "reference_public.csv"
    private_path = base_dir / "reference_private.csv"

    if not ref_path.exists():
        raise FileNotFoundError(f"Reference file not found at {ref_path}")

    ref = pd.read_csv(ref_path)
    id_column = _identify_id_column(ref)

    public = (
        ref.sample(n=round(0.3 * len(ref)), random_state=2)
        .sort_values(id_column)
        .reset_index(drop=True)
    )
    private = (
        ref[~ref[id_column].isin(public[id_column])]
        .sort_values(id_column)
        .reset_index(drop=True)
    )

    public.to_csv(public_path, index=False)
    private.to_csv(private_path, index=False)

    print(f"Public reference saved to: {public_path}")
    print(f"Private reference saved to: {private_path}")


def _identify_id_column(df: pd.DataFrame) -> str:
    """Return the ID column name (defaults to `image_id`)."""
    candidates = ["ID", "id", "image_id"]
    for name in candidates:
        if name in df.columns:
            return name
    raise ValueError(
        "Unable to find an ID column. Supported column names: "
        + ", ".join(candidates)
    )


if __name__ == "__main__":
    main()

