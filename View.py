from tkinter import Tk, Entry, Button, Label, CENTER, END, messagebox, NO, Toplevel
from tkinter.ttk import Treeview
from Program import Program
from validations import is_integer, file_exists


class View:
    """
    Main program view.
    """

    def __init__(self, view: Tk):
        self.view = view
        self.__file_path_label: Label = None
        self.__file_path_entry: Entry = None
        self.__number_label: Label = None
        self.__number_entry: Entry = None
        self.__submit_button: Button = None

        self.create_file_path_entry()
        self.create_entry_number()
        self.create_submit_button()

        self.tree = self.create_tree_view(("1", "2"), 400)
        self.tree.grid(row=3, column=0, columnspan=3)
        if not self.fill_tree_view(Program.get_passwords(), self.tree):
            messagebox.showerror("Error", "There aren't any records to display")

        # ================================================================================
        # ================================ for tests only ================================

        self.file_path_entry.delete(0, END)
        self.file_path_entry.insert(0, "diceware.txt")

        self.number_entry.delete(0, END)
        self.number_entry.insert(0, 3)
        # ================================================================================

    @property
    def file_path_label(self) -> Label:
        """
        file path property getter
        :return: Label, self.file_path_label
        """
        return self.__file_path_label

    @file_path_label.setter
    def file_path_label(self, val: Label) -> None:
        """
        self file path setter
        :param val: Label
        :return: None
        """
        self.__file_path_label = val

    @property
    def file_path_entry(self) -> Entry:
        """
        file_path entry getter
        :return: Entry, self.file_path_entry
        """
        return self.__file_path_entry

    @file_path_entry.setter
    def file_path_entry(self, val: Entry) -> None:
        """
        self.file_path_entry setter
        :param val: Entry
        :return: None
        """
        self.__file_path_entry = val

    @property
    def number_label(self) -> Label:
        """
        number property getter
        :return: Label, self.number_label
        """
        return self.__number_label

    @number_label.setter
    def number_label(self, val: Label) -> None:
        """
        self number setter
        :param val: Label
        :return: None
        """
        self.__number_label = val

    @property
    def number_entry(self) -> Entry:
        """
        number entry getter
        :return: Entry, self.number_entry
        """
        return self.__number_entry

    @number_entry.setter
    def number_entry(self, val: Entry) -> None:
        """
        self.number_entry setter
        :param val: Entry
        :return: None
        """
        self.__number_entry = val

    @property
    def submit_button(self) -> Button:
        """
        self.submit_button getter
        :return: Button
        """
        return self.__submit_button

    @submit_button.setter
    def submit_button(self, val: Button) -> None:
        """
        self.submit_button setter
        :param val: Button
        :return: None
        """
        self.__submit_button = val

    def create_file_path_entry(self) -> None:
        """
        Create path label in view
        :return: None
        """
        self.file_path_label = Label(self.view, text="File Path")
        self.file_path_label.grid(row=0, column=0)
        self.file_path_entry = Entry(self.view)
        self.file_path_entry.grid(row=1, column=0)

    def create_entry_number(self) -> None:
        """
        Create number entry in view
        :return: None
        """
        self.number_label = Label(self.view, text="Number")
        self.number_label.grid(row=0, column=1)
        self.number_entry = Entry(self.view)
        self.number_entry.grid(row=1, column=1)

    def create_submit_button(self) -> None:
        """
        Create submit button in view
        :return: None
        """
        self.__submit_button = Button(self.view, text='Submit', command=self.on_submit_clicked)
        self.__submit_button.grid(row=1, column=2)

    def on_submit_clicked(self) -> None:
        """
        Function called by clicking on submit button
        :return: None
        """
        path = self.file_path_entry.get()
        number = self.number_entry.get()
        if is_integer(number) and file_exists(path):
            if Program.make_password(path, int(number)):
                if not self.fill_tree_view(Program.get_passwords(), self.tree):
                    messagebox.showwarning("Warning", "There aren't any records to display")
                else:
                    self.tree.delete(*self.tree.get_children())
                    self.fill_tree_view(Program.get_passwords(), self.tree)
            else:
                messagebox.showwarning("Warning", "There aren't any records to display")
        else:
            messagebox.showwarning("Warning", "Path must be path to valid file. Number must be an integer")

    def on_tree_select(self) -> None:
        """
        Function called by clicking on tree item
        :return: None
        """
        values = []
        for item in self.tree.selection():
            row_values = self.tree.item(item, 'values')
            values.append(row_values[1])
        if len(values) > 0:
            self.view.clipboard_clear()
            self.view.clipboard_append(values[0])
            self.show_notification("Password copied to clipboard")

    def show_notification(self, message: str, duration="1000") -> None:
        """
        This function show simple pop up window
        :param message: showing message
        :param duration: showing time
        :return: None
        """
        top = Toplevel()
        top.title('')
        lb = Label(top, text=message)
        lb.grid(row=0, column=0)
        top.after(duration, top.destroy)

    def create_tree_view(self, columns: tuple, height: int) -> Treeview:
        """
        Function creates a new Tree view
        :param columns: Tree view columns
        :param height: Tree view screen height
        :return: Tree view object reference
        """
        tree = Treeview(self.view, column=columns, show='headings', selectmode="extended", height=height)
        tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        return tree

    def fill_tree_view(self, data: list, tree: Treeview) -> bool:
        """
        Function fills an existing tree view with given data (list of dictionaries which contain the data to display)
        :param data: Data to display
        :param tree: Tree view to display the data at
        :return: True if there is some data to display and the data format is valid and False otherwise
        """
        # If parameters are valid
        if isinstance(tree, Treeview) and len(data) > 0:
            # Displaying columns' names
            i = 1
            for key in data[0].keys():
                tree.column(f"#{i}", anchor=CENTER, stretch=NO)
                tree.heading(f"#{i}", text=key)
                i += 1

            tree.column("#1", minwidth=0, width=100)
            tree.column("#2", minwidth=0, width=300)

            # Adding records' information
            for record in data:
                tree.insert('', END, values=([val for val in record.values()]))

            return True
        return False
