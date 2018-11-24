class File_Saver:
    def __init__(self, file_name, read_config= "r+", write_config= "w+"):
        self.file_name = file_name
        self.write_config = write_config
        self.read_config = read_config

    def readFile(self):
        file_data = open(self.file_name, self.read_config)

        lines = file_data.readlines()

        file_data.close()

        return lines

    def writeToFile(self, text):
        file_data = open(self.file_name, self.write_config)
        
        file_data.write(text)

        file_data.close()
