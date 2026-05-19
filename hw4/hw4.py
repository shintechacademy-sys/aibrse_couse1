# Bai 1:
class BrowserHistory:
    def __init__(self, homepage):
        self.current = homepage
        self.backward_stack = []
        self.forward_stack = []

    def visit(self, url):
        self.backward_stack.append(self.current)
        self.current = url
        self.forward_stack.clear()

    def back(self, steps):
        for i in range(steps):
            self.forward_stack.append(self.current)
            if self.backward_stack:
                self.current = self.backward_stack.pop()

        return self.current

    def forward(self, steps):
        for i in range(steps):
            self.backward_stack.append(self.current)
            if self.forward_stack:
                self.current = self.forward_stack.pop()
        return self.current

h = BrowserHistory("trang-chu")
h.visit("san-pham/ao-thun")
h.visit("san-pham/quan-jean")
h.visit("gio-hang")
print(h.back(1))
print(h.back(1))
print(h.forward(1))
print(h.back(3))


# Bai 2:
def is_valid_brackets(s):
  stack = []
  # sử dụng dictionary ngoặc mở tương ứng với ngoặc đóng
  mapping = {
      ')': '(',
      ']': '[',
      '}': '{'
  }
  for char in s:
      if char in mapping.values():  # ngoặc mở
          stack.append(char)
      elif char in mapping:  # ngoặc đóng
          if not stack or stack[-1] != mapping[char]:
              return False
          stack.pop()

  return len(stack) == 0
        

print(is_valid_brackets('{"name": "An", "items": [1, 2]}')) # True 
print(is_valid_brackets('{"data": [{"id": 1}'))             # False   
print(is_valid_brackets('(())'))                            # True 
print(is_valid_brackets('{"data": [{"id": 1]}'))            # False 


# Bai 3: 
from collections import defaultdict  # Có thể ko dùng defaultdict từ thư viện collections

def validate_transaction_order(events):
  # gom events theo txn_id theo đúng thứ tự xuất hiện
  txns = defaultdict(list)
  for e in events:
    txns[e["txn_id"]].append(e["event"])

  errors = []
  completed = 0
  valid = True

  for txn_id, evs in txns.items():
    state = "NONE"
    has_processing = False

    for ev in evs:
      if state == "NONE":
        if ev == "INIT":
          state = "INIT"
        else:
          valid = False
          errors.append(f"{txn_id}: sai luong bat dau (thieu INIT)")
          break

      elif state == "INIT":
        if ev == "PROCESSING":
          state = "PROCESSING"
          has_processing = True
        else:
          valid = False
          errors.append(f"{txn_id}: thieu buoc PROCESSING")
          break

      elif state == "PROCESSING":
        if ev in ("COMPLETED", "FAILED"):
          state = ev
        else:
          valid = False
          errors.append(f"{txn_id}: trang thai khong hop le sau PROCESSING")
          break

    else:
      # chỉ tính completed nếu flow hợp lệ
      if state in ("COMPLETED", "FAILED") and has_processing:
        completed += 1

  return {
    "valid": len(errors) == 0,
    "completed": completed,
    "errors": errors
  }


# Test
events1 = [
 {"txn_id": "T1", "event": "INIT"},
 {"txn_id": "T2", "event": "INIT"},
 {"txn_id": "T2", "event": "PROCESSING"},
 {"txn_id": "T2", "event": "COMPLETED"},
 {"txn_id": "T1", "event": "PROCESSING"},
 {"txn_id": "T1", "event": "FAILED"},
]

events2 = [
 {"txn_id": "T3", "event": "INIT"},
 {"txn_id": "T3", "event": "COMPLETED"},
]

print(validate_transaction_order(events1))
print(validate_transaction_order(events2))

# Bai 4
import heapq
from itertools import count

class PriorityShippingQueue:
  def __init__(self):
    self.heap = []
    self.counter = count()  # đảm bảo FIFO trong cùng priority
    self.priority_map = {
      "express": 1,
      "vip": 2,
      "normal": 3
    }

  def enqueue(self, item):
    priority = self.priority_map[item["type"]]
    order = next(self.counter)

    # heap: (priority, order, item)
    heapq.heappush(self.heap, (priority, order, item))

  def dequeue(self):
    if not self.heap:
      return None
    _, _, item = heapq.heappop(self.heap)
    return item

# Test
psq = PriorityShippingQueue()

psq.enqueue({"id": "S1", "type": "normal",  "dest": "HN"})
psq.enqueue({"id": "S2", "type": "express", "dest": "HCM"})
psq.enqueue({"id": "S3", "type": "vip",     "dest": "DN"})
psq.enqueue({"id": "S4", "type": "express", "dest": "HN"})

print(psq.dequeue())
print(psq.dequeue())
print(psq.dequeue())

# Bai 5:
def simulate_checkout(customers, n_counters):
    # Khởi tạo các quầy
    counters = {
        f"counter_{i+1}": {
            "customers": [],
            "total_items": 0
        }
        for i in range(n_counters)
    }

    for customer in customers:
        # Chọn quầy có total_items nhỏ nhất
        best_counter = min(
            counters,
            key=lambda c: counters[c]["total_items"]
        )

        counters[best_counter]["customers"].append(customer["id"])
        counters[best_counter]["total_items"] += customer["items"]

    return counters


# Test
customers = [
    {"id": "C1", "items": 5},
    {"id": "C2", "items": 12},
    {"id": "C3", "items": 3},
    {"id": "C4", "items": 8},
    {"id": "C5", "items": 1},
]

result = simulate_checkout(customers, n_counters=2)
print(result)

# Ket qua dung: {'counter_1': {'customers': ['C1', 'C3', 'C4'], 'total_items': 16}, 'counter_2': {'customers': ['C2', 'C5'], 'total_items': 13}}
# -> Vì xếp hàng vào luôn chọn hàng đang có items nhỏ nhất

# Dù C1 + C4 + C5 = 5+8+1 = 14, C2+C3 = 15 nhưng phải reorder mới sắp xếp được như vậy -> ko đúng với mô phỏng hàng thực tế