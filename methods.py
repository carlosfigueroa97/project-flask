import pandas as pd
import os
import matplotlib.pyplot as plt

def read_csv(file):
    df = pd.read_csv('./pdfs/' + file)
    return df

def graph_dataframe(route, columnY, columnX, option, nameGraph, app):
    try:
        df = read_csv(route)
        if(option == 'barra'):
            plt.hist(df[columnY], df[columnX])
        elif option == 'pastel':
            plt.pie(df[columnY], labels=df[columnX])
        else:
            plt.plot(df[columnY], 'b--')
        plt.savefig(os.path.join(app.config['IMG_FOLDER']) + "{}.png".format(nameGraph))
        return plt
    except SystemError as err:
        print(err)

