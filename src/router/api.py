from fastapi import APIRouter

from services.gen_character.anl_txt import anl_env_relation

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Hello, World!"}

@router.get("/gen-character")
def gen_character(text: str):
    anl_env_relation(text)
    # return anl_txt(text)
