import threading,zipfile

class AsyncZip(threading.Thread):

    def __init__(self,infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)


background = AsyncZip('C:\\Users\\ant\\Desktop\\aaa.txt', 'C:\\Users\\ant\\Desktop\\aaa.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')