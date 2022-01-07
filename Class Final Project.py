# Name: Tahsinul Haque Abir
# VUnetID: abirth
# Email: tahsinul.h.abir@vanderbilt.edu
# Class: CS 1104 - Vanderbilt University
# Section: 2
# Date: 12/09/2021
# Honor statement: I attest that I understand the honor code for this class and have
#                  neither given nor received any unauthorized aid on this assignment.

# Program description: In this assignment, a class template is developed to
#                      represent a person and their children. A client program is also
#                      developed that will instantiate Person objects that as
#                      a whole represents a family.

class Person:
    def __init__(self, name = 'N/A', birth_date = 'N/A', death_date =''):
        """The constructor takes name, birth date and death date as input and
        create a person object.

        Parameters:
          name:
            The name of the Person.
          birth_date:
            The date of birth of the person.
          death_date:
            The date of death of the person.
        """
        self.__name = name
        self.__birth_date = birth_date
        self.__death_date = death_date
        self.__parent = None
        self.__children = []

    def add_child(self, person):
        """This method adds a child of the Person object.

        Parameters:
          person:
            The child of the Person object as a Person object.
        """
        person.__parent = self
        self.__children.append(person)

    def delete_child(self, name):
        """This method deletes a child of the Person object.

        Parameters:
          name:
            The name of the child to be deleted.
        """
        for child in self.__children[:]:
            if name == child.__name:
                self.__children.remove(child)

    def get_age(self):
        """This method calculates the age of the Person object.

        Returns:
          The age of the Person object.
        """
        birthday = self.__birth_date
        deathday = self.__death_date
        birth_year = int(birthday[:4])
        birth_month = int(birthday[5:7])
        birth_date = int(birthday[8:])
        death_year = int(deathday[:4])
        death_month = int(deathday[5:7])
        death_date = int(deathday[8:])

        if death_month < birth_month:
            return death_year - birth_year -1
        elif death_month == birth_month:
            if death_date < birth_date:
                return death_year - birth_year - 1
            else:
                return death_year - birth_year
        else:
            return death_year - birth_year

    def get_birth_date(self):
        """This method gets the birth date of the person object.

        Returns:
          The birth date of the person object.
        """
        return self.__birth_date

    def get_child(self, name):
        """This method returns the child as a Person object with the particular name.

        Parameters:
          name:
            The name of the child.

        Returns:
          The child as a Person object.
        """
        for child in self.__children:
            if name == child.__name:
                return child

    def get_children(self):
        """This method gets the children list of the Person object.

        Returns:
          The list containing all children names.
        """
        return self.__children

    def get_death_date(self):
        """This method gets the date of the death of the person object.

        Returns:
          The date of the death of the Person object.
        """
        return self.__death_date

    def get_name(self):
        """This method gets the name of the person object.

        Returns:
          The name of the Person object.
        """
        return self.__name

    def get_parent(self):
        """This method returns the parent of the Person object.

        Returns:
          The parent of the Person object.
        """
        return self.__parent

    def set_birth_date(self, birth_date):
        """This method updates the date of birth of the person to the string
        passed as a parameter.

        Parameters:
          birth_date:
            The date of the birth of the person.
        """
        self.__birth_date = birth_date

    def set_death_date(self, death_date):
        """This method updates the date of death of the person to the string
        passed as a parameter.

        Parameters:
          death_date:
            The date of the death of the person.
        """
        self.__death_date = death_date

    def set_name(self, name):
        """This method updates the name of the person to the string
        passed as a parameter to this method.

        Parameters:
          name:
            The name of the Person object.
        """
        self.__name = name

    def set_parent(self, parent):
        """This method updates the parent of the person to the Person object
        passed as a parameter to this method.

        Parameters:
          The parent of the person as a object.
        """
        self.__parent = parent

    def __str__(self):
        """This method stringifies the Person object.

        Returns:
          The Person object as a formatted string.
        """
        if self.__death_date != '':
            return f"{self.__name} *{self.__birth_date} " \
                   f"✝{self.__death_date} ({self.get_age()})"
        else:
            return f"{self.__name} *{self.__birth_date}"

    def __eq__(self, other):
        """This method checks whether two Person objects are equal or not.

        Returns:
          True if the two Person objects are equal; else false.
        """
        return isinstance(other, Person) and other.__name == self.__name \
               and other.__birth_date[:7] == self.__birth_date[:7]


