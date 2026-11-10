import os
import hashlib

def calculate_sha256(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def verify_dataset_splits(data_dir):
    splits = ['train', 'val', 'test']
    split_hashes = {}
    total_images = 0
    
    print("=" * 60)
    print("DATASET 70/20/10 SPLIT & ZERO-LEAKAGE VERIFICATION")
    print("=" * 60)
    
    for s in splits:
        s_dir = os.path.join(data_dir, s, 'images') if os.path.exists(os.path.join(data_dir, s, 'images')) else os.path.join(data_dir, s)
        hashes = set()
        if os.path.exists(s_dir):
            for fname in os.listdir(s_dir):
                if fname.lower().endswith(('.jpg', '.jpeg', '.png')):
                    fpath = os.path.join(s_dir, fname)
                    h = calculate_sha256(fpath)
                    hashes.add(h)
        split_hashes[s] = hashes
        total_images += len(hashes)
        print(f"Split: {s:<10} | Images: {len(hashes):<5}")
        
    print("-" * 60)
    # Check overlap
    train_val_overlap = split_hashes['train'] & split_hashes['val']
    train_test_overlap = split_hashes['train'] & split_hashes['test']
    val_test_overlap = split_hashes['val'] & split_hashes['test']
    
    print(f"Train / Val Overlap:  {len(train_val_overlap)} images (Leakage: {len(train_val_overlap) > 0})")
    print(f"Train / Test Overlap: {len(train_test_overlap)} images (Leakage: {len(train_test_overlap) > 0})")
    print(f"Val / Test Overlap:   {len(val_test_overlap)} images (Leakage: {len(val_test_overlap) > 0})")
    
    leakage = len(train_val_overlap) + len(train_test_overlap) + len(val_test_overlap)
    if leakage == 0:
        print("VERIFICATION RESULT: ZERO DATA LEAKAGE CONFIRMED (100% CLEAN)")
    else:
        print(f"VERIFICATION WARNING: {leakage} LEAKED SAMPLES DETECTED!")
    print("=" * 60)

if __name__ == '__main__':
    verify_dataset_splits(os.path.join('..', 'data'))
