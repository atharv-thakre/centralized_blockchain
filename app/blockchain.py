# app/blockchain.py
import hashlib
import json
from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Session
from app import models

def compute_hash(index: int, timestamp: str, data: str, previous_hash: str) -> str:
    payload = f"{index}{timestamp}{data}{previous_hash}"
    return hashlib.sha256(payload.encode('utf-8')).hexdigest()

def get_last_block(db: Session) -> Optional[models.Block]:
    return db.query(models.Block).order_by(models.Block.index.desc()).first()

def create_genesis_block(db: Session):
    last = get_last_block(db)
    if last is not None:
        return last
    index = 0
    timestamp = datetime.utcnow().isoformat()
    data = json.dumps({"action": "genesis"})
    previous_hash = "0"
    h = compute_hash(index, timestamp, data, previous_hash)
    blk = models.Block(index=index, timestamp=timestamp, data=data, previous_hash=previous_hash, hash=h)
    db.add(blk)
    db.commit()
    db.refresh(blk)
    return blk

def add_block(db: Session, data_obj: dict):
    """
    data_obj: dictionary to record in block (e.g., {"action":"create_student", "student":{...}})
    """
    last = get_last_block(db)
    if last is None:
        last = create_genesis_block(db)

    index = last.index + 1
    timestamp = datetime.utcnow().isoformat()
    data = json.dumps(data_obj, sort_keys=True)
    previous_hash = last.hash
    h = compute_hash(index, timestamp, data, previous_hash)
    blk = models.Block(index=index, timestamp=timestamp, data=data, previous_hash=previous_hash, hash=h)
    db.add(blk)
    db.commit()
    db.refresh(blk)
    return blk

def is_chain_valid(db: Session) -> bool:
    blocks = db.query(models.Block).order_by(models.Block.index.asc()).all()
    if not blocks:
        return True
    for i in range(1, len(blocks)):
        prev = blocks[i-1]
        cur = blocks[i]
        # check linkage
        if cur.previous_hash != prev.hash:
            return False
        # recompute hash
        recomputed = compute_hash(cur.index, cur.timestamp, cur.data, cur.previous_hash)
        if recomputed != cur.hash:
            return False
    return True