def header(current_person):
    """The function prints the menu.

    Parameters:
      current_person:
        The current Person object.
    """
    print('------------------------------------------------------')
    print(current_person)
    print('------------------------------------------------------')
    print(' 1) Edit name                 6) Print statistics\n'
          ' 2) Edit date of birth        7) Print children\n'
          ' 3) Edit date of death        8) Print grandchildren\n'
          ' 4) Add a child               9) Print aunts/uncles\n'
          ' 5) Delete a child           10) Print cousins')
    print()
    print('11) Enter child\'s family     12) Enter parent\'s family')
    print()


def name_fun():
    """This function asks for the name and checks whether a name is
    entered or not.

    Returns:
      The name of the person.
    """
    name = input("Enter name: ")
    while name == '':
        name = input("ERROR: No name entered, try again: ")

    return name


def option1(current_person):
    """The name of the current person can be updated using this function.

    Parameters:
      current_person:
        The current Person object.

    Returns:
      The current Person object.
    """
    name = name_fun()
    current_person.set_name(name)
    print()

    return current_person


def dob_fun(dob):
    """This function takes a date of birth and checks whether it's valid or not.

    Parameters:
      dob:
        The date of the birth of the person.

    Returns:
      The proper date of birth of the person.
    """
    condition = len(dob) == 10 and (dob[:4] + dob[5:7] + dob[8:]).isdigit() \
                and dob[4] == '-' and dob[7] == '-' \
                and int(dob[5:7]) <= 12 and int(dob[8:]) <= 30

    while not(condition):
        dob = input("ERROR: Must follow 1970-01-01 format, try again: ")
        condition = len(dob) == 10 and (dob[:4] + dob[5:7] + dob[8:]).isdigit() \
                and dob[4] == '-' and dob[7] == '-' \
                and int(dob[5:7]) <= 12 and int(dob[8:]) <= 30

    return dob


def option2(current_person):
    """The date of birth of the current person can be updated using this function.

    Parameters:
      current_person:
        The current Person object.

    Returns:
      The current Person object.
    """
    dob = input("Enter date of birth: ")
    dob = dob_fun(dob)
    current_person.set_birth_date(dob)
    print()

    return current_person


def option3(current_person):
    """The date of death of the current person can be updated using this function.

    Parameters:
      current_person:
        The current Person object.

    Returns:
      The current Person object.
    """
    dod = input("Enter date of death: ")
    dod = dob_fun(dod)
    current_person.set_death_date(dod)
    print()

    return current_person


def option4(current_person):
    """A child of the current person can be added using this function.

    Parameters:
      current_person:
        The current Person object.

    Returns:
      The current Person object.
    """
    name = name_fun()
    dob = input("Enter date of birth: ")
    dob = dob_fun(dob)

    child = Person(name, dob)

    if child in current_person.get_children():
        print('ERROR: Child with same name, and year and month of birth already exists.')
    else:
        current_person.add_child(child)
    print()

    return current_person


def child_fun(current_person):
    """This function checks whether the person has a child or not and works
    accordingly.

    Parameters:
      current_person:
        The current Person object.

    Returns:
      The picked child number and the children list as a tuple.
    """
    ch_lst = current_person.get_children()
    if len(ch_lst) == 0:
        print(f"No children found for {current_person.get_name()}.")
        picked_ch = 0

    else:
        for idx, child in enumerate(ch_lst):
            print(f'{idx + 1}) {child.get_name()}')
        picked_ch = int(input("Select a child (or 0 to go back to main menu): "))
        print()
        if picked_ch == 0:
            print("Returning to main menu.")

    return picked_ch, ch_lst


def option5(current_person):
    """A child of the current person can be deleted using this function.

    Parameters:
      current_person:
        The current Person object.

    Returns:
      The current Person object.
    """
    del_ch, ch_lst = child_fun(current_person)
    if del_ch != 0:
        print(f'{ch_lst[del_ch - 1].get_name()} deleted.')
        del ch_lst[del_ch - 1]
    print()

    return current_person


def option11(current_person):
    """Going into the family of a child can be done using this function.

    Parameters:
      current_person:
        The current Person object.

    Returns:
      The current Person object (The Child)
    """
    picked_ch, ch_lst = child_fun(current_person)
    if picked_ch == 0:
        print()
        return current_person
    else:
        current_person = ch_lst[picked_ch - 1]
        print(f"Entering family of {current_person.get_name()}.")
        print()

        return current_person


