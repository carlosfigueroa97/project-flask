import pandas as pd
import os
import matplotlib.pyplot as plt

def read_csv(file):
    df = pd.read_csv('./pdfs/' + file)
    return df

def graph_dataframe(filename, columnY, columnX, option, nameGraph, app):
    try:
        print(filename)
        df = read_csv(filename)
        if(option == 'barra'):
            plt.step(df[columnY], df[columnX])
        elif option == 'pastel':
            plt.scatter(df[columnY], df[columnX])
        else:
            plt.plot(df[columnY], 'b--')
        plt.savefig(os.path.join(app.config['IMG_FOLDER']) + "{}.png".format(nameGraph))
    except SystemError as err:
        print(err)

