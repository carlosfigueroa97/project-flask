import pandas as pd
import matplotlib.pyplot as plt

def read_csv(routeFile):
    route = routeFile
    df = pd.read_csv(route)
    return df

def graph_dataframe(route, columnName, option, nameGraph):
    df = read_csv(route)
    if(option == 'barra'):
        plt.hist(df[columnName], df['Year'])
    elif option == 'pastel':
        plt.pie(df[columnName], labels=df['Year'])
    else:
        plt.plot(df[columnName], 'b--')
    plt.savefig("{}.png".format(nameGraph))

