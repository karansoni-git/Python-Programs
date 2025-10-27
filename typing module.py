'''
=> The typing module in Python provides type hints that help you specify the expected data types of variables, function arguments, and return values.

=> It was introduced in Python 3.5 (with improvements in later versions) to support static type checking, making code more readable, maintainable, and easier to debug.

=> common types in typing module
| Type                                 | Usage                                   |
| ------------------------------------ | --------------------------------------- |
| `Any`                                | Any type is allowed                     |
| `List[type]`                         | List of specific type, e.g. `List[int]` |
| `Tuple[type1, type2]`                | Fixed-length tuple with specific types  |
| `Dict[key_type, value_type]`         | Dictionary with key-value types         |
| `Set[type]`                          | Set of specific type                    |
| `Optional[type]`                     | Either `type` or `None`                 |
| `Union[type1, type2]`                | Either `type1` or `type2`               |
| `Callable[[arg_types], return_type]` | Function signature                      |
| `Literal[value1, value2]`            | Specific literal values                 |
| `TypeVar`                            | Generic type variable                   |
| `Generic`                            | For creating generic classes            |
| `Final`                              | Marks a variable as constant            |
| `TypedDict`                          | Dict with fixed keys and value types    |
'''

from typing import List, Dict, Tuple, Union, Optional, Callable

# 1. List of integers
numbers : List[int] = [10,20,30,40]
print(numbers)

# 2. Dictionary with str keys & int values
details : Dict[str,int] = {"karan":20,"krish":21,"dhruvil":18}
print(details)

# 3. Union: accepts int or str
values : Union[int,str] = "sample"
print(values)
