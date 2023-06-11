import subprocess

file_map = {
        "txt" : "0001",
        "png" : "0010"
}

def main():
        # get file name
        file_name = "filetosend.txt"

        # get file type
        file_type = file_name.split('.')[1]

        # convert file to bits
        bytes = file_to_byte(file_name)
        bits = bytes_to_bits(bytes)

        # starting bits to calculate spacing
        starting_bits = "1010"

        # bits to send
        bits = starting_bits + file_map[file_type] + bits

        # ending bit
        bits += "1"

        # send
        send(bits)
        print(bits)

def file_to_byte(file_name):
        with open(file_name, "rb") as file:
                bytes = file.read()
        return bytes

def bytes_to_bits(bytes):
        return ''.join(format(byte, '08b') for byte in bytes)

def send(bits):
        frequency = "172.0M"
        pause = "10000"
        reps = "1"
        subprocess.run(["sudo", "sendook", "-f", frequency, "-0", pause, "-1", pause, "-r", reps, bits])

if __name__ == "__main__":
        main()

