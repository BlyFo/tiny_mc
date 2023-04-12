import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE_NAME = "data.csv"

def plot_average_ipc():
    df = pd.read_csv(DATA_FILE_NAME)
    df_avg = df[df['type'] == 'Average']
    df_avg.plot(x="description",y="instuctions per cycle",kind="bar")

    plt.ylabel("Instucciones por ciclo")
    plt.xlabel("")
    plt.xticks(rotation=0, ha='center')
    plt.show()

def plot_average_time():
    df = pd.read_csv(DATA_FILE_NAME)
    df_avg = df[df['type'] == 'Average']
    df_avg.plot(x="description",y="time",kind="bar")
    plt.ylabel("Tiempo (s))")
    plt.xlabel("")
    plt.xticks(rotation=0, ha='center')
    plt.show()

if __name__ == "__main__":
    plot_average_ipc()
    plot_average_time()
