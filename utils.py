import matplotlib.pyplot as plt

def plot_clusters(dataframe, x_column, y_column, cluster_column):
    # Create a new figure
    plt.figure(figsize=(20, 12))

    # Loop through each unique cluster label
    for cluster_label in dataframe[cluster_column].unique():
        # Select the rows with the current cluster label
        cluster_data = dataframe[dataframe[cluster_column] == cluster_label]

        # Plot the scatter plot for the current cluster
        plt.scatter(cluster_data[x_column], cluster_data[y_column], label=cluster_label)
        for index, row in cluster_data.iterrows():
            plt.text(row[x_column], row[y_column], index)
    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()

def plot(dataframe, x_column, y_column):
    # Create a new figure
    plt.figure(figsize=(10, 6))



        # Plot the scatter plot for the current cluster
    plt.scatter(dataframe[x_column], dataframe[y_column])
    for index, row in dataframe.iterrows():
        plt.text(row[x_column], row[y_column], index)
    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()