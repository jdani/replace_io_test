import time
import csv
import io


def list_to_csv_row(lst):
    mem_file = io.StringIO()
    writer = csv.writer(mem_file, delimiter=',')
    writer.writerow(lst)
    csv_string = mem_file.getvalue()
    mem_file.close()
    return csv_string

row_count = 100000

headers = [  
    "timeStamp",
    "elapsed",
    "label",
    "responseCode",
    "responseMessage",
    "dataType",
    "success",
    "failureMessage",
    "bytes",
    "sentBytes",
    "grpThreads",
    "allThreads",
    "Latency",
    "IdleTime",
    "Connect",
    "Hostname"
]



sample_row = [
    str('1622465708079'),
    str('3'),
    str('/2021/05/28/hola-mundo/'),
    str('0'),
    str('KO'),
    str('unknown'),
    str('false'),
    str("HTTPConnectionPool(host='192.168.1.128', port=80): Max retries exceeded with url: /2021/05/28/hola-mundo/ (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f2fa690ba90>: Failed to establish a new connection: [Errno 111] Connection refused'))"),
    str('0'),
    str('0'),
    str('1306'),
    str('1306'),
    str('0'),
    str('0'),
    str('0'),
    str('loadtest-solemn-unicorn-worker-tdv8s_1')
]




def main():

    print("Running tests against {} rows".format(row_count))
    print("Replace method test start...")
    replace_start = time.time()
    replace_rows = ''
    for _ in range(row_count):
        replace_rows += ','.join([x.replace(',','\\,') for x in sample_row]) + '\n'
    replace_stop = time.time()
    print("Replace method test finished...")

    print("io-csv method test start...")
    io_start = time.time()
    io_rows = ''
    for _ in range(row_count):
        io_rows += list_to_csv_row(sample_row)
    io_stop = time.time()
    print("io-csv method test finished...")

    replace_total_time = replace_stop - replace_start
    io_total_time = io_stop - io_start

    print("Total replace method time: {}".format(replace_total_time))
    print("Total io method time: {}".format(io_total_time))
    if io_total_time > replace_total_time:
        print("Replace method is faster {}s faster for {} rows!!".format(io_total_time - replace_total_time, row_count))
    else:
        print("Replace IO-CSV is faster {}s faster for {} rows!!".format(io_total_time - replace_total_time, row_count))

    io_file = 'io.csv'
    replace_file = 'replace.csv'

    with open(replace_file, 'w+') as f:
        f.write(replace_rows)
    
    with open(io_file, 'w+') as f:
        f.write(io_rows)




if __name__ == '__main__':
    main()




