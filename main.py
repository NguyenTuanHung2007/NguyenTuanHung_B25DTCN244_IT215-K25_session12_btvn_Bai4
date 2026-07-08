from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db, engine
import models
import schemas
import user_service

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.delete("/students/{student_id}", response_model=schemas.DeleteSuccessResponse)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    deleted_student_info = user_service.delete_student_service(db, student_id)
    
    return {
        "message": "Xóa học viên thành công",
        "data": deleted_student_info
    }