from attrs import define, field
from litestar import Litestar, get, post, put
from litestar.exceptions import NotFoundException


@define(kw_only=True)
class TodoItem:
    title: str
    done: bool

@define
class TodoList:
    items: list[TodoItem] = field(factory=list)

td = TodoList()
td.items.append(TodoItem(title="Start writing TODO list", done=True))
td.items.append(TodoItem(title="???", done=False))
td.items.append(TodoItem(title="Profit", done=False))

def get_todo_by_title(todo_name) -> TodoItem:
    for item in td.items:
        if item.title == todo_name:
            return item
    raise NotFoundException(detail=f"Item {todo_name} not found")

@get("/")
async def get_list(done: bool | None = None) -> list[TodoItem]:
    return [item for item in td.items if item.done is done]

@post("/data_insert")
async def add_item(data: TodoItem) -> list[TodoItem]:
    td.items.append(data)
    return td.items

@put("/{item_title:str}")
async def update_item(
        item_title: str,
        data: TodoItem
) -> list[TodoItem]:
    todo_item = get_todo_by_title(item_title)
    todo_item.title = data.title
    todo_item.done = data.done
    return td.items

app = Litestar([get_list, add_item, update_item])