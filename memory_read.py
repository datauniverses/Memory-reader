from ahk import AHK
import pymem

ah = AHK(executable_path="C://Program Files//AutoHotkey//UX//AutoHotkeyUX.exe")
application_window = AHK.find_window_by_title(ah, title=b'NSUNS4')

p1_hp_address = 0x1A615350E98
p1_hp_size = 4

p2_hp_address = 0x1A614FBB768
p2_hp_size = 4

p1_chakra_address = 0x1A615350E9C
p1_chk_size = 8

p2_chakra_address = 0x1A614FBB76C
p2_chk_size = 8

p1_subjustu_address = 0x1A615350EA8
p1_sub_size = 4

p2_subjustu_address = 0x1A614FBB778
p2_sub_size = 4

variables = [
    (p1_hp_address, p1_hp_size),
    (p2_hp_address, p2_hp_size),
    (p1_chakra_address, p1_chk_size),
    (p2_chakra_address, p2_chk_size),
    (p1_subjustu_address, p1_sub_size),
    (p2_subjustu_address, p2_sub_size)
]


def fetch_game_stats(variables):
    process_name = "NSUNS4.exe"  # Replace with the actual process name
    process = pymem.Pymem(process_name)
    stats_values = []

    for address, byte in variables:
        address = address  # Replace with the actual memory address
        # Open the process using Pymem

        # Read the memory value at the specified address as bytes
        value = process.read_bytes(address, byte)

        # Convert the bytes to an integer
        int_value = int.from_bytes(value, byteorder="little", signed=False)

        stats_values.append(int_value)

    return stats_values
