# Turing
A Turing machine.

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
