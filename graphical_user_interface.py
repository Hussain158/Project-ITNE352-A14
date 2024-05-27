import socket
import json
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

def send_client(option, cs):
    cs.send(option.encode())

def main_menu(cs, username):
    def handle_option(option):
        if option == 1:
            headline_menu(cs, username)
        elif option == 2:
            sources_menu(cs, username)
        elif option == 3:
            cs.close()
            root.quit()
        else:
            messagebox.showerror("Invalid Option", "Please choose a valid option")

    for widget in root.winfo_children():
        widget.destroy()

    welcome_label = ttk.Label(root, text=f"Welcome {username}, please choose the desired option:", font=('Arial', 14))
    welcome_label.pack(pady=20)

    button_frame = ttk.Frame(root)
    button_frame.pack(pady=20)

    option1_btn = ttk.Button(button_frame, text="1- Search for specific headlines", command=lambda: handle_option(1))
    option2_btn = ttk.Button(button_frame, text="2- Search for a specific list of sources", command=lambda: handle_option(2))
    option3_btn = ttk.Button(button_frame, text="3- Quit the program", command=lambda: handle_option(3))

    option1_btn.grid(row=0, column=0, padx=20, pady=10)
    option2_btn.grid(row=1, column=0, padx=20, pady=10)
    option3_btn.grid(row=2, column=0, padx=20, pady=10)

def headline_menu(cs, username):
    def handle_lower_option(lower_option):
        if lower_option == 1:
            request = simpledialog.askstring("Keyword Search", "Enter a specific keyword you want to search about:")
            option = f"1.{lower_option}.{request}"
            send_client(option, cs)
            headlines(cs, username)
        elif lower_option == 2:
            category_menu(cs, username, "headline")
        elif lower_option == 3:
            country_menu(cs, username, "headline")
        elif lower_option == 4:
            option = f"1.{lower_option}.null"
            send_client(option, cs)
            headlines(cs, username)
        elif lower_option == 5:
            main_menu(cs, username)
        else:
            messagebox.showerror("Invalid Option", "Please choose a valid option")

    for widget in root.winfo_children():
        widget.destroy()

    option_label = ttk.Label(root, text="Headline Search Options:", font=('Arial', 14))
    option_label.pack(pady=20)

    button_frame = ttk.Frame(root)
    button_frame.pack(pady=20)

    option1_btn = ttk.Button(button_frame, text="1- Search for Keywords", command=lambda: handle_lower_option(1))
    option2_btn = ttk.Button(button_frame, text="2- Search by Category", command=lambda: handle_lower_option(2))
    option3_btn = ttk.Button(button_frame, text="3- Search by Country", command=lambda: handle_lower_option(3))
    option4_btn = ttk.Button(button_frame, text="4- List all New Headlines", command=lambda: handle_lower_option(4))
    option5_btn = ttk.Button(button_frame, text="5- Back to Main Menu", command=lambda: handle_lower_option(5))

    option1_btn.grid(row=0, column=0, padx=20, pady=10)
    option2_btn.grid(row=1, column=0, padx=20, pady=10)
    option3_btn.grid(row=2, column=0, padx=20, pady=10)
    option4_btn.grid(row=3, column=0, padx=20, pady=10)
    option5_btn.grid(row=4, column=0, padx=20, pady=10)

def sources_menu(cs, username):
    def handle_lower_option(lower_option):
        if lower_option == 1:
            category_menu(cs, username, "sources")
        elif lower_option == 2:
            country_menu(cs, username, "sources")
        elif lower_option == 3:
            language_menu(cs, username)
        elif lower_option == 4:
            option = f"2.{lower_option}.null"
            send_client(option, cs)
            resources(cs, username)
        elif lower_option == 5:
            main_menu(cs, username)
        else:
            messagebox.showerror("Invalid Option", "Please choose a valid option")

    for widget in root.winfo_children():
        widget.destroy()

    option_label = ttk.Label(root, text="Sources Search Options:", font=('Arial', 14))
    option_label.pack(pady=20)

    button_frame = ttk.Frame(root)
    button_frame.pack(pady=20)

    option1_btn = ttk.Button(button_frame, text="1- Search by Category", command=lambda: handle_lower_option(1))
    option2_btn = ttk.Button(button_frame, text="2- Search by Country", command=lambda: handle_lower_option(2))
    option3_btn = ttk.Button(button_frame, text="3- Search by Languages", command=lambda: handle_lower_option(3))
    option4_btn = ttk.Button(button_frame, text="4- List all the available sources", command=lambda: handle_lower_option(4))
    option5_btn = ttk.Button(button_frame, text="5- Back to Main Menu", command=lambda: handle_lower_option(5))

    option1_btn.grid(row=0, column=0, padx=20, pady=10)
    option2_btn.grid(row=1, column=0, padx=20, pady=10)
    option3_btn.grid(row=2, column=0, padx=20, pady=10)
    option4_btn.grid(row=3, column=0, padx=20, pady=10)
    option5_btn.grid(row=4, column=0, padx=20, pady=10)

