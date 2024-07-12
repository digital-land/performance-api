from typing import List

from sqlalchemy import ForeignKey, Integer, Column
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Organisation(Base):
    __tablename__ = "organisations"
    id = Column(String(100), primary_key=True)
    name = Column(String(100))
    dataset_active_count = Column(Integer)
    dataset_warning_count = Column(Integer)
    dataset_error_count = Column(Integer)

    datasets = relationship("Dataset", back_populates="organisation", uselist=True, lazy="noload")

    def __repr__(self) -> str:
        return f"Organisation(id={self.id!r}, name={self.name!r})"


class Dataset(Base):
    __tablename__ = "datasets"
    # id = Column(Integer, primary_key=True)
    organisation_id = Column(String(100), ForeignKey("organisations.id"), primary_key=True)
    dataset = Column(String(100), primary_key=True)
    record_count = Column(Integer)
    warning_count = Column(Integer)
    error_count = Column(Integer)

    organisation = relationship(
        "Organisation", uselist=False, back_populates="datasets", lazy="joined"
    )

    def __repr__(self) -> str:
        return (f"Dataset(organisation_id={self.organisation_id!r}, dataset={self.dataset!r},"
                f" record_count={self.record_count!r}, warning_count={self.warning_count!r},"
                f" error_count={self.error_count!r})")



# class Response(Base):
#     __tablename__ = "response"
#
#     id = Column(Integer, primary_key=True)
#     request_id = Column(String, ForeignKey("request.id"), index=True)
#     data = Column(JSONB)
#     error = Column(JSONB)
#
#     request = relationship("Request", back_populates="response")
#     details = relationship(
#         "ResponseDetails", back_populates="response", uselist=True, lazy="noload"
#     )
#
# class ResponseDetails(Base):
#     __tablename__ = "response_details"
#
#     id = Column(Integer, primary_key=True)
#     response_id = Column(Integer, ForeignKey("response.id"), index=True)
#     detail = Column(JSONB)
#
#     response = relationship("Response", back_populates="details")
