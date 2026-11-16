import hashlib
import secrets

import numpy as np


def generate_key() -> str:
    return secrets.token_urlsafe(24)


def generate_indices(key: str, sample_count: int) -> np.ndarray:
    if not key:
        raise ValueError("Ключ не може бути порожнім")

    seed = int.from_bytes(hashlib.sha256(key.encode("utf-8")).digest(), "big")
    return np.random.default_rng(seed).permutation(sample_count)
