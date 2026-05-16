# Python OOP — Module 09

OOP organizes code around **objects** (data + behavior) instead of just functions. Everything in Python is an object.

---

## Quick Reference

| Concept | One-liner |
|---|---|
| Class | Blueprint for objects |
| Object | Instance of a class |
| `self` | Reference to the current instance |
| `__init__` | Auto-called constructor to set up state |
| Class attribute | Shared across all instances |
| Instance attribute | Belongs to one object only |
| Inheritance | Child reuses parent code (`is-a`) |
| Composition | Class holds another class (`has-a`) |
| `super()` | Safe way to call parent methods |
| MRO | Order Python searches for attributes/methods |
| `@staticmethod` | Utility — no `self`, no `cls` |
| `@classmethod` | Factory/alternative constructor — receives `cls` |
| `@property` | Controlled attribute access with validation |

---

## 1. Classes and Objects

A **class** is a blueprint; an **object** is the real thing built from it.

```python
class Car:
    pass

maruti = Car()
print(type(maruti))         # <class '__main__.Car'>
print(type(maruti) is Car)  # True
print(type(Car))            # <class 'type'>  ← classes are instances of 'type'
```

> 💡 **Tip:** Don't create a class just to group functions — that's what modules are for. A class earns its place when it has both **state** (attributes) and **behavior** (methods) that belong together.

📄 `09-01-simple-class.py`

---

## 2. Namespace and Class Attributes

A **namespace** maps names → objects. Class attributes live in the class namespace and are shared by all instances.

```python
class Car:
    origin = "India"    # class attribute

Car.wheels = 4          # add dynamically

maruti = Car()
print(maruti.origin)    # India  ← inherited from class
```

> 💡 **Tip:** Avoid mutable class attributes (lists, dicts) — they're shared across all instances and cause hard-to-debug bugs. Define them in `__init__` as instance attributes instead.
> ```python
> # ❌ Dangerous — all instances share the same list
> class Team:
>     members = []
>
> # ✅ Safe — each instance gets its own list
> class Team:
>     def __init__(self):
>         self.members = []
> ```

📄 `09-02-namespace.py`

---

## 3. Attribute Shadowing

Instance attributes **shadow** (hide) class attributes with the same name. Delete the instance attribute to reveal the class one again.

```python
class Bike:
    power = "350 CC"

reborn = Bike()
reborn.power = "450 CC"    # shadows class attribute
print(reborn.power)        # 450 CC
print(Bike.power)          # 350 CC  ← class unchanged

del reborn.power
print(reborn.power)        # 350 CC  ← back to class value
```

> 💡 **Tip:** Shadowing is often a sign of a design problem. If different instances need different values, those should be instance attributes from the start (set in `__init__`), not class attributes being overridden ad hoc.

📄 `09-03-attribute-shadowing.py`

---

## 4. The `self` Argument

`self` is automatically passed as the first argument to any instance method — it refers to the object calling the method.

```python
class Building:
    floor = 5

    def describe(self):
        return f"This building has {self.floor} floors."

antilla = Building()
antilla.describe()              # self = antilla (automatic)
Building.describe(antilla)      # same thing, explicit
```

📄 `09-04-self-argument.py`

---

## 5. The `__init__` Constructor

`__init__` runs automatically when an object is created. Use it to set up initial instance state.

```python
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

emp = Employee("Kalu", 25)
print(emp.name)    # Kalu
```

> 💡 **Tip:** Keep `__init__` focused on setting up state — no heavy logic, no network calls, no file I/O. If construction is complex, use a `@classmethod` factory instead (see section 10). Also consider `__post_init__` when using `@dataclass`.

📄 `09-05-init-contructor.py`

---

## 6. Inheritance vs Composition

**Inheritance** — child class extends a parent (`is-a` relationship).  
**Composition** — class holds an instance of another class (`has-a` relationship).

```python
# Inheritance
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class TwoWheeler(Vehicle):
    def __init__(self, brand, model, engine_size):
        super().__init__(brand, model)
        self.engine_size = engine_size
```

```python
# Composition
class FourWheeler:
    def __init__(self, power, color):
        self.power = power
        self.vehicle = Vehicle("Honda", "Civic")  # has-a Vehicle

civic = FourWheeler(200, "Blue")
print(civic.vehicle.brand)    # Honda
```

> Prefer composition over inheritance when the relationship isn't clearly "is-a".

> 💡 **Tip:** Deep inheritance chains (3+ levels) are a maintenance nightmare. When you catch yourself saying "but it's *almost* like the parent except...", that's composition territory. Also look into **`ABC` (Abstract Base Classes)** when you want to enforce an interface without full implementation inheritance:
> ```python
> from abc import ABC, abstractmethod
>
> class Shape(ABC):
>     @abstractmethod
>     def area(self) -> float: ...   # subclasses MUST implement this
> ```

📄 `09-06-inheritance-composition.py`

---

## 7. Calling the Base Class

Three ways to call a parent's `__init__` from a child — only one is recommended.

```python
# ❌ Don't — code duplication
class Mobile(Device):
    def __init__(self, brand, model, storage):
        self.brand = brand      # duplicated
        self.model = model      # duplicated
        self.storage = storage

# ⚠️ OK — explicit, but brittle if class name changes
class Mobile(Device):
    def __init__(self, brand, model, storage):
        Device.__init__(self, brand, model)
        self.storage = storage

# ✅ Best — use super()
class Tab(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size
```

📄 `09-07-ways-to-access-base-class.py`

---

## 8. Method Resolution Order (MRO)

MRO defines the order Python searches for a method/attribute across a class hierarchy. Uses **C3 Linearization**.

```python
class A: label = "A"
class B(A): label = "B"
class C(A): label = "C"
class D(B, C): pass        # inherits from B first, then C

print(D().label)    # B  ← B comes before C in MRO
print(D.__mro__)    # (D, B, C, A, object)
```

Order always goes: **class itself → left parent → right parent → shared base → object**

> 💡 **Tip:** If you're using multiple inheritance and MRO feels confusing, that's a design smell. Python's MRO handles mixins well — a common pattern is to use small, focused mixin classes for cross-cutting behavior (logging, serialization) rather than full multiple inheritance:
> ```python
> class LogMixin:
>     def log(self, msg): print(f"[{self.__class__.__name__}] {msg}")
>
> class JsonMixin:
>     def to_json(self): import json; return json.dumps(self.__dict__)
>
> class Order(LogMixin, JsonMixin):
>     def __init__(self, id): self.id = id
> ```

📄 `09-08-mro.py`

---

## 9. Static Methods

No `self`, no `cls` — just a plain function namespaced inside a class. Use for utility logic related to the class.

```python
class StringUtils:
    @staticmethod
    def clean(text):
        return [item.strip() for item in text.split(",")]

StringUtils.clean("A , B , C")    # ['A', 'B', 'C']
```

📄 `09-09-static-methods.py`

---

## 10. Class Methods vs Static Methods

```python
class MultiOrder:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer

    @classmethod
    def from_dict(cls, d):              # alternative constructor
        return cls(d["order_id"], d["customer"])

    @classmethod
    def from_string(cls, s):            # another constructor
        oid, name = s.split(",")
        return cls(oid.strip(), name.strip())

    @staticmethod
    def validate_id(order_id):          # utility, no class/instance needed
        return str(order_id).isdigit()
```

| | `self` | `cls` | Use case |
|---|---|---|---|
| Instance method | ✅ | ❌ | Regular behavior |
| `@classmethod` | ❌ | ✅ | Alternative constructors, factory methods |
| `@staticmethod` | ❌ | ❌ | Utility functions |

> 💡 **Tip:** If a `@staticmethod` grows large or gets reused outside the class, move it to a standalone module-level function. Static methods inside classes only make sense when they're tightly coupled to the class's concept. Also — if you find yourself writing many `@classmethod` constructors, consider `@dataclass` with `__post_init__` or a dedicated Builder pattern.

📄 `09-10-classmethods-vs-staticmethod.py`

---

## 11. Property Decorator

Turns a method into an attribute-style accessor. Lets you add validation without changing the calling code.

```python
class Product:
    def __init__(self, price):
        self._price = price         # convention: _ means "internal"

    @property
    def price(self):                # getter
        return self._price

    @price.setter
    def price(self, value):         # setter with validation
        if 1 <= value <= 100:
            self._price = value
        else:
            raise ValueError("Price must be 1–100")

p = Product(50)
print(p.price)    # 50  ← looks like attribute access, not a method call
p.price = 75      # triggers setter
p.price = 150     # raises ValueError
```

> 💡 **Tip:** Don't over-use `@property` for simple data — it adds overhead and hides what's happening. Use it when you genuinely need validation, lazy computation, or computed attributes. For modern Python (3.7+), also look at `@dataclass` with `field()` for simpler data classes, and `__slots__` when you need memory efficiency at scale:
> ```python
> # __slots__ prevents arbitrary attribute creation and reduces memory per instance
> class Point:
>     __slots__ = ('x', 'y')
>     def __init__(self, x, y):
>         self.x = x
>         self.y = y
> ```

📄 `09-11-property-decorator.py`

---

## Key Takeaways

- **Class** = blueprint. **Object** = instance. Everything in Python is an object.
- Class attributes are shared; instance attributes are per-object. Instance shadows class when names clash.
- `self` is auto-injected — it's always the calling instance.
- `__init__` sets up state. Always use `super().__init__()` in child classes.
- **Inheritance** = `is-a`. **Composition** = `has-a`. Prefer composition when in doubt.
- MRO order: left-to-right, depth-first, then shared base.
- `@staticmethod` = pure utility. `@classmethod` = factory/constructor. `@property` = controlled access.

---

## Engineer Checklist

Before shipping a class, ask yourself:

- [ ] Does this class have a single, clear responsibility? (SRP)
- [ ] Are mutable defaults (lists, dicts) in `__init__`, not at class level?
- [ ] Is `__init__` free of heavy logic, I/O, or side effects?
- [ ] Am I inheriting, or should I be composing?
- [ ] Is the inheritance chain deeper than 2 levels? If yes — reconsider.
- [ ] Would `@dataclass` make this simpler?
- [ ] Does `@property` add real value, or am I over-engineering?
- [ ] If performance matters at scale — do I need `__slots__`?
- [ ] Is the public interface clean? Are internals prefixed with `_`?