def category_menu(cs, username, menu_type):
    def select_category(category):
        if menu_type == "headline":
            option = f"1.2.{category}"
            send_client(option, cs)
            headlines(cs, username)
        elif menu_type == "sources":
            option = f"2.1.{category}"
            send_client(option, cs)
            resources(cs, username)

    for widget in root.winfo_children():
        widget.destroy()

    option_label = ttk.Label(root, text="Select Category:", font=('Arial', 14))
    option_label.pack(pady=20)

    button_frame = ttk.Frame(root)
    button_frame.pack(pady=20)

    for category in cat:
        btn = ttk.Button(button_frame, text=category.capitalize(), command=lambda c=category: select_category(c))
        btn.pack(padx=20, pady=10)

    back_btn = ttk.Button(root, text="Back", command=lambda: headline_menu(cs, username) if menu_type == "headline" else sources_menu(cs, username))
    back_btn.pack(pady=20)

def country_menu(cs, username, menu_type):
    def select_country(country):
        if menu_type == "headline":
            option = f"1.3.{country}"
            send_client(option, cs)
            headlines(cs, username)
        elif menu_type == "sources":
            option = f"2.2.{country}"
            send_client(option, cs)
            resources(cs, username)

    for widget in root.winfo_children():
        widget.destroy()

    option_label = ttk.Label(root, text="Select Country:", font=('Arial', 14))
    option_label.pack(pady=20)

    button_frame = ttk.Frame(root)
    button_frame.pack(pady=20)

    for country in regions:
        btn = ttk.Button(button_frame, text=country.upper(), command=lambda c=country: select_country(c))
        btn.pack(padx=20, pady=10)

    back_btn = ttk.Button(root, text="Back", command=lambda: headline_menu(cs, username) if menu_type == "headline" else sources_menu(cs, username))
    back_btn.pack(pady=20)
cat = ["entertainment","business" , "general", "technology","sports", "science" ,"health" ]
regions = ["eg", "nz", "ca", "ae", "sa", "gb", "us","au" , "ma"]
languages = ["ar", "en"]
def language_menu(cs, username):
    def select_language(language):
        option = f"2.3.{language}"
        send_client(option, cs)
        resources(cs, username)

    for widget in root.winfo_children():
        widget.destroy()

    option_label = ttk.Label(root, text="Select Language:", font=('Arial', 14))
    option_label.pack(pady=20)

    button_frame = ttk.Frame(root)
    button_frame.pack(pady=20)

    for language in languages:
        btn = ttk.Button(button_frame, text=language.upper(), command=lambda l=language: select_language(l))
        btn.pack(padx=20, pady=10)

    back_btn = ttk.Button(root, text="Back", command=lambda: sources_menu(cs, username))
    back_btn.pack(pady=20)

def headlines(cs, username):
    for widget in root.winfo_children():
        widget.destroy()

    headlines_label = ttk.Label(root, text="Please wait, we are processing your request...", font=('Arial', 14))
    headlines_label.pack(pady=20)

    headlines_data = cs.recv(200000).decode()
    articles = json.loads(headlines_data)['articles']

    listbox = tk.Listbox(root, width=80, height=20)
    for index, item in enumerate(articles):
        listbox.insert(tk.END, f"{index + 1}. {item['title']} - {item['description']}")
    listbox.pack(pady=20)

    def show_details(event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            desired_headline = articles[index]
            details = f"""
            Article {index + 1} Details:
            Source: {desired_headline['source']['name']}
            Author: {desired_headline['author']}
            Title: {desired_headline['title']}
            URL: {desired_headline['url']}
            Description: {desired_headline['description']}
            Published At: {desired_headline['publishedAt']}
            """
            messagebox.showinfo("Headline Details", details)

    listbox.bind('<<ListboxSelect>>', show_details)

    back_btn = ttk.Button(root, text="Back", command=lambda: headline_menu(cs, username))
    back_btn.pack(pady=20)

def resources(cs, username):
    for widget in root.winfo_children():
        widget.destroy()

    resources_label = ttk.Label(root, text="Please wait, we are processing your request...", font=('Arial', 14))
    resources_label.pack(pady=20)

    sources_data = cs.recv(200000).decode()
    sources = json.loads(sources_data)['sources']

    listbox = tk.Listbox(root, width=80, height=20)
    for index, item in enumerate(sources):
        listbox.insert(tk.END, f"{index + 1}. {item['name']}")
    listbox.pack(pady=20)

    def show_details(event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            desired_source = sources[index]
            details = f"""
            Source {index + 1} Details:
            Source: {desired_source['name']}
            Country: {desired_source['country']}
            Description: {desired_source['description']}
            URL: {desired_source['url']}
            Category: {desired_source['category']}
            Language: {desired_source['language']}
            """
            messagebox.showinfo("Source Details", details)

    listbox.bind('<<ListboxSelect>>', show_details)

    back_btn = ttk.Button(root, text="Back", command=lambda: sources_menu(cs, username))
    back_btn.pack(pady=20)

if __name__ == "__main__":
    server_ip = "127.0.0.1"
    server_port = 4926

    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs.connect((server_ip, server_port))
    print(f"Connected to server {server_ip}:{server_port}")

    root = tk.Tk()
    root.title("News Client")
    root.geometry("800x600")

    username = simpledialog.askstring("Username", "Enter your username:")
    if username:
        send_client(username, cs)
        main_menu(cs, username)

    root.mainloop()
