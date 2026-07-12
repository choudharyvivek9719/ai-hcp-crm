from typing import List, Optional

from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models.hcp import HCP
from app.schemas.hcp import HCPCreate


def create_hcp(db: Session, hcp: HCPCreate) -> HCP:
    """
    Create a new Healthcare Professional (HCP).
    """

    db_hcp = HCP(
        doctor_name=hcp.doctor_name,
        speciality=hcp.speciality,
        hospital=hcp.hospital,
        city=hcp.city,
        phone=hcp.phone,
    )

    db.add(db_hcp)
    db.commit()
    db.refresh(db_hcp)

    return db_hcp


def get_hcp_by_id(db: Session, hcp_id: int) -> Optional[HCP]:
    """
    Get HCP by ID.
    """

    return (
        db.query(HCP)
        .filter(HCP.id == hcp_id)
        .first()
    )


def get_hcp_by_name(db: Session, doctor_name: str) -> Optional[HCP]:
    """
    Get HCP by doctor name.
    """

    return (
        db.query(HCP)
        .filter(HCP.doctor_name.ilike(f"%{doctor_name}%"))
        .first()
    )


def get_all_hcps(
    db: Session,
    skip: int = 0,
    limit: int = 100,
) -> List[HCP]:
    """
    Return all HCPs.
    """

    return (
        db.query(HCP)
        .offset(skip)
        .limit(limit)
        .all()
    )


def search_hcps(
    db: Session,
    doctor_name: str = "",
    speciality: str = "",
    hospital: str = "",
    city: str = "",
) -> List[HCP]:
    """
    Search HCPs using optional filters.
    """

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


def search_hcp_keyword(
    db: Session,
    keyword: str,
) -> List[HCP]:
    """
    Global keyword search across multiple columns.
    """

    return (
        db.query(HCP)
        .filter(
            or_(
                HCP.doctor_name.ilike(f"%{keyword}%"),
                HCP.speciality.ilike(f"%{keyword}%"),
                HCP.hospital.ilike(f"%{keyword}%"),
                HCP.city.ilike(f"%{keyword}%"),
            )
        )
        .all()
    )


def update_hcp(
    db: Session,
    hcp_id: int,
    updated_data: dict,
) -> Optional[HCP]:
    """
    Update HCP details.
    """

    hcp = (
        db.query(HCP)
        .filter(HCP.id == hcp_id)
        .first()
    )

    if not hcp:
        return None

    for key, value in updated_data.items():
        if hasattr(hcp, key):
            setattr(hcp, key, value)

    db.commit()
    db.refresh(hcp)

    return hcp


def delete_hcp(
    db: Session,
    hcp_id: int,
) -> bool:
    """
    Delete an HCP.
    """

    hcp = (
        db.query(HCP)
        .filter(HCP.id == hcp_id)
        .first()
    )

    if not hcp:
        return False

    db.delete(hcp)
    db.commit()

    return True


def hcp_exists(
    db: Session,
    doctor_name: str,
    hospital: str,
) -> bool:
    """
    Check whether an HCP already exists.
    """

    hcp = (
        db.query(HCP)
        .filter(
            HCP.doctor_name == doctor_name,
            HCP.hospital == hospital,
        )
        .first()
    )

    return hcp is not None


def get_hcps_by_speciality(
    db: Session,
    speciality: str,
) -> List[HCP]:
    """
    Return all HCPs belonging to a speciality.
    """

    return (
        db.query(HCP)
        .filter(
            HCP.speciality.ilike(f"%{speciality}%")
        )
        .all()
    )


def get_hcps_by_city(
    db: Session,
    city: str,
) -> List[HCP]:
    """
    Return HCPs from a city.
    """

    return (
        db.query(HCP)
        .filter(
            HCP.city.ilike(f"%{city}%")
        )
        .all()
    )
