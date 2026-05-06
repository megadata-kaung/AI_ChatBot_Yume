# import tkinter as tk
# from tkinter import scrolledtext, PhotoImage
# import threading
# import json
#
# from Yume.yume import get_response
#
#
# class ChatInterface:
#     def __init__(self, root):
#         self.root = root
#         root.title("Yume")
#         # root.configure(bg='#282828')  # dark background
#         root.geometry("19204x1080")  # sets the window size
#
#         # load the background image
#         self.background_image = tk.PhotoImage(file="solo leveling 1920x1080.png")
#         self.background_label = tk.Label(root, image=self.background_image)
#         self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
#
#         # create a scrolled text widget fot the chat
#         self.chat_area = scrolledtext.ScrolledText(root, state='disabled',
#                                                    height=15,
#                                                    width=50,
#                                                    bg='#282828',
#                                                    fg='white', font=('MS Gothic', 12))
#
#         self.chat_area.place(x=-1000, y=250, width=924, height=476)  # Adjusted for the window size
#
#         # self.chat_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
#
#         # create an entry field for user input
#         self.user_input = tk.Entry(root, width=40,
#                                    bg='#333333',
#                                    fg='white',
#                                    font=('MS Gothic', 12))
#
#         # self.user_input.place(x=50, y=560, width=700)  # Adjust the position as needed
#         self.user_input.place(x=500, y=900, width=924)  # Adjusted for the window size
#
#         # self.user_input.grid(row=1, column=0, padx=10, pady=10)
#
#         # create a send button
#         self.send_button = tk.Button(root, text="Send", command=self.send_message,
#                                      bg='#4CAF50',
#                                      fg='white',
#                                      font=('MS Gothic', 12))
#         self.send_button.place(x=900, y=950, width=100)  # Adjusted for the window size
#
#         # self.send_button.grid(row=1, column=1, padx=10, pady=10)
#
#     def send_message(self):
#         message = self.user_input.get()
#         self.display_message(message, "User")
#         self.user_input.delete(0, tk.END)
#         threading.Thread(target=self.process_message, args=(message,)).start()
#
#     def display_message(self, message, sender):
#         self.chat_area.configure(state='normal')
#         self.chat_area.insert(tk.END, f"{sender}: {message}\n")
#         self.chat_area.configure(state='disabled')
#         self.chat_area.see(tk.END)
#
#     # def process_message(self, message):
#     #     placeholder for processing the message with 'Yume'
#     #     for now, I'll just simulate a response
#     # response = "this is a simulated response"
#     # self.display_message(response, "Yume")
#
#     def process_message(self, message):
#         response = get_response(message)
#         self.display_message(response, "Yume")
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     chat_interface = ChatInterface(root)
#     root.mainloop()
