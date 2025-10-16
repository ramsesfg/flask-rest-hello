from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    apellido: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    fecha_de_subscripcion: Mapped[str] =mapped_column(DateTime,nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
     # favorites


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
class Planeta(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped [str] = mapped_column(String(120),nullable=False)
    poblacion: Mapped [int] = mapped_column(Integer,nullable=False)
    clima: Mapped [str] = mapped_column(String(120),nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "poblacion": self.poblacion,
            "clima": self.nombre,

        }

class Personaje(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120),nullable=False)
    edad: Mapped[int] = mapped_column(Integer,nullable=False)
    raza: Mapped[str] = mapped_column(String(120),nullable=False)
    origen : Mapped[str] = mapped_column(String(120),nullable=False)
    color_de_ojos : Mapped[str] = mapped_column(String(120),nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "raza": self.raza,
            "origen": self.origen,
        }


class Favoritos (db.Model) :
    id: Mapped[int] = mapped_column(primary_key=True)

    usuario_id: Mapped[str] = mapped_column(db.ForeignKey("user.id"))
    usuario: Mapped["User"] = db.relationship(backref="favorites")

    planeta_id: Mapped[int] = mapped_column(db.ForeignKey("planeta.id"))
    planeta: Mapped["Planeta"] = db.relationship(backref="favorites")

    personaje_id: Mapped[str] = mapped_column(db.ForeignKey("personaje.id"))
    personaje: Mapped["Personaje"] = db.relationship(backref="favorites")


    