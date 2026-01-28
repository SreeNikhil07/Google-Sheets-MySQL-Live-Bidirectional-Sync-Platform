from app.sync_engine import should_apply
from datetime import datetime

print(should_apply("123", "SHEET", datetime.utcnow()))
print(should_apply("123", "MYSQL", datetime.utcnow()))
