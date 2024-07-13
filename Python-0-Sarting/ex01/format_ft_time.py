import time as time

epoch = time.time()

epoch_sec = "{:,.4f}".format(epoch)
epoch_sci = "{:,.2e}".format(epoch)

str_tm = time.localtime(epoch)
date = time.strftime("%b %d %Y", str_tm)

print("Seconds since January 1, 1970:", epoch_sec, "or", epoch_sci, "in scientific notation")
print(date)