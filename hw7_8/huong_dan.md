## Run thử để kiểm tra API

### 1. Chạy server

```bash
python main.py
```

Hoặc:

```bash
uvicorn main:app --reload
```

---

### 2. Gửi request

#### Cách 1: Chạy lệnh trong terminal (Git Bash)

```bash
curl -X POST "http://localhost:8000/products/available" \
-H "Content-Type: application/json" \
-d '{
    "products": [
        {"id": 1, "name": "Áo thun", "stock": 10, "is_active": true},
        {"id": 2, "name": "Quần jeans", "stock": 0, "is_active": true},
        {"id": 3, "name": "Giày thể thao", "stock": 5, "is_active": false}
    ]
}'
```

> Lưu ý: Trong JSON phải dùng `true/false` thay vì `True/False`.

#### Kết quả trả về

```json
{
    "products": [
        {
            "id": 1,
            "name": "Áo thun",
            "stock": 10,
            "is_active": true
        }
    ]
}
```

---

#### Cách 2: Sử dụng API Docs của FastAPI

- Mở trình duyệt và truy cập:

```bash
http://localhost:8000/docs
```

- Tìm endpoint:

```bash
POST /products/available
```

- Nhấn **Try it out**
- Dán payload JSON vào ô **Request body**
- Nhấn **Execute** để gửi request và xem kết quả