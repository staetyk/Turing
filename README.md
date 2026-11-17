# Turing
A Turing machine class.\
Class definition in [`turing.py`](/turing.py).



### `Turing(*states: StateType, alphabet: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_", tape: List[int] | str = [-1], pos: int = 0, shorten: bool = False) -> Turing`
Initializes the Turing object.
* `*states` - Each state of the Turing machine. In the format `(case0, case1, ..., caseBlank)`. Each case is in the format `(nextState, setValue, direction)`. In the `caseBlank`, `setValue` can be `-1` for blank.
* `alphabet` - The character to use for representing each cell value. The last character is for blank cells. The rest are in order (the first is for `0` cells, the second is for `1` cells, etc.). If there are excess characters, all but the first `n-1` characters and the last character are discarded, where `n` is the number of possible cell values.
* `tape` - Initial tape. In the format of a list of values (`True`, `False`, or `None`), or in the format of a string. Any character not in `alphabet` is ignored. Default `[None]`.
* `pos` - Initial position. Default `0`.
* `shorten` - Whether or not to strip excess blank cells automatically. Default `False`.



## Attributes

### `Turing.StateType`
`type Tuple[Tuple[int, int, int], ...]`

Type for the instructions associated with a state of the Turing machine.

### `object.states`
`Dict[int, StateType | None]`

Dictionary containing the instructions associated with each state of the Turing machine.

### `object.nums`
`int`

Number of different possible cell values.

### `object.alpha`
`str`

Characters to use when representing each cell value.

### `object.tape`
`List[int]`

Current memory tape.

### `object.pos`
`int`

Current position on tape.

### `object.phase`
`int`

Current state. `-1` for Halt.

### `object.shorten`
`bool`

Whether to automatically strip excess blank cells.

### `object.count`
`int`

Number of steps that have passed.



## Methods

### `Turing.beavers(n: int, _m: int = -1, _first: bool = True) -> List[Turing]`
Returns a comprehensive list of Turing machines of size n and an alphabet length of 2.
* `n` - The number of non-Halt states each Turing machine should have.

### `Turing.BB(n: int, checkUntil: int = 100) -> int`
Finds the maximum running length of halting Turing machines of size `n` and an alphabet length of `2`. If a Turing machine does not halt within `checkUntil` steps, it is considered non-halting. If none of the Turing machines halt, returns `-1`.
* `n` - The number of non-Halt states the considered Turing machines should have.
* `checkUntil` - The maximum number of steps to check before declaring the Turing machine non-halting. Default `100`.

### `object.copy() -> Turing`
Returns a copy of the Turing machine.

### `object.keys() -> collections.abc.KeysView[int]`
### `object.values() -> collections.abc.ValuesView[StateType | None]`
### `objects.items() -> collections.abc.ItemsView[int, StateType | None]`
Returns a dictionary keys, values, or items view object of `object.states`, respectively.

### `object.strip() -> None`
Strips any excess blank cells from the tape.

### `object.halting(checkUntil: int = 100) -> int`
Checks how many steps the Turing machine will take to halt. If it doesn't halt within `checkUntil` steps, returns `-1`.
* `checkUntil` - The maximum number of steps to check before declaring the Turing machine non-halting. Default `100`.



## Other Functionality

### `next(object)`
### `object() -> Turing`
Progresses the Turing machine by one step.

### `object[key]`
Returns value of the specified state.

### `str(object)`
Returns the current tape as a string.

### `n in object`
Returns whether the Turing Machine includes a state with the index `n`.

### `bool(object)`
Returns whether the Turing machine has halted. `True` if it has, `False` if it hasn't.

### `int(object)`
Returns the current running time of the Turing machine in steps.

### `len(object)`
Returns the number of states the Turing machine has.

### `object.__repr__()`
Returns the current tape as a string. The cell the Turing machine is currently on is put in parentheses (`()`).

### `iter(object)`
Returns the current tape as an iterator.

### `object == other`
### `object != other`
### `object > other`
### `object >= other`
### `object < other`
### `object <= other`
Compares based on running time in steps. If compared to another Turing machine, if only one of them is halted, then the halted one is considered greater.
