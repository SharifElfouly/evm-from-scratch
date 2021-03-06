def address(cpu):
    cpu.stack.push("0xD912bCb457Ea4FB70EEAD8cfbbb97a32319e4dC7")
    cpu.pc += 1
    cpu.gas_dec(3)

def balance(cpu):
    address = cpu.stack.pop()
    warm, account = cpu.access_account(address)
    cpu.stack.push(account.balance)

    cpu.pc += 1
    cpu.gas_dec(100 if warm else 2600)

def origin(cpu):
    cpu.stack.push("0xD912bCb457Ea4FB70EEAD8cfbbb97a32319e4dC7")
    cpu.pc += 1
    cpu.gas_dec(2)

def caller(cpu):
    cpu.stack.push("0xD912bCb457Ea4FB70EEAD8cfbbb97a32319e4dC7")
    cpu.pc += 1
    cpu.gas_dec(2)

def callvalue(cpu):
    cpu.stack.push(0x00)
    cpu.pc += 1
    cpu.gas_dec(2)

def calldataload(cpu):
    i = cpu.stack.pop()

    delta = 0
    if i+32 > len(cpu.calldata):
        delta = i+32 - len(cpu.calldata)

    # always has to be 32 bytes
    # if its not we append 0x00 bytes until it is
    calldata = cpu.calldata[i:i+32-delta]
    calldata += 0x00*delta

    cpu.stack.push(calldata)
    cpu.pc += 1
    cpu.gas_dec(3)

def calldatasize(cpu):
    cpu.stack.push(0x00)
    cpu.pc += 1
    cpu.gas_dec(2)

def calldatacopy(cpu):
    destOffset = cpu.stack.pop().value
    offset = cpu.stack.pop().value
    size = cpu.stack.pop().value

    calldata = cpu.calldata[offset:offset+size]
    memory_expansion_cost = cpu.memory.store(destOffset, calldata)

    static_gas = 3
    minimum_word_size = (size + 31) // 32
    dynamic_gas = 3 * minimum_word_size + memory_expansion_cost

    cpu.gas_dec(static_gas + dynamic_gas)
    cpu.pc += 1

def codesize(cpu):
    cpu.stack.push(0x00)
    cpu.pc += 1
    cpu.gas_dec(2)

def codecopy(cpu):
    destOffset = cpu.stack.pop().value
    offset = cpu.stack.pop().value
    size = cpu.stack.pop().value

    code = cpu.program[offset:offset+size]
    memory_expansion_cost = cpu.memory.store(destOffset, code)

    static_gas = 3
    minimum_word_size = (size + 31) / 32
    dynamic_gas = 3 * minimum_word_size + memory_expansion_cost

    cpu.gas_dec(static_gas + dynamic_gas)
    cpu.pc += 1

def gasprice(cpu):
    cpu.stack.push(0x00)
    cpu.pc += 1
    cpu.gas_dec(2)

def extcodesize(cpu):
    address = cpu.stack.pop()

    warm, account = cpu.access_account(address)
    cpu.stack.push(account.codesize)

    cpu.gas_dec(100 if warm else 2600)
    cpu.pc += 1

def extcodecopy(cpu):
    address = cpu.stack.pop()
    destOffset = cpu.stack.pop()
    offset = cpu.stack.pop()
    size = cpu.stack.pop()

    warm, account = cpu.access_account(address)
    extcode = account.code[offset:offset+size]
    memory_expansion_cost = cpu.memory.store(destOffset, extcode)

    # refactor this in seperate method
    minimum_word_size = (size + 31) / 32
    dynamic_gas = 3 * minimum_word_size + memory_expansion_cost
    address_access_cost = 100 if warm else 2600

    cpu.gas_dec(dynamic_gas + address_access_cost)
    cpu.pc += 1

def returndatasize(cpu):
    cpu.stack.push(len(cpu.prev_returndata))
    cpu.pc += 1
    cpu.gas_dec(2)

def returndatacopy(cpu):
    destOffset = cpu.stack.pop()
    offset = cpu.stack.pop()
    size = cpu.stack.pop()

    returndata = cpu.program[offset:offset+size]
    memory_expansion_cost = cpu.memory.store(destOffset, returndata)

    minimum_word_size = (size + 31) / 32
    dynamic_gas = 3 * minimum_word_size + memory_expansion_cost

    cpu.gas_dec(3 + dynamic_gas)
    cpu.pc += 1


def extcodehash(cpu):
    address = cpu.stack.pop()

    warm, account = cpu.access_account(address)
    cpu.stack.push(account.hash)

    cpu.gas_dec(100 if warm else 2600)
    cpu.pc += 1

def blockhash(cpu):
    blockNumber = cpu.stack.pop().value
    if blockNumber > 256: raise Exception("blockhash: Only last 256 blocks can be accessed")
    cpu.stack.push(0x1cbcfa1ffb1ca1ca8397d4f490194db5fc0543089b9dee43f76cf3f962a185e8)

    cpu.pc += 1
    cpu.gas_dec(20)

def coinbase(cpu):
    # address of miner
    cpu.stack.push(0x1cbcfa1ffb1ca1ca8397d4f490194db5fc0543089b9dee43f76cf3f962a185e8)

    cpu.pc += 1
    cpu.gas_dec(2)
