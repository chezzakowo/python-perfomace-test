import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import datetime
# Function to calculate average values from the log file
def calculate_averages(file_path):
    cpu_values = []
    ram_values = []
    fps_values = []

    with open(file_path, "r") as file:
        for line in file:
            # Extract values from the log file
            if "CPU" in line and "RAM" in line and "FPS" in line:
                try:
                    timestamp_str, data_str = line.split(" - ", 1)
                    timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                    
                    cpu_values.append(float(data_str.split("CPU = ")[1].split("%")[0]))
                    ram_values.append(float(data_str.split("RAM = ")[1].split("%")[0]))
                    fps_values.append(float(data_str.split("FPS = ")[0]))
                except (ValueError, IndexError):
                    # Handle cases where the line doesn't contain the expected values
                    continue

    # Calculate averages
    avg_cpu = sum(cpu_values) / len(cpu_values) if cpu_values else 0
    avg_ram = sum(ram_values) / len(ram_values) if ram_values else 0
    avg_fps = sum(fps_values) / len(fps_values) if fps_values else 0

    return avg_cpu, avg_ram, avg_fps

# Function to plot a graph with timestamp
def plot_graph(file_path):
    timestamps = []
    cpu_values = []
    ram_values = []
    fps_values = []

    with open(file_path, "r") as file:
        for line in file:
            # Extract values from the log file
            if "CPU" in line and "RAM" in line and "FPS" in line:
                try:
                    timestamp_str, data_str = line.split(" - ", 1)
                    timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

                    timestamps.append(timestamp)
                    cpu_values.append(float(data_str.split("CPU = ")[1].split("%")[0]))
                    ram_values.append(float(data_str.split("RAM = ")[1].split("%")[0]))
                    fps_values.append(float(data_str.split("FPS = ")[1]))
                except (ValueError, IndexError):
                    # Handle cases where the line doesn't contain the expected values
                    continue

    # Plot the graph with timestamp
    plt.plot(timestamps, cpu_values, label='CPU', color='blue')
    plt.plot(timestamps, ram_values, label='RAM', color='green')
    plt.plot(timestamps, fps_values, label='FPS', color='red')

    plt.xlabel('Timestamp')
    plt.ylabel('Usage')
    plt.title('CPU, RAM, and FPS Usage Over Time')
    plt.legend()
    plt.show()


# Function to plot a graph
def plot_graph(file_path):
    cpu_values = []
    ram_values = []
    fps_values = []

    with open(file_path, "r") as file:
        for line in file:
            # Extract values from the log file
            if "CPU" in line and "RAM" in line and "FPS" in line:
                try:
                    cpu_values.append(float(line.split("CPU = ")[1].split("%")[0]))
                    ram_values.append(float(line.split("RAM = ")[1].split("%")[0]))
                    fps_values.append(float(line.split("FPS = ")[1]))
                except (ValueError, IndexError):
                    # Handle cases where the line doesn't contain the expected values
                    continue

    # Plot the graph
    plt.plot(cpu_values, label='CPU', color='blue')
    plt.plot(ram_values, label='RAM', color='green')
    plt.plot(fps_values, label='FPS', color='red')

    plt.xlabel('Iteration')
    plt.ylabel('Usage')
    plt.title('CPU, RAM, and FPS Usage Over Time')
    plt.legend()
    plt.show()

# Function to handle the "Open File" button click event
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        avg_cpu, avg_ram, avg_fps = calculate_averages(file_path)
        result_label.config(text=f"Average CPU: {avg_cpu:.2f}%\nAverage RAM: {avg_ram:.2f}%\nAverage FPS: {avg_fps:.2f}")

# Function to handle the "Show Graph" button click event
def show_graph():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        plot_graph(file_path)

# Create the main window
window = tk.Tk()
window.title("Log Analyzer")

# Create and configure widgets
open_button = tk.Button(window, text="Open File", command=open_file)
open_button.pack(pady=20)

result_label = tk.Label(window, text="")
result_label.pack(pady=20)

show_graph_button = tk.Button(window, text="Show Graph", command=show_graph)
show_graph_button.pack(pady=20)

# Start the GUI event loop
window.mainloop()
