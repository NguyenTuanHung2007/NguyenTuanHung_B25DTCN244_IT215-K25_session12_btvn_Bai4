from pydantic import BaseModel

class StudentInfo(BaseModel):
    id: int
    full_name: str
    email: str

    class Config:
        from_attributes = True

class DeleteSuccessResponse(BaseModel):
    message: str
    data: StudentInfo