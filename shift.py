from datetime import timedelta

def shift_subtitles(srt_in, shift):
    # Create name for output file
    srt_out = srt_in.split(".")
    srt_out[0] += " shifted"
    srt_out = ".".join(srt_out)

    eof = False
    with open(srt_in, "r") as f_in, open(srt_out, "w") as f_out:
        while not eof:
            # Read section number
            curr_line = f_in.readline()
            # End of file reached
            if curr_line == "".rstrip():
                eof = True
            else:
                # Write section index
                f_out.write(curr_line)

                # Write updated times
                curr_line = f_in.readline().rstrip()
                times = curr_line.split(" --> ")
                f_out.write(f"{add_shift(times[0], shift)} --> {add_shift(times[1], shift)}\n")

                # Write subtitles
                while curr_line.rstrip() != "":
                    curr_line = f_in.readline()
                    f_out.write(curr_line)

# Add a shift to the given times
def add_shift(time, shift):
    # TODO: add shift to time (use datetime.timedelta)

    return time
