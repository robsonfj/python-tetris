class FileSaver:

    def readFile(self, file_name):
        file = open(file_name, "r+")

        lines = file.readlines()

        file.close()

        return lines

    def writeToFile(self, text, file_name):
        file = open(file_name, "w+")

        file.write(text)

        file.close()
