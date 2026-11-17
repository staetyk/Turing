import collections



class Turing():
    """A Turing machine.
    ﻿\t- Turing.StateType: Type for the instructions associated with a state of the Turing machine.
    ﻿\t- self.states: Dictionary containing the instructions associated with each state of the Turing machine.
    ﻿\t- self.nums: Number of different possible cell values.
    ﻿\t- self.alpha: Characters to use when representing each cell value.
    ﻿\t- self.tape: Current memory tape.
    ﻿\t- self.pos: Current position on tape.
    ﻿\t- self.phase: Current state.
    ﻿\t- self.shorten: Whether to automatically strip excess blank cells.
    ﻿\t- self.count: Number of steps that have passed."""
    
    # Type for the instructions associated with a state of the Turing machine.
    type StateType = Tuple[Tuple[int, int, int], ...]
    
    def __init__(self, *states: StateType, alphabet: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_", tape: List[int] | str = [-1], pos: int = 0, shorten: bool = False) -> None:
        """A Turing machine.
        ﻿\t- *states: Each state of the Turing machine. In the format '(case0, case1, ..., caseBlank)'. Each case is in the format '(nextState, setValue, direction)'. In the caseBlank, setValue can be -1 for blank.
        ﻿\t- alphabet: The character to use for representing each cell value. The last character is for blank cells. The rest are in order (the first is for 0 cells, the second is for 1 cells, etc.). If there are excess characters, all but the first n-1 characters and the last character are discarded, where n is the number of possible cell values.
        ﻿\t- tape: Initial tape. In the format of a list of values (True, False, or None), or in the format of a string ("1" for True, "0" for False, {blank} for None, any other character is ignored). Default [None].
        ﻿\t- pos: Initial position. Default 0.
        ﻿\t- shorten: Whether or not to strip excess blank cells automatically. Default False."""
        
        # Number of different possible cell values.
        self.nums = len(states[0])
        try: assert len(alphabet) >= self.nums
        except: raise Exception("Not a long enough alphabet.")
        
        # Dictionary containing the instructions associated with each state of the Turing machine.
        self.states: Dict[int, StateType | None] = {-1 : None}
        for i, x in enumerate(states):
            try: assert len(x) == self.nums
            except:
                if len(x) > self.nums: raise Exception(f"State {i} has too many cases.")
                else: raise Exception(f"State {i} does not have enough cases.")
            for j, y in enumerate(x):
                try: assert -1 <= y[0] < len(states)
                except: raise Exception(f"State {i} case {j} has an invalid newState.")
            self.states.update({i : x})
        
        # Characters to use when representing each cell value.
        self.alpha: str = alphabet[:self.nums - 1] + alphabet[-1]
        
        if isinstance(tape, list):
            # Current memory tape.
            self.tape: List[int] = tape.copy()
        else:
            tapeL = []
            for x in tape:
                if x == self.alpha[-1]: tapeL.append(-1)
                elif x in self.alpha: tapeL.append(self.alpha.find(x))
            self.tape: List[int] = tapeL
        # Current position on tape.
        self.pos: int = pos
        # Current state.
        self.phase: int = 0
        
        # Whether to automatically strip excess blank cells.
        self.shorten: bool = shorten
        # Number of steps that have passed.
        self.count: int = 0
        
        
    def __next__(self) -> 'Turing':
        """Progresses the Turing machine by one step."""
        
        if not(self):
            self.count += 1
            cell = self.tape[self.pos]
            newPhase, newVal, direction = self.states[self.phase][cell]
            self.tape[self.pos] = newVal
            self.phase = newPhase
            if not(direction):
                if self.pos == 0:
                    self.tape.insert(0, -1)
                else:
                    self.pos -= 1
            else:
                self.pos += 1
                if self.pos == len(self.tape):
                    self.tape.append(-1)
        if self.shorten: self.strip()
        return self
    
    
    def __call__(self) -> 'Turing':
        """Progresses the Turing machine by one step."""
        
        return next(self)
                
    
    def __getitem__(self, key: int) -> StateType | None:
        """Returns value of the specified state."""
        
        return self.states[key]
    
    
    def __str__(self) -> str:
        """Returns the current tape as a string."""
        
        out = ""
        for i, x in enumerate(self.tape):
            cell = self.alpha[x]
            if i == self.pos:
                # out += f"\u001b[4m{int(x)}\u001b[24m"
                out += f"({cell})"
            else:
                out += cell
        return out
    
    
    def copy(self) -> 'Turing':
        """Returns a copy of self."""
        
        nonH = self.states.copy()
        nonH.pop(-1)
        statesT = (x for x in nonH.values())
        new = Turing(*statesT, alphabet = self.alpha, tape = self.tape, pos = self.pos, shorten = self.shorten)
        new.phase = self.phase
        new.count = self.count
        return new
    
    
    def keys(self) -> collections.abc.KeysView[int]:
        """Returns a dictionary keys view object of self.states."""
        
        return self.states.keys()
    
    
    def values(self) -> collections.abc.ValuesView[StateType | None]:
        """Returns a dictionary values view object of self.states."""
        
        return self.states.values()
    
    
    def items(self) -> collections.abc.ItemsView[int, StateView | None]:
        """Returns a dictionary items view object of self.states."""
        
        return self.states.items()
    
    
    def __contains__(self, index: int) -> bool:
        """Returns whether the Turing Machine includes a state with the given index.
        ﻿\t- index: The supposed index of a state in the Turing machine."""
        
        return index in self.states
    
    
    def __bool__(self) -> bool:
        """Returns whether the Turing machine has halted. True if it has, False if it hasn't."""
        
        return self.phase == -1
    
    
    def __int__(self) -> int:
        """Returns the current running time of the Turing machine in steps."""
        
        return self.count
    
        
    def __len__(self) -> int:
        """Returns the number of states the Turing machine has."""
        
        return len(self.states) - 1
    
    
    def __repr__(self) -> str:
        """Returns the current tape as a string. The cell the Turing machine is currently on is put in parentheses ('()')."""
        
        out = ""
        for i, x in enumerate(self.tape):
            cell = self.alpha[x]
            if i == self.pos:
                # out += f"\u001b[4m{int(x)}\u001b[24m"
                out += f"({cell})"
            else:
                out += cell
        return out
    
    
    def __iter__(self) -> iter:
        """Returns the current tape as an iterator."""
        
        return iter(self.tape)
    
    
    def strip(self) -> None:
        """Strips any excess blank cells from the tape."""
        
        for _ in range(self.pos):
            if self.tape[0] != -1:
                break
            else:
                self.tape.pop(0)
                self.pos -= 1
        for _ in range(len(self.tape) - 1, self.pos, -1):
            if self.tape[-1] != -1:
                break
            else:
                self.tape.pop()
                
        
    def __lt__(self, other: 'Turing' | float) -> bool:
        """Compares based on running time in steps. If compared to another Turing machine, if only one of them is halted, then the halted one is considered greater.
        ﻿\t- other: The object the Turing machine is being compared to."""
        
        if type(other) == 'Turing':
            if self ^ other:
                return bool(other)
            else:
                return int(self) < int(other)
        else:
            return int(self) < other
            
        
    def __le__(self, other: 'Turing' | float) -> bool:
        """Compares based on running time in steps. If compared to another Turing machine, if only one of them is halted, then the halted one is considered greater.
        ﻿\t- other: The object the Turing machine is being compared to."""
        
        if type(other) == 'Turing':
            if not(self) and other:
                return False
            else:
                return int(self) <= int(other)
        else:
            return int(self) <= other
            
        
    def __eq__(self, other: 'Turing' | float) -> bool:
        """Compares based on running time in steps. If compared to another Turing machine, if only one of them is halted, then the halted one is considered greater.
        ﻿\t- other: The object the Turing machine is being compared to."""
        
        if type(other) == 'Turing':
            if self ^ other:
                return False
            else:
                return int(self) == int(other)
        else:
            return int(self) == other


    def __ne__(self, other: 'Turing' | float) -> bool:
        """Compares based on running time in steps. If compared to another Turing machine, if only one of them is halted, then the halted one is considered greater.
        ﻿\t- other: The object the Turing machine is being compared to."""
        
        if type(other) == 'Turing':
            if self ^ other:
                return True
            else:
                return int(self) != int(other)
        else:
            return int(self) != other


    def __gt__(self, other: 'Turing' | float) -> bool:
        """Compares based on running time in steps. If compared to another Turing machine, if only one of them is halted, then the halted one is considered greater.
        ﻿\t- other: The object the Turing machine is being compared to."""
        
        if type(other) == 'Turing':
            if self ^ other:
                return bool(self)
            else:
                return int(self) > int(other)
        else:
            return int(self) > other


    def __ge__(self, other: 'Turing' | float) -> bool:
        """Compares based on running time in steps. If compared to another Turing machine, if only one of them is halted, then the halted one is considered greater.
        ﻿\t- other: The object the Turing machine is being compared to."""
        
        if type(other) == 'Turing':
            if self and not(other):
                return False
            else:
                return int(self) >= int(other)
        else:
            return int(self) >= other


    def halting(self, checkUntil: int = 100) -> int:
        """Checks how many steps the Turing machine will take to halt. If it doesn't halt within checkUntil steps, returns -1.
        ﻿\t- checkUntil: The maximum number of steps to check before declaring the Turing machine non-halting. Default 100."""

        try: assert checkUntil >= 1
        except: raise Exception("checkUntil msut be positive.")
        x = self.copy()
        for i in range(0, checkUntil + 1):
            if x: return i
            next(x)
        if x: return checkUntil
        else: return -1
        
        
    @staticmethod
    def beavers(n: int, _m: int = -1, _first: bool = True) -> List['Turing']:
        """Returns a comprehensive list of Turing machines of size n and an alphabet length of 2.
        ﻿\t- n: The number of non-Halt states each Turing machine should have."""

        try: assert n >= 1
        except: raise Exception("n must be positive.")
        if _m == -1: _m = n
        assert _m >= n
        if n == 1:
            sub = []
            for i in range(-1, _m):
                for j in [0, -1]:
                    for k in [0, -1]:
                        sub.append((i, j, k))
            states = []
            for x in sub:
                for y in sub:
                    states.append([(x, y)])
        else:
            states = []
            for x in Turing.beavers(n - 1, _m, _first = False):
                for y in Turing.beavers(1, _m, _first = False):
                    states.append(x + y)
        if _first:
            out = []
            for x in states:
                out.append(Turing(*tuple(x), alphabet = "10"))
            return out
        else:
            return states
    
    
    @staticmethod
    def BB(n: int, checkUntil: int = 100) -> int:
        """Finds the maximum running length of halting Turing machines of size n and an alphabet length of 2. If a Turing machine does not halt within checkUntil steps, it is considered non-halting. If none of the Turing machines halt, returns -1.
        ﻿\t- n: The number of non-Halt states the considered Turing machines should have.
        ﻿\t- checkUntil: The maximum number of steps to check before declaring the Turing machine non-halting. Default 100."""

        try: assert n >= 1
        except: raise Exception("n must be positive.")
        try: assert checkUntil >= 1
        except: raise Exception("checkUntil must be positive.")
        return max(*(x.halting(checkUntil) for x in Turing.beavers(n)))
