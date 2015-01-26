def DataLog(filename,data_list):
    try:
        with open(filename,"a") as f:
            data = "$".join(data_list)
            f.write(data)
            f.write("\n")
        return True
    except:
        return False

def readDataLog(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()

        data = data.split("\n")
        data_valid = []
        for i in data:
            data_valid.append(i)

        datas = []
        for i in data_valid:
            datas.append(i.replace("\n","").split("$"))
        datas.remove([''])
        return datas
    except:
        return False