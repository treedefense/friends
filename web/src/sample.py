from fastapi import APIRouter

router = APIRouter()


@router.get("/sample")
def echo_sample():
    return "sample"
