from cpu import CPU

# PROGRAM = [0x60, 0x42, 0x60, 0x01, 0x53, 0x00]
PROGRAM = [0x60, 0x42, 0x60, 0xFF, 0x53, 0x00]

cpu = CPU()
cpu.load(PROGRAM)
cpu.run()
