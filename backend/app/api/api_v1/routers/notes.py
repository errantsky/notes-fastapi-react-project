from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session

from datetime import datetime

from app.db.session import get_db
from app.db.crud import (
    get_note,
    create_note,
    edit_note,
    delete_note,
)
from app.db.schemas import NoteEdit, NoteCreate, Note, User
from app.core.auth import get_current_acitve_user

notes_router = APIRouter()


@notes_router.get('/notes/{note_id}', response_model=Note)
async def note_detail(request: Request, note_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_acitve_user)):
    note = get_note(db, note_id)
    if note.owner_id == current_user.id:
        return note
    else:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Only the owner can access the note.")


@notes_router.post('/notes', response_model=Note)
async def note_create(request: Request, note: NoteCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_acitve_user)):
