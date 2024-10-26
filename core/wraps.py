from functools import wraps

# 初始化 DAG 結構和調用堆疊
dag_structure = []
call_stack = []


def track_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 記錄函數名稱作為節點
        node = {"name": func.__name__, "children": []}  # 內部函數將被添加為子節點

        # 如果堆疊中有父節點，將當前節點添加為子節點
        if call_stack:
            call_stack[-1]["children"].append(node)
        else:
            dag_structure.append(node)

        # 壓入堆疊並執行函數
        call_stack.append(node)
        result = func(*args, **kwargs)
        call_stack.pop()

        return result

    return wrapper
