from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.hcp import HCP
from app.schemas.hcp import HCPCreate, HCPResponse

router = APIRouter(
    prefix="/hcp",
    tags=["Healthcare Professionals (HCP)"]
)


# ---------------------------------------------------
# Create HCP
# ---------------------------------------------------
@router.post(
    "/",
    response_model=HCPResponse,
    status_code=status.HTTP_201_CREATED
)
def create_hcp(
    hcp: HCPCreate,
    db: Session = Depends(get_db)
):

    existing_hcp = (
        db.query(HCP)
        .filter(HCP.doctor_name == hcp.doctor_name)
        .first()
    )

    if existing_hcp:
        raise HTTPException(
            status_code=400,
            detail="HCP already exists."
        )

    new_hcp = HCP(
        doctor_name=hcp.doctor_name,
        speciality=hcp.speciality,
        hospital=hcp.hospital,
        city=hcp.city,
        phone=hcp.phone
    )

    db.add(new_hcp)
    db.commit()
    db.refresh(new_hcp)

    return new_hcp


# ---------------------------------------------------
# Get All HCPs
# ---------------------------------------------------
@router.get(
    "/",
    response_model=List[HCPResponse]
)
def get_all_hcps(
    db: Session = Depends(get_db)
):

    return db.query(HCP).all()


# ---------------------------------------------------
# Get HCP By ID
# ---------------------------------------------------
@router.get(
    "/{hcp_id}",
    response_model=HCPResponse
)
def get_hcp(
    hcp_id: int,
    db: Session = Depends(get_db)
):

    hcp = (
        db.query(HCP)
        .filter(HCP.id == hcp_id)
        .first()
    )

    if not hcp:
        raise HTTPException(
            status_code=404,
            detail="HCP not found."
        )

    return hcp


# ---------------------------------------------------
# Search HCP
# ---------------------------------------------------
@router.get("/search/")
def search_hcp(
    doctor_name: Optional[str] = Query(None),
    speciality: Optional[str] = Query(None),
    hospital: Optional[str] = Query(None),
    city: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):

    query = db.query(HCP)

    if doctor_name:
        query = query.filter(
            HCP.doctor_name.ilike(f"%{doctor_name}%")
        )

    if speciality:
        query = query.filter(
            HCP.speciality.ilike(f"%{speciality}%")
        )

    if hospital:
        query = query.filter(
            HCP.hospital.ilike(f"%{hospital}%")
        )

    if city:
        query = query.filter(
            HCP.city.ilike(f"%{city}%")
        )

    return query.all()


# ---------------------------------------------------
# Update HCP
# ---------------------------------------------------
@router.put(
    "/{hcp_id}",
    response_model=HCPResponse
)
def update_hcp(
    hcp_id: int,
    updated_hcp: HCPCreate,
    db: Session = Depends(get_db)
):

    hcp = (
        db.query(HCP)
        .filter(HCP.id == hcp_id)
        .first()
    )

    if not hcp:
        raise HTTPException(
            status_code=404,
            detail="HCP not found."
        )

    hcp.doctor_name = updated_hcp.doctor_name
    hcp.speciality = updated_hcp.speciality
    hcp.hospital = updated_hcp.hospital
    hcp.city = updated_hcp.city
    hcp.phone = updated_hcp.phone

    db.commit()
    db.refresh(hcp)

    return hcp


# ---------------------------------------------------
# Delete HCP
# ---------------------------------------------------
@router.delete("/{hcp_id}")
def delete_hcp(
    hcp_id: int,
    db: Session = Depends(get_db)
):

    hcp = (
        db.query(HCP)
        .filter(HCP.id == hcp_id)
        .first()
    )

    if not hcp:
        raise HTTPException(
            status_code=404,
            detail="HCP not found."
        )

    db.delete(hcp)
    db.commit()

    return {
        "message": "HCP deleted successfully."
    }