def option12(current_person):
    """Going into the family of the parent can be done using this function.

    Parameters:
      current_person:
        The current Person object.

    Returns:
      The current Person object. (The Parent)
    """
    if current_person.get_parent() is None:
        print(f"No parent found for {current_person.get_name()}.")
        print()
        return current_person
    else:
        current_person = current_person.get_parent()
        print(f"Entering family of {current_person.get_name()}.")
        print()
        return current_person


def option6(current_person):
    """The number of children and grandchildren of a person can be printed
    using this function.

    Parameters:
      current_person:
        The current Person object.

    Returns:
      The original Person object for whom the function was called.
    """
    print(f"Number of children: {len(current_person.get_children())}")
    grandchild = 0
    temp = current_person
    for child in current_person.get_children():
        current_person = child
        grandchild += len(current_person.get_children())

    print(f"Number of grandchildren: {grandchild}")
    print()

    return temp


def option7(current_person):
    """The children of a person can printed using this function.

    Parameters:
      current_person:
        The current Person object.

    Returns:
      The current Person object.
    """
    ch_lst = current_person.get_children()
    if len(ch_lst) == 0:
        print(f"No children found for {current_person.get_name()}.")
    else:
        print(f"Children of {current_person.get_name()}:")

    for child in ch_lst:
        print(f'- {child}')
    print()

    return current_person


def option8(current_person):
    """The grandchildren of a person can be printed using this function.

    Parameters:
      current_person:
        The current Person object.

    Returns:
      The current Person object.
    """
    ch_lst = current_person.get_children()
    if len(ch_lst) == 0:
        print(f"No grandchildren found for {current_person.get_name()}.")
    else:
        print(f"Grandchildren of {current_person.get_name()}:")

    for child in ch_lst:
        grand_ch_lst = child.get_children()
        for grandchild in grand_ch_lst:
            print(f'- {grandchild}')
    print()

    return current_person


def option10(current_person):
    """The cousins of a person can printed using this function.

    Parameters:
      current_person:
        The current Person object.

    Returns:
      The current Person object.
    """
    parent = current_person.get_parent()
    uncle_aunt_lst = []
    if parent is not None:
        granny = parent.get_parent()
        if granny is not None:
            granny_ch_lst = granny.get_children()
            if len(granny_ch_lst) > 1:
                print(f"Cousins of {current_person.get_name()}:")
                for val in granny_ch_lst:
                    if not(val == parent):
                        uncle_aunt_lst.append(val)
            else:
                print(f"No cousins found for {current_person.get_name()}.")
        else:
            print(f"No cousins found for {current_person.get_name()}.")
    else:
        print(f"No cousins found for {current_person.get_name()}.")

    check = 0
    for uncle_aunt in uncle_aunt_lst:
        for child in uncle_aunt.get_children():
            print(f'- {child}')
            check = 1

    if check == 0:
        print(f"No cousins found for {current_person.get_name()}.")
    print()

    return current_person


def option9(current_person):
    """The aunts and uncles of a person can be printed using this function.

    Parameters:
      current_person:
        The current Person object.

    Returns:
      The current Person object.
    """
    parent = current_person.get_parent()
    if parent is not None:
        granny = parent.get_parent()
        if granny is not None:
            granny_ch_lst = granny.get_children()
            print(f"Aunts and uncles of {current_person.get_name()}:")
            for val in granny_ch_lst:
                if not(val == parent):
                    print(f'- {val}')
        else:
            print(f"No aunts and uncles found for {current_person.get_name()}.")
    else:
        print(f"No aunts and uncles found for {current_person.get_name()}.")

    print()
    return current_person


def menu(option, current_person):
    """This function takes the option user enters and calls the function related
    to that option.

    Parameters:
      option:
        The option entered by the user.
      current_person:
        The current Person object.

    Returns:
      Calls the function related to that option.
    """
    fun_list = [option1, option2, option3, option4, option5, option6, option7, option8,
                option9, option10, option11, option12]
    for i in range(12):
        if option == i + 1:
            return fun_list[i](current_person)


def main():
    current_person = Person('John Doe', '1960-01-15', '2020-01-15')
    header(current_person)
    option = int(input('Select option (or 0 to exit): '))
    print()

    while option != 0:
        current_person = menu(option, current_person)
        header(current_person)
        option = int(input('Select option (or 0 to exit): '))
        print()
    print()


if __name__ == '__main__':
    main()