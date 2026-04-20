from jose import jwt
from datetime import datetime

# REPLACE THIS WITH YOUR NEW TOKEN
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0Iiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNzc2NjczNDQyfQ.LTHyjj1fvCA5IN8NMYe6ab5zWvT4y_5FCwiur00HOuI"

print("=" * 60)
print("TOKEN ANALYSIS")
print("=" * 60)

# Check if token has 3 parts
parts = token.split('.')
print(f"\nToken parts: {len(parts)} (should be 3)")

if len(parts) != 3:
    print("❌ Invalid token format! Token should have 3 parts separated by dots")
    print(f"   Got {len(parts)} parts instead")
else:
    # Decode without verification
    try:
        payload = jwt.decode(token, None, options={"verify_signature": False})
        print("\n✅ Token decoded successfully!")
        print(f"   User ID: {payload.get('sub')}")
        print(f"   Role: {payload.get('role')}")
        
        exp_timestamp = payload.get('exp')
        if exp_timestamp:
            exp_date = datetime.fromtimestamp(exp_timestamp)
            now = datetime.now()
            print(f"   Expires: {exp_date}")
            print(f"   Current: {now}")
            
            if now.timestamp() > exp_timestamp:
                print("\n   ❌ Token is EXPIRED")
            else:
                print("\n   ✅ Token is VALID")
                minutes_left = (exp_date - now).total_seconds() / 60
                print(f"   Time left: {minutes_left:.0f} minutes")
    except Exception as e:
        print(f"\n❌ Error: {e}")