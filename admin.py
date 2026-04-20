# create_admin.py
from app.database import SessionLocal
from app.models import User
from app.auth import get_password_hash

def create_admin():
    db = SessionLocal()
    
    # Check if admin already exists
    existing_admin = db.query(User).filter(User.email == "admin@gmail.com").first()
    
    if existing_admin:
        print(f"Admin user already exists!")
        print(f"Email: {existing_admin.email}")
        print(f"Role: {existing_admin.role}")
    else:
        # Create new admin
        admin = User(
            first_name="Admin",
            last_name="7",
            email="admin@gmail.com",
            hashed_password=get_password_hash("Password5"),
            role="admin",
            is_active=True
        )
        
        db.add(admin)
        db.commit()
        db.refresh(admin)
        
        print("✓ Admin user created successfully!")
        print(f"   Email: admin@gmail.com")
        print(f"   Password: Password5")
        print(f"   Role: admin")
        print(f"   ID: {admin.id}")
    
    db.close()

if __name__ == "__main__":
    create_admin